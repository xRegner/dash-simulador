from django.apps import AppConfig


class InicioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inicio'

    def ready(self):
        import inicio.dash_apps.simple_dash_app  # Importa la aplicación Dash
