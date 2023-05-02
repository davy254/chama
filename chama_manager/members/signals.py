from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Member


       
@receiver(post_save, sender=Member)
def create_user(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.first_name, email='' , password='password')


# @receiver(pre_delete, sender=Member)
# def delete_user(sender, instance , **kwargs):
#     print('statr user removal')
#     try:
#         member = Member.objects.get(first_name= instance.first_name)
#         member.delete()
#         print(member + 'deleted')
#     except User.DoesNotExist:
#         print('user not found')




