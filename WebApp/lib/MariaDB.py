'''
    MariaDB.py Lib
    Written By Kyle Chen
    Version 20190402v1
'''

# import buildin pkgs
import os
import re
import pymysql

## MariaDB Class
class MariaDB(object):
    ## initial function
    def __init__(self, logger, host, port, user, password, database):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.database = database
    
    ## insert func
    def insertDB(self, SQL):
        self.logger.debug('[{}]Insert DataBase Start'.format(self.name))
        result = None
        try:
            conn =  pymysql.connect(host = self.host,
                    user = self.user,
                    passwd = self.password,
                    db = self.database,
                    port = self.port)
            with conn.cursor() as cur:
                self.logger.debug('[{}]Connect to mariadb success'.format(self.name))
                cur.execute(SQL)
                conn.commit()

        except Exception as e:
            result = str(e)
            self.logger.debug('[{}]Insert DataBase Error [{}]'.format(self.name, e))
            return(result)

        self.logger.debug('[{}]Insert DataBase End'.format(self.name))
        return('Insert Done')

    ## update func
    def updateDB(self, SQL):
        self.logger.debug('[{}]Update DataBase Start'.format(self.name))
        result = None
        try:
            conn =  pymysql.connect(host = self.host,
                    user = self.user,
                    passwd = self.password,
                    db = self.database,
                    port = self.port)
            with conn.cursor() as cur:
                self.logger.debug('[{}]Connect to mariadb success'.format(self.name))
                cur.execute(SQL)
                conn.commit()

        except Exception as e:
            result = e
            self.logger.debug('[{}]Update DataBase Error [{}]'.format(self.name, e))
            return(e)

        self.logger.debug('[{}]Update DataBase End'.format(self.name))
        return('Update Done')

    ## select func
    def selectDB(self, SQL):
        self.logger.debug('[{}]Select DataBase Start'.format(self.name))
        result = []
        try:
            conn =  pymysql.connect(host = self.host,
                    user = self.user,
                    passwd = self.password,
                    db = self.database,
                    port = self.port)
            with conn.cursor() as cur:
                self.logger.debug('[{}]Connect to mariadb success'.format(self.name))
                cur.execute(SQL)
                for line in cur:
                    result.append(line)

        except Exception as e:
            result = e
            self.logger.debug('[{}]Select DataBase Error [{}]'.format(self.name, e))
            return(e)

        self.logger.debug('[{}]Select DataBase End'.format(self.name))
        return(result)
