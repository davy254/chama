from django.contrib import admin
from .models import Member,Contribution, Loan

# Register your models here.
admin.site.register(Member)
admin.site.register(Contribution)
admin.site.register(Loan)
