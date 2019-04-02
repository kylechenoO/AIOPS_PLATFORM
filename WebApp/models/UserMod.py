'''
    UserMod.py Lib
    Written By Kyle Chen
    Version 20190402v1
'''

# import buildin pkgs
from flask_login import UserMixin
from DBConnector import DBConnector

## User Mod Class
class UserMod(UserMixin):
    ## initial UserMod
    def __init__(self, user_name):
        self.user_name = user_name
        id = self.getId(self.user_name)

    ## get user id
    def getId(self, user_name):
        if self.user_name is not None:
            return(True)

    ## create user func
    def createUser(self, password, email, group_list = '',
        role_list = '', business_system_list = ''):
        dbconnectorObj = DBConnector()
        SQL = "INSERT INTO sys_user(user_name, password, email, group_list, role_list, business_system_list) VALUES('{}', '{}', '{}', '{}', '{}', '{}');".format(
            self.user_name, password, email, group_list, role_list, business_system_list)
        result = dbconnectorObj.run('insert', SQL)
        return(result)

    ## getPassword func
    def getPassword(self):
        dbconnectorObj = DBConnector()
        result = []
        SQL = "SELECT password FROM sys_user WHERE user_name = '{}';".format(self.user_name)
        result = dbconnectorObj.run('select', SQL)
        if result != []:
            result = result[0][0]

        else:
            result = ''

        return(result)
