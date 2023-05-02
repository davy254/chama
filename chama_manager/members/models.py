from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404






# Model of members
class Member(models.Model):
    """
        Details of a member
    """
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.first_name)


@receiver(post_save, sender=Member)
def create_user(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(
            username='@' + instance.first_name + '_' + instance.last_name, 
            email= '', 
            password='password')
        

@receiver(pre_delete, sender=Member)
def delete_user(sender, instance , **kwargs):
    print('statr user removal')
    try:
        user = get_object_or_404(User,username='@' + instance.first_name + '_' + instance.last_name)
        print(user)
        user.delete()
        
    except User.DoesNotExist:
        print('user not found')




    

#Model of loan
class Loan(models.Model):
    """
        loan detail of a member
    """
    status = [("PAID","PAID"),("PENDING","PENDING")]
    months =[
        ("JAN","January"),
        ("FEB","February"),
        ("MAR","March"),
        ("APR","April"),
        ("MAY","May"),
        ("JUN","June"),
        ("JUL","July"),
        ("AUG","August"),
        ("SEP","September"),
        ("OCT","October"),
        ("NOV","November"),
        ("DEC","December"),    
    ]
    month = models.CharField( max_length=3 , choices=months, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=0)
    paid = models.CharField(max_length=20, choices=status, null=True)

    def __str__(self) -> str:
        return '%s  %d loan in %s' % (self.member,self.amount, self.month)



