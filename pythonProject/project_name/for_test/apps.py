from django.apps import AppConfig

class ForTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'for_test'

    def ready(self):
        import for_test.signals  # Импорт файла с сигналами

