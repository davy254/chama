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
