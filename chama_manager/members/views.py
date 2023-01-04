
from django.shortcuts import redirect, render

from django.views.generic import CreateView
from .models import Member
from .forms import MemberForm

# Create your views here.

def homepage(request):
    form = MemberForm()
    context = {'form': form,
        'members': Member.objects.all()
    }
    return render(request, 'members/homepage.html', context)

def create_member(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        
    form = MemberForm()
    context = { 'form': form,}
    return redirect('home' )



