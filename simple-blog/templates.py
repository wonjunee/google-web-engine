import os
import re
import jinja2
import webapp2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape=True)

class BlogHandler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(BlogHandler):
	def get(self):
		self.write("Hello, Udacity!")


###### blog stuff

def blog_key(name = 'default'):
	return db.Key.from_path('blogs', name)

class Post(db.Model):
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	last_modified = db.DateTimeProperty(auto_now = True)

	def render(self):
		self._render_text = self.content.replace('\n', '<br>')
		return render_str("post.html", p = self)

class BlogFront(BlogHandler):
	def get(self):
		posts = Post.all().order('-created')
		self.render('front.html', posts = posts)

class PostPage(BlogHandler):
	def get(self, post_id):
		key = db.GqlQuery("select * from Post order by created desc limit 10")
		self.render('front.html', posts = posts)

class PostPage(BlogHandler):
	def get(self, post_id):
		key = db.Key.from_path('Post', int(post_id), parent=blog_key())
		post = db.get(key)

		if not post:
			self.error(404)
			return

		self.render("permalink.html", post = post)
		
class Art(db.Model):
	# defining type. required makes sure the data is not empty
	title = db.StringProperty(required = True)
	art = db.TextProperty(required = True)

	# auto_now_add: current time
	created = db.DateTimeProperty(auto_now_add = True)

class MainPage(BlogHandler):
	def render_front(self, title="", art="", error=""):
		# Gql always starts from select *
		arts = db.GqlQuery("select * from Art order by created DESC")
		self.render("front.html", title=title, art=art, error=error, arts=arts)

	def get(self):
		self.render_front()

	def post(self):
		title = self.request.get("title")
		art = self.request.get("art")

		if title and art:
			# don't need to put datetime because
			# it will be created automatically
			a = Art(title=title, art=art)
			a.put()

			# to avoid reload error message
			self.redirect("/")
		else:
			error = "we need both a title and some artwork!"
			self.render_front(title, art, error)

app = webapp2.WSGIApplication([

	('/', MainPage)

], debug=True)
