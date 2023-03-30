from django.db import models




# Model of members
class Member(models.Model):
    """
        Details of a member
    """
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

    



    

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



