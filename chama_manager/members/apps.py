from email.policy import default
import imp
from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save
from .models import Member


class MembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'

    def ready(self):
        import members.signals
        

