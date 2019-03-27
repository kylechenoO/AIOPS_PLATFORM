'''
    MariaDB.py Lib
    Written By Kyle Chen
    Version 20190327v1
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
    
    ## run func
    def insertDB(self, SQL):
        self.logger.debug('[{}]Insert DataBase Start'.format(self.name))
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
            self.logger.debug('[{}]Insert DataBase Error [{}]'.format(self.name, e))
            return(False)

        self.logger.debug('[{}]Insert DataBase End'.format(self.name))
        return(True)
