from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import CreateView
from matplotlib.style import context
from .models import Contribution, Member
from .forms import MemberForm, ContributionForm

# Create your views here.

def homepage(request):
    form = MemberForm()
    total_contribution = Member.objects.annotate(total_cont=Sum('contribution__amount'))
    context = {'form': form,
        'members': Member.objects.annotate(total_cont=Sum('contribution__amount')),
        'total_contribution':total_contribution,
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

def view_contributions(request):
    
    return render(request, 'members/show_contributions.html')
def show_contributions(request, month):
    contr = Contribution.objects.filter(month=month)
    context = {
        'contr':contr,
        'month':month
    }
    return render(request, 'members/show_contributions.html', context)
    



