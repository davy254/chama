from django.contrib import admin
from .models import Member,Contribution , Month

# Register your models here.
admin.site.register(Member)
admin.site.register(Contribution)
admin.site.register(Month)