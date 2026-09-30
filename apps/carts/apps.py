from django.apps import AppConfig


class CartsConfig(AppConfig):
    name = 'apps.carts'

class CartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.carts'
    verbose_name = 'Корзины'
    def ready(self):
        import apps.carts.signals # noqa    
