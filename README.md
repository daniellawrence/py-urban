py-urban
============

py-urban is a client for urbandictionary.com.

Project forked from https://github.com/novel/py-urbandict

Usage
------

Get a sinle word as dict

	>>> import urbandict
	>>> urbandict.get_random_word()
	INFO:root:Processed word 'hindsight'
	{u'down': 21, u'meaning': u'  Recognition of the realities, possibilities of events, situations,decisions etc     after they have occurred', u'word': u'hindsight', u'up': 140, u'example': u'  In hindsight, we should have acted differently when Chris told us he was gay, now hes not talking to us  '}


Get a number of words, and write it to a file

	>>> import urbandict
	>>> urbandict.get_n_random_words(2)
	INFO:root:Processed word 'base jumping'
	INFO:root:Processed word 'Clingy'
	INFO:root:Writing output as /tmp/urbandict_2_words.json

Get a single word, return as a dict

	>>> urbandict.get_word("python")
	INFO:root:Processed word 'python'
	{u'down': 172, u'meaning': u"Python is a powerful high-level interpreted language\nPython's design is notably clean, elegant, and well thought through; it tends to attract the sort of programmers who find Perl grubby and exiguous", u'word': u'python', u'up': 477, u'example': u'#!/usr/bin/python\rprint "Hello World"'}
	>>>

Get many words, returned as list of dicts 

	>>> import pprint
    >>>  import urbandict
	>>> pprint.pprint(urbandict.get_words(['python', 'ruby']))
	INFO:root:Processed word 'python'
	INFO:root:Processed word 'Ruby'
	INFO:root:Writing output as /tmp/urbandict_python,ruby.json
	[{u'down': 172,
	 u'example': u'#!/usr/bin/python\rprint "Hello World"',
	 u'meaning': u"Python is a powerful high-level interpreted language\nPython's design is notably clean, elegant, and well thought through; it tends to attract the sort of programmers who find Perl grubby and exiguous",
	 u'up': 477,
	 u'word': u'python'},
	{u'down': 748,
	 u'example': u"Tom: I think I saw her, was she that, that, that Ruby?\r Rory: 'Yeah, that's the one, she had nice hair\n'",
	 u'meaning': u"That mysterious girl that you saw once, but don't know whether you'll see her again\nnice hair!",
	 u'up': 2444,
	 u'word': u'Ruby'
	}]
	>>> 
