import email
from click import password_option
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Member


@receiver(pre_save, sender=Member)
def create_user(sender, instance, created, **kwargs):
    print('signal received')
    if created:
        print('start user creation')
        user = User.objects.create_user(username=instance.first_name, email='' )
        user.set_password('password')
        user.save()






