'''
    SendData.py Lib
    Written By Kyle Chen
    Version 20190324v1
'''

# import buildin pkgs
import pika
from random import randint

## SendData Class
class SendData(object):
    ## initial function
    def __init__(self, logger, config, ci_list):
        self.logger = logger
        self.SYS_CSV_DIR = config.SYS_CSV_DIR
        self.MQ_SERVERS = config.MQ_SERVERS
        self.MQ_PORT = config.MQ_PORT
        self.MQ_QUEUE = config.MQ_QUEUE
        self.ci_list = ci_list

    ## readCSV function
    def readCSV(self, ci, file_name):
        result = []
        with open(file_name) as fp:
            next(fp)
            data_raw = fp.read()

        result = data_raw.split('\n')
        result.remove('')
        result = [ '{}###{}'.format(ci, line) for line in result ]
        return(result)

    ## get random server
    def getRandomServer(self):
        result = self.MQ_SERVERS[randint(0, len(self.MQ_SERVERS) - 1)]
        return(result)

    ## send data to server
    def sendData(self, server, queue, ci, data):
        self.logger.debug('Sending [{}] to [{}] Start'.format(ci, server))
        ## conn = pika.BlockingConnection(
                    ## pika.ConnectionParameters(server)
                ## )

        with pika.BlockingConnection(pika.ConnectionParameters(host = server,
                                        port = self.MQ_PORT)) as conn:
            for line in data:
                chan = conn.channel()
                chan.queue_declare(queue = queue, durable = True)
                chan.basic_publish(exchange = '', routing_key = queue, body = line,
                                    properties = pika.BasicProperties(delivery_mode = 2, ))
        self.logger.debug('Sending [{}] to [{}] Done'.format(ci, server))
        return(True)

    ## run func
    def run(self):
        self.logger.debug('Sending Data Start')
        for ci in self.ci_list:
            file_name = '{}/{}.csv'.format(self.SYS_CSV_DIR, ci)
            data = self.readCSV(ci, file_name)
            server = self.getRandomServer()
            self.sendData(server, self.MQ_QUEUE, ci, data)

        self.logger.debug('Sending Data End')
        return(True)
