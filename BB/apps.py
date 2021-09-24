from django.apps import AppConfig


class BbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BB'

    def ready(self):
        import BB.signals
