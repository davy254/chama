from django.urls import  path
from .views import homepage,create_member,remove_member


urlpatterns = [
    path('home/', homepage, name='home'),
    path('create-member/', create_member, name='new-member'),
    path('remove-member/<int:pk>/', remove_member, name='remove-member'),

    

]