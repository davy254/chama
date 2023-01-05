from django.urls import  path
from .views import homepage,create_member,remove_member,make_contribution


urlpatterns = [
    path('home/', homepage, name='home'),
    path('create-member/', create_member, name='new-member'),
    path('remove-member/<int:pk>/', remove_member, name='remove-member'),
    path('make-contribution/', make_contribution, name='make-contribution'),


    

]