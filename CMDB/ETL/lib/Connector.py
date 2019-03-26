'''
    Connector.py Lib
    Written By Kyle Chen
    Version 20190326v1
'''

# import buildin pkgs
import os
import re
import pika
import time

## import priviate pkgs
from CiConfig import CiConfig

## Connector Class
class Connector(object):
    ## initial function
    def __init__(self, logger, config, ci_list):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.workpath = config.workpath
        self.logger = logger
        self.MQ_SERVER = config.MQ_SERVER
        self.MQ_PORT = config.MQ_PORT
        self.MQ_QUEUE = config.MQ_QUEUE
        self.BUFFER_SIZE = config.SYS_BUFFER_SIZE
        self.BUFFER_WAIT = config.SYS_BUFFER_WAIT
        self.buff = []
        self.insert_flag = False
        self.ci_list = ci_list

    ## insert into MariaDB
    def getSQL(self, buff):
        for line in buff:
            ci = re.sub(r'###.*$', '', line)
            data = re.sub(r'^.*###', '', line)
            self.logger.debug('[{}][CI][{}]'.format(self.name, ci))
            self.logger.debug('[{}][DATA][{}]'.format(self.name, data))
            ciConfigObj = CiConfig(self.logger, self.workpath, ci)
            struct_dict = ciConfigObj.run()

        return(True)

    ## getQueueSize
    def getQueueSize(self, server, port, queue):
        result = 0
        with pika.BlockingConnection(pika.ConnectionParameters(host = server,
                        port = port)) as connection:
            channel = connection.channel()
            response = channel.queue_declare('asset', passive = True)
            result = response.method.message_count

        return(result)

    ## get data from server
    def getData(self, server, port, queue):
        ## callback func for fetching line from RabbitMQ
        def callback(ch, method, properties, body): 
            self.buff.append(body.decode('utf-8'))
            ch.basic_ack(delivery_tag = method.delivery_tag)
            queue_size = self.getQueueSize(server, port, queue)

            ## to check the queue size, for last batch
            ## if not use insert_flag, will get two '0' here
            ## at last I decide to handle it manually
            queue_size = self.getQueueSize(server, port, queue)
            if queue_size == 0 and (self.insert_flag == False):
                self.insert_flag = True
                return(True)

            ## for the last batch insert
            if queue_size == 0 and (self.insert_flag == True):
                self.getSQL(self.buff)
                self.buff = []
                self.insert_flag = False
                self.logger.debug('[{}]Waiting for data...'.format(self.name))
                time.sleep(self.BUFFER_WAIT)
                return(True)

            ## if the buffer is full, insert them
            if method.delivery_tag % self.BUFFER_SIZE == 0:
                self.getSQL(self.buff)
                self.buff = []
                self.logger.debug('[{}]Waiting for data...'.format(self.name))
                time.sleep(self.BUFFER_WAIT)
                return(True)

        self.logger.debug('[{}]Getting [{}] from [{}] Start'.format(self.name, queue, server))

        ## connect to RabbitMQ and fetch data
        with pika.BlockingConnection(pika.ConnectionParameters(host = server,
                                        port = port)) as conn:
            chan = conn.channel()
            chan.queue_declare(queue = queue, durable = True)
            chan.basic_qos(prefetch_count = 1)
            chan.basic_consume(callback, queue = queue, no_ack = False)
            try:
                chan.start_consuming()

            except KeyboardInterrupt:
                chan.stop_consuming()

        self.logger.debug('[{}]Getting [{}] from [{}] Done'.format(self.name, queue, server))
        return(True)

    ## run func
    def run(self):
        self.logger.debug('[{}]Getting Data Start'.format(self.name))
        self.getData(self.MQ_SERVER, self.MQ_PORT, self.MQ_QUEUE)

        self.logger.debug('[{}]Getting Data End'.format(self.name))
        return(True)
