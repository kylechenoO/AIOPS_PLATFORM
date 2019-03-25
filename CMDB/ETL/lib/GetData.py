'''
    GetData.py Lib
    Written By Kyle Chen
    Version 20190325v1
'''

# import buildin pkgs
import pika
import time

## GetData Class
class GetData(object):
    ## initial function
    def __init__(self, logger, config, ci_list):
        self.logger = logger
        self.MQ_SERVERS = config.MQ_SERVERS
        self.MQ_PORT = config.MQ_PORT
        self.MQ_QUEUE = config.MQ_QUEUE
        self.BUFFER_SIZE = config.SYS_BUFFER_SIZE
        self.BUFFER_WAIT = config.SYS_BUFFER_WAIT
        self.buff_count = self.BUFFER_SIZE
        self.buff = []
        self.ci_list = ci_list

    ## insert into MariaDB
    def insertDB(self):
        print('[insertDB][{}]'.format(self.buff))
        return(True)

    ## get data from server
    def getData(self, server, queue):
        def callback(ch, method, properties, body): 
            ##print('[RAW][{}][{}][{}]'.format(ch, method, properties))
            ##print("[SIZE = {}][DATA][{}]".format(self.buff, body))
            self.buff.append(body)
            ch.basic_ack(delivery_tag = method.delivery_tag)
            self.buff_count -= 1

            if self.buff_count == 0:
                self.insertDB()
                time.sleep(self.BUFFER_WAIT)
                self.logger.debug('Waiting for data...')
                self.buff = []
                self.buff_count = self.BUFFER_SIZE

        self.logger.debug('Getting [{}] from [{}] Start'.format(queue, server))
        with pika.BlockingConnection(pika.ConnectionParameters(host = server,
                                        port = self.MQ_PORT)) as conn:
            chan = conn.channel()
            q = chan.queue_declare(queue = queue, durable = True)
            chan.basic_qos(prefetch_count = 1)
            chan.basic_consume(callback, queue = queue, no_ack = False)
            try:
                chan.start_consuming()

            except KeyboardInterrupt:
                chan.stop_consuming()

        self.logger.debug('Getting [{}] from [{}] Done'.format(queue, server))
        return(True)

    ## run func
    def run(self):
        self.logger.debug('Getting Data Start')
        for server in self.MQ_SERVERS:
            self.getData(server, self.MQ_QUEUE)

        self.logger.debug('Getting Data End')
        return(True)
