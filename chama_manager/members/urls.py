from django.urls import  path
from .views import ( homepage,create_member,
                    remove_member,make_contribution,
                    show_contributions, show_loans, view_contributions,
                    take_loan)


urlpatterns = [
    path('home/', homepage, name='home'),
    path('create-member/', create_member, name='new-member'),
    path('remove-member/<int:pk>/', remove_member, name='remove-member'),
    path('make-contribution/', make_contribution, name='make-contribution'),
    path('view-contribution/', view_contributions, name='view-contribution'),
    path('show-contribution/<str:month>/', show_contributions, name='show-contribution'),
    path('take-loan/', take_loan, name='take-loan'),
    path('show-loans/', show_loans, name='show-loans'),



]