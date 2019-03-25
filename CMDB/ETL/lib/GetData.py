'''
    GetData.py Lib
    Written By Kyle Chen
    Version 20190325v1
'''

# import buildin pkgs
import pika

## GetData Class
class GetData(object):
    ## initial function
    def __init__(self, logger, config, ci_list):
        self.logger = logger
        self.MQ_SERVERS = config.MQ_SERVERS
        self.MQ_PORT = config.MQ_PORT
        self.MQ_QUEUE = config.MQ_QUEUE
        self.ci_list = ci_list

    ## get data from server
    def getData(self, server, queue):
        self.logger.debug('Getting [{}] from [{}] Start'.format(queue, server))
        with pika.BlockingConnection(pika.ConnectionParameters(host = server,
                                        port = self.MQ_PORT)) as conn:
            ## NOT DONE YET
            pass
        self.logger.debug('Getting [{}] from [{}] Done'.format(queue, server))
        return(True)

    ## run func
    def run(self):
        self.logger.debug('Getting Data Start')
        for server in self.MQ_SERVERS:
            self.getData(server, self.MQ_QUEUE)

        self.logger.debug('Getting Data End')
        return(True)
