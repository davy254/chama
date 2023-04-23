import imp
from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save
from .models import Member


class MembersConfig(AppConfig):
    name = 'members'

    def ready(self):
        from .signals import create_user
        pre_save.connect(create_user)

