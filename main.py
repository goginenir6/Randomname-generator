import webapp2
from httplib2 import Http
import json
import logging
from google.appengine.ext.webapp import template
from oauth2client.client import OAuth2Credentials
from oauth2client.appengine import OAuth2Decorator
# from oauth2client.contrib.appengine import OAuth2Decorator
import datetime, os
import logging
from google.appengine.api import users, app_identity, mail




class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(str(template.render('home.html', {})))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/login', login),
	# ('/submittoken', submittoken),
    # ('/logout', LogoutHandler),
    # (auth_enticated.callback_path, auth_enticated.callback_handler()),
], debug=True)
