from django.apps import AppConfig
from topshiriq.tasks import start_scheduler


class TopshiriqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topshiriq'

    def ready(self):
        start_scheduler()  # Scheduler faqat bir marta boshlanadi
        import topshiriq.signals  # Signalni yuklash
