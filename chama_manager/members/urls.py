from django.urls import  path
from .views import members


urlpatterns = [
    path('', members, name='members')
]