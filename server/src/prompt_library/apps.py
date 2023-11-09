from django.apps import AppConfig

class AppConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prompt_library'

    def ready(self) -> None:
        """
        Called once the application is loaded to perform startup tasks.
        """
        pass