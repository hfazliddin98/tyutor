from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, date




def topshiriq_active():
    from topshiriq.models import Topshiriq
    bugun = date.today()
    Topshiriq.objects.filter(
        active=False,
        vaqt_tugadi=False,
        boshlanish_vaqti__lte=bugun,
        tugash_vaqti__gte=bugun
        ).update(active=True)


def topshiriq_vaqt_tugadi():
    from topshiriq.models import Topshiriq
    bugun = date.today()
    Topshiriq.objects.filter(
        vaqt_tugadi=False,
        tugash_vaqti__lt=bugun
        ).update(active=False, vaqt_tugadi=True)


 


def start_scheduler():
    scheduler = BackgroundScheduler()

    # Har 8 sekundda birinchi vazifa
    scheduler.add_job(topshiriq_active, 'interval', hours=4, minutes=0, seconds=10)

    scheduler.add_job(topshiriq_vaqt_tugadi, 'interval', hours=4, minutes=5, seconds=15)

    scheduler.start()









