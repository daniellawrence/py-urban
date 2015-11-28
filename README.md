py-urbandict
============

py-urbandict is a client for urbandictionary.com.

Projectf forked from https://github.com/novel/py-urbandict

Usage
------

Get a sinle word as dict()

	>>> import urbandict
	>>> dir(urbandict)
	['MAX_LENGTH', 'MIN_UPVOTES', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'bs4', 'get_n_random_words', 'get_random_word', 'json', 'logging', 'requests', 'requests_logger']
	>>> urbandict.get_random_word()
	INFO:root:Processed word 'hindsight'
	{u'down': 21, u'meaning': u'  Recognition of the realities, possibilities of events, situations,decisions etc     after they have occurred', u'word': u'hindsight', u'up': 140, u'example': u'  In hindsight, we should have acted differently when Chris told us he was gay, now hes not talking to us  '}


Get a number of words, and write it to a file

	>>> urbandict.get_n_random_words(2)
	INFO:root:Processed word 'base jumping'
	INFO:root:Processed word 'Clingy'
	INFO:root:Writing output as /tmp/urbandict_2_words.json

