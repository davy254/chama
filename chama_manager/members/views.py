
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import CreateView
from .models import Member
from .forms import MemberForm, ContributionForm

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

def remove_member(request, pk):
    members = Member.objects.all()
    member = get_object_or_404(Member,pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('home')
    context = {'member':member}
    return render(request, 'members/remove_member.html', context)
    

def make_contribution(request):
    form = ContributionForm()
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ContributionForm()
    context = { 'form': form,}
    return render(request, 'members/make_contribution.html', context)
    



