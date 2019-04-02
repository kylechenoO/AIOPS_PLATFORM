'''
    UserMod.py Lib
    Written By Kyle Chen
    Version 20190402v1
'''

# import buildin pkgs
from flask_login import UserMixin
from App import DB_SQLAlchemy as db

## User Mod Class
class UserMod(UserMixin, db.Model):
    ## initial db section
    __tablename__='country'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True,
        unique = True, nullable = False)
    user_name = db.Column(db.String(32), unique = True, nullable = False)
    password =  db.Column(db.String(256), nullable = False)
    email =  db.Column(db.String(64), unique = True, nullable = False)
    group_list = db.Column(db.String(1024))
    role_list = db.Column(db.String(1024))
    business_system_list = db.Column(db.String(1024))

    ## initial UserMod
    def __init__(self, user_name):
        self.user_name = user_name
        id = self.getId(self.user_name)

    ## get user id
    def getId(self, user_name):
        if self.username is not None:
            return(1)

    ## create user func
    def createUser(self, user_name, password, email, group_list = '',
        role_list = '', business_system_list = ''):
        pass
