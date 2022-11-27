from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'secretsantasu.apps.userprofile'

    def ready(self):
        from secretsantasu.apps.userprofile.signals import create_profile
        from django.contrib.auth.models import User
        from django.db.models.signals import post_save
        post_save.connect(create_profile, sender=User)
