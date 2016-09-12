import os
import re
import jinja2
import webapp2

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
	return USER_RE.match(username)

PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
	return PASSWORD_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
	return EMAIL_RE.match(email)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

# jinja will look for templates in the specified path
# There are two ways of escaping html syntax
# You can use 'autoescape' in jinja2.Environment or
# you can use {{ name | escape}} in html
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
										autoescape = True)

def render_str(template, **params):
	# jinja will load the file from the templates path
	t = jinja_env.get_template(template)
	return t.render(params)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render(self, template, **kw):
		self.write(render_str(template, **kw))

class ROT13(Handler):
	def get(self):
		# render the empty form.
		self.render("ROT13.html")

	def post(self):
		content = ""
		pre_content = self.request.get("text")
		if pre_content:
			content = pre_content.encode('rot13')

		# render with content.
		self.render("ROT13.html", text = content)

class SignUp(Handler):
	def get(self):
		username = self.request.get("username")


app = webapp2.WSGIApplication([

	('/rot13', ROT13)

], debug=True)
