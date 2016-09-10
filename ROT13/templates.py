import os

import jinja2
import webapp2

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

class MainPage(Handler):
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

app = webapp2.WSGIApplication([

	('/', MainPage)

], debug=True)
