from django.shortcuts import render
from .models import Member

# Create your views here.

def members(request):
    context = {
        'members': Member.objects.all(),
    }
    
    return render(request, 'members/members.html', context)