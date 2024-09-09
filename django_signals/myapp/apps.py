from django.apps import AppConfig



class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    
    
    def ready(self):
        # Import signals here to ensure they're registered
        import myapp.signals

