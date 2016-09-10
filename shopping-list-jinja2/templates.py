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

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		# jinja will load the file from the templates path
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		# get_all: get all of food parameters and get them in the list
		items = self.request.get_all("food")

		# render the empty form.
		self.render("shopping_list.html", items = items)

class FizzBuzzHandler(Handler):
	def get(self):
		n = self.request.get('n', 0)
		n = n and int(n)
		self.render('fizzbuzz.html', n=n)

app = webapp2.WSGIApplication([

	('/', MainPage)

], debug=True)
