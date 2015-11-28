#!/usr/bin/env python
import json
import logging
import requests
import bs4


MAX_LENGTH = 250
MIN_UPVOTES = 200


logging.basicConfig(level=logging.INFO)
requests_logger = logging.getLogger("requests")
requests_logger.setLevel(logging.WARNING)


def process_word_html(raw_html):
    soup = bs4.BeautifulSoup(raw_html, "html.parser")

    word = {}
    for i in soup.find_all('a'):
        if 'class' not in i.attrs:
            continue
        tags = set(i.attrs['class']) & set(['up', 'down', 'word'])
        if not tags:
            continue
        tag = "".join(tags)
        text = i.text.strip()
        if tag in word:
            continue
        if tag in ('up', 'down'):
            text = int(text)
        word[tag] = text

    for i in soup.find_all('div'):
        if 'class' not in i.attrs:
            continue
        tags = set(i.attrs['class']) & set(['meaning', 'example'])
        if not tags:
            continue

        tag = "".join(tags)
        text = ""
        sentences = i.text.strip().split('.')
        for sentence in sentences:
            sentence_length = len(sentence)
            if len(text) + sentence_length > MAX_LENGTH:
                continue
            text += "  " + sentence

        if tag in word:
            continue

        word[tag] = text
    logging.info("Processed word '{0}'".format(word['word']))
    return word


def get_random_word():
    random_url = "http://www.urbandictionary.com/random.php"

    logging.debug("Getting random word from {0}".format(random_url))
    word_html = requests.get(random_url).text
    return process_word_html(word_html)


def get_words(words):
    word_list = []
    for word in words:
        word_list.append(get_word(word))

    out_file = "/tmp/urbandict_{0}.json".format(",".join(words))
    logging.info("Writing output as {0}".format(out_file))
    with open(out_file, 'w') as f:
        f.write(json.dumps(word_list, indent=4))


def get_word(word):
    single_url = "http://www.urbandictionary.com/define.php?term={0}".format(word)
    word_html = requests.get(single_url).text
    word_dict = process_word_html(word_html)
    return word_dict


def get_n_random_words(number_of_words=10, min_upvotes=MIN_UPVOTES):
    words = [get_random_word() for _ in range(int(number_of_words))]

    good_words = []
    for word in words:
        if word['up'] < int(min_upvotes):
            logging.debug("Skipping {0[word]} as upvotes={0[up]} < required={1}".format(word, min_upvotes))
            continue
        good_words.append(word)
        continue

    out_file = "/tmp/urbandict_{0}_words.json".format(number_of_words)
    logging.info("Writing output as {0}".format(out_file))
    with open(out_file, 'w') as f:
        f.write(json.dumps(good_words, indent=4))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Make a json file of random urbandict words.')
    parser.add_argument('--words', '-w', dest='number_of_words', default=10,
                        help="Number of random words to get")
    parser.add_argument('--votes', '-u', dest='min_upvotes', default=200,
                        help="Required number of upvotes")
    parser.add_argument('words', nargs='*', help="Define a word")

    args = parser.parse_args()
    if args.words:
        get_words(args.words)
    else:
        get_n_random_words(int(args.number_of_words), args.min_upvotes)
