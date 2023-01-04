from django.shortcuts import render
from django.views.generic import CreateView
from members.models import Member


# Render Landinpage
def index(request):
    return render(request, 'core/index.html')







    

