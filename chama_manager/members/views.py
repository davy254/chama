from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import CreateView
from matplotlib.style import context
from .models import Contribution, Loan, Member
from .forms import LoanForm, MemberForm, ContributionForm

# Create your views here.

def homepage(request):
    form = MemberForm()
    member_total_contribution = Member.objects.annotate(total_cont=Sum('contribution__amount'))
    total_contribution = Contribution.objects.aggregate(Sum('amount'))
    context = {'form': form,
        'members': member_total_contribution,
        'total_contribution':total_contribution,
    }
    return render(request, 'members/homepage.html', context)

def create_member(request):
    add_member_form = MemberForm()
    if request.method == 'POST':
        add_member_form = MemberForm(request.POST)
        if add_member_form.is_valid():
            add_member_form.save()
        
    add_member_form = MemberForm()
    context = { 'add_member_form': add_member_form,}
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
    add_member_form = MemberForm()
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ContributionForm()
    context = { 'form': form,'add_member_form':add_member_form}
    return render(request, 'members/make_contribution.html', context)

def view_contributions(request):
    add_member_form = MemberForm()
    context = { 'add_member_form': add_member_form,}
    return render(request, 'members/view_contributions.html', context)


def show_contributions(request, month):
    add_member_form = MemberForm()
    contr = Contribution.objects.filter(month=month)
    month_contribution = Contribution.objects.filter(month=month)
    sum_month_contribution = month_contribution.aggregate(Sum('amount'))
    context = {
        'contr':contr,
        'month':month,
        'sum_month_contribution':sum_month_contribution,
        'add_member_form':add_member_form
    }
    return render(request, 'members/show_contributions.html', context)

def take_loan(request):
    add_member_form = MemberForm()
    form = LoanForm()
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-loans')
    form = LoanForm()
    context = { 'form': form,'add_member_form':add_member_form}
    return render(request, 'members/make_contribution.html', context)
    
def show_loans(request):
    add_member_form = MemberForm()
    loans = Loan.objects.all()
    context = {
        'loans':loans,
        'add_member_form':add_member_form
        
    }
    return render(request, 'members/show_loans.html', context)


