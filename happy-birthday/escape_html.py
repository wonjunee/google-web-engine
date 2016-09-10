import cgi
def escape_html(s):
	# for (i, o) in (("&", "%amp;"),
	# 			   (">", "&gt;"),
	# 			   ("<", "&lt;"),
	# 			   ('"', "&quote;")):
	# 	s = s.replace(i,o)
	# return s
	return cgi.escape(s, quote = True)

s = "<b>html</b>&lt;"

# print escape_html(s)

from HTMLParser import HTMLParser
print HTMLParser.unescape.__func__(HTMLParser,s)