from validation import *
import webapp2


form = """
<form method="post">
	What is your birthday?
	<br>

	<label> Month
		<input type="text" name="month">
	</label>

	<label> Day
		<input type="text" name="day">
	</label>

	<label> Year
		<input type="text" name="year">
	</label>
	<br>
	<br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
    	user_month = valid_month(self.request.get('month'))
    	user_day = valid_day(self.request.get('day'))
    	user_year = valid_year(self.request.get('year'))

    	if not (user_month and user_day and user_year):
    		self.response.out.write(form)
    	else:
    		self.response.out.write("Thanks!")

app = webapp2.WSGIApplication([

    ('/', MainPage)

], debug=True)
