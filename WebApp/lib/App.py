'''
    App.py Lib
    Written By Kyle Chen
    Version 20190401v1
'''

# import buildin pkgs
import os
import re
import logging
from flask import Flask
from flask_restful import Api
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from logging.handlers import RotatingFileHandler

## import priviate pkgs
from IndexPage import IndexPage
from SignInPage import SignInPage
from SignUpPage import SignUpPage

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
        self.app = Flask(__name__, template_folder = '../templates')
        self.app.secret_key = os.urandom(24)
        self.api = Api(self.app)

        ## set up login manager
        self.login_manager = LoginManager()
        self.login_manager.session_protection = 'strong'
        self.login_manager.login_view = 'signinpage'
        self.login_manager.login_message = 'Unauthorized User'
        self.login_manager.login_message_category = 'info'
        self.login_manager.init_app(self.app)
        self.csrf = CSRFProtect()
        self.csrf.init_app(self.app)

    ## run func
    def run(self):
        ## set route
        self.api.add_resource(IndexPage, '/')
        self.api.add_resource(SignInPage, '/sign_in')
        self.api.add_resource(SignUpPage, '/sign_up')

        ## run app
        self.app.run(
            host = self.LISTEN_IP,
            port = self.LISTEN_PORT,
            debug = self.DEBUG,
            use_reloader = False
        )

