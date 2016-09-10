import os

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

# jinja will look for templates in the specified path
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

hidden_html = """
<input type="hidden" name="food" value="%s">
"""
item_html = "<li>%s</li>"

shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

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
		# render the empty form.
		self.render("shopping_list.html", name="steve")

		# output = form_html
		# output_hidden = ""

		# # get_all: get all of food parameters and get them in the list
		# items = self.request.get_all("food")
		# if items:
		# 	output_items = ""
		# 	for item in items:
		# 		output_hidden += hidden_html % item
		# 		output_items += item_html % item

		# 	output_shopping = shopping_list_html % output_items
		# 	output += output_shopping

		# output = output % output_hidden

		# self.write(output)

app = webapp2.WSGIApplication([

	('/', MainPage)

], debug=True)
