import random

def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(5))
