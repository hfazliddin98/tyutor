from celery import shared_task

@shared_task
def xabar_message():
    print("Hello from Celery!")



