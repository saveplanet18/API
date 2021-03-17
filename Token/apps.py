from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'Token'

    def ready(self):
        import Token.signals