'''
    User.py Lib
    Written By Kyle Chen
    Version 20190420v1
'''

# import buildin pkgs
import json
from flask import session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin, logout_user, login_required

## import priviate pkgs
from app import db, login_manager

## User Class
class User(UserMixin, db.Model):
    __tablename__ = 'sys_user'
    id = db.Column('id', db.Integer, primary_key = True, autoincrement = True)
    user_name = db.Column('user_name', db.String(32), nullable = False, unique = True)
    password = db.Column(db.String(256))
    email = db.Column('email', db.String(64), nullable = False, unique = True)
    group_list = db.Column('group_list', db.String(1024))
    role_list = db.Column('role_list', db.String(1024))
    business_system_list = db.Column('business_system_list', db.String(1024))

    ## initial func
    def __init__(self, user_name, password = None, email = None, group_list = None,
        role_list = None, business_system_list = None):
        self.user_name = user_name
        self.password = None if password is None else generate_password_hash(password)
        self.email = email
        self.group_list = group_list
        self.role_list = role_list
        self.business_system_list = business_system_list
        self.id = self.getId()

    ## __repr__ func
    def __repr__(self):
        result = {
            'id': self.id,
            'user_name': self.user_name,
            'password': self.password,
            'email': self.email,
            'group_list': self.group_list,
            'role_list': self.role_list,
            'business_system_list': self.business_system_list
        }
        return(json.dumps(result))

    ## createUser func
    def createUser(self):
        result = None
        if self.user_name is not None:
            try:
                db.session.add(self)
                db.session.commit()
                result = True

            except Exception as e:
                pass
                print('createUser [{}]'.format(e))

        return(result)

    ## verify password
    def verifyPassword(self, password):
        userObj = None
        if self.id is None:
            return(False)

        if password is None:
            return(False)

        else:
            userObj = self.getUserInfo()
            if check_password_hash(userObj.password, password):
                self.email = userObj.email
                self.group_list = userObj.group_list
                self.role_list = userObj.role_list
                self.business_system_list = userObj.business_system_list
                return(True)

    ## getUserInfo func
    def getUserInfo(self):
        result = None
        try:
            result = self.query.filter_by(user_name = self.user_name).first()

        except Exception as e:
            pass
            print('getUserInfo [{}]'.format(e))

        return(result)

    ## get func
    @staticmethod
    def getUser(user_id):
        result = None
        if user_id is None or user_id == '':
            pass

        else:
            try:
                result = db.session.query(User).filter(User.id == user_id).first().user_name

            except Exception as e:
                pass
                print('getUser [{}]'.format(e))

        return(User(result))

    ## getid func
    def getId(self):
        result = None
        if self.user_name is not None:
            try:
                result = self.query.filter_by(user_name = self.user_name).first().id

            except Exception as e:
                pass
                print('getID [{}]'.format(e))

        return(result)

    ## logout func
    @login_required
    def logout(self):
        logout_user()
        return(redirect(url_for('login')))

    ## is_active func
    def is_active(self):
        return(True)

    ## is_authenticated func
    def is_authenticated(self):
        return(True if session['user_id'] else False)

    ## is_anonymous func
    def is_anonymous(self):
        return(True if self.id is None else False)

    ## get_id func
    def get_id(self):
        return(self.id)
