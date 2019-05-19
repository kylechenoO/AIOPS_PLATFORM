import time
import psutil
import datetime
from pytz import utc
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

def job():
    with open('./log.txt', 'a') as fp:
        now = datetime.datetime.now()
        boot_time = psutil.boot_time()
        result = '[{}][{}]\n'.format(now, boot_time)
        fp.write(result)


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
sched = BackgroundScheduler(jobstores = jobstores, executors = executors, job_defaults = job_defaults, timezone = utc)
## sched = BlockingScheduler(jobstores = jobstores, executors = executors, job_defaults = job_defaults, timezone = utc)
## sched.add_job(job, 'cron', second = '*/2')
sched.start()
while True:
    time.sleep(1)
