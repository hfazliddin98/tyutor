from django.apps import AppConfig


class TopshiriqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topshiriq'

    def ready(self):
        import topshiriq.signals  # Signalni yuklash
