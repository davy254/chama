from unicodedata import name
from django.urls import path
from.views import  index, homepage


urlpatterns = [
    #path('', index, name='landing'),
    path('', homepage, name='home'),

    
]

