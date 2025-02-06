import time
from celery import shared_task

@shared_task
def delayed_message():
    time.sleep(2)  # 2 soniya kutish
    return "Salom! Bu 2 soniyadan keyin kelgan javob."


