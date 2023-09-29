from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import logging
import datetime
import atexit

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)  # This sets up basic logging to the console

last_run_time = None

@app.route('/')
def cron_status():
    global last_run_time
    return f"Last run time of the job: {last_run_time}"

def my_cron_job():
    global last_run_time
    last_run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    app.logger.info(f"Job run at: {last_run_time}")

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Schedule the job to run every minute
scheduler.add_job(
    func=my_cron_job,
    trigger=IntervalTrigger(minutes=1),
    id='my_cron_job_id',
    name='Print every 1 minute',
    replace_existing=True)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__': 
    app.run()
