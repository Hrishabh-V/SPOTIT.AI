from django.apps import AppConfig

class SpAppConfig(AppConfig):
    """Configuration for the 'sp_app' application."""
    
    default_auto_field = 'django.db.models.BigAutoField'  # Use BigAutoField for primary keys by default
    name = 'sp_app'  # The name of the application
