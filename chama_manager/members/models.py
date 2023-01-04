from django.db import models
from flask_sqlalchemy import Model
from sqlalchemy import false



# Model of members
class Member(models.Model):
    """
        Details of a member
    """
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

#Model of contribution
class Contribution(models.Model):
    """
        Contribution detail of a member
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    contributed = models.BooleanField(default=false)


#Model of Month
class Month(models.Model):
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
    month = models.CharField( max_length=3 , choices=months)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)