# from django.apps import AppConfig
# from baxo.tasks import baxo_start_scheduler


# class BaxoConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'baxo'

#     def ready(self):
#         baxo_start_scheduler()



from django.apps import AppConfig

class BaxoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'baxo'

    def ready(self):
        import baxo.signals  # Signalni yuklaymiz

