from django.shortcuts import render
from .models import Contribution
from members.models import Member
from django.db.models import Sum



# Render Landinpage
def index(request):
    return render(request, 'core/index.html')


#Render the homepage showing all members and their total contribution
def homepage(request):
    member_total_contribution = Member.objects.annotate(total_cont=Sum('contribution__amount'))
    total_contribution = Contribution.objects.aggregate(Sum('amount'))
    context = {
        'members': member_total_contribution,
        'total_contribution':total_contribution,
    }
    return render(request, 'core/homepage.html', context)






    

