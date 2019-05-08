import psutil
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    with open('/root/test/log.txt', 'a') as fp:
        now = datetime.datetime.now()
        boot_time = psutil.boot_time()
        result = '[{}][{}]\n'.format(now, boot_time)
        fp.write(result)

sched = BlockingScheduler()
sched.add_job(job, 'cron', second = '*/2')
sched.start()