'''
    App.py Lib
    Written By Kyle Chen
    Version 20190330v1
'''

# import buildin pkgs
import os
import re
from flask import Flask
## from flask import Flask, render_template
## from flask_wtf.csrf import CSRFProtect
## from flask_login import login_user, login_required
## from flask_login import LoginManager, current_user
## from flask_login import logout_user

## import priviate pkgs
## from LoginForm import LoginForm
## from User import User

## App Class
class App(object):
    ## initial function
    def __init__(self, logger, config):
        ## initial valus
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.LISTEN_IP = config.SYS_LISTEN_IP
        self.LISTEN_PORT = config.SYS_LISTEN_PORT
        self.DEBUG = config.SYS_DEBUG

        ## some flask args
        self.app = Flask(__name__)

    def run(self):
        self.app.run(
            host = self.LISTEN_IP,
            port = self.LISTEN_PORT,
            debug = self.DEBUG,
            use_reloader = False
        )
