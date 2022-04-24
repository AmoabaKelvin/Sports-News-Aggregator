from apscheduler.schedulers.background import BackgroundScheduler

from bot import get_and_send_updates

scheduler = BackgroundScheduler(timezone="UTC")


def job():
    """
    This function is called at 6am everyday.
    """
    get_and_send_updates()


scheduler.add_job(job, "cron", hour=6, minute=0, second=0)
scheduler.start()

while True:
    import time

    time.sleep(1)
