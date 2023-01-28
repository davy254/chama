from django.db import models

from members.models import Member

# Create your models here.
#Model of contribution
class Contribution(models.Model):
    """
        Contribution detail of a member
    """
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
    contributed = models.BooleanField(default=False)