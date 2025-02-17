from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from datetime import datetime
from django.conf import settings



# Yangi scheduler faqat bir marta yaratish
scheduler = None

def baxo_start_scheduler():
    global scheduler
    if scheduler is None:  # Faqat bir marta yaratilishini ta'minlash
        scheduler = BackgroundScheduler()


        scheduler.start()









