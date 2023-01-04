from django.urls import  path
from .views import homepage,create_member


urlpatterns = [
    path('home/', homepage, name='home'),
    path('create-member/', create_member, name='new-member'),

    

]