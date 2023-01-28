from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from matplotlib.style import context
from core.models import Contribution
from .models import Loan, Member
from .forms import LoanForm, MemberForm, ContributionForm




# functionality for adding a member
def create_member(request):
    add_member_form = MemberForm()
    if request.method == 'POST':
        add_member_form = MemberForm(request.POST)
        if add_member_form.is_valid():
            add_member_form.save()
            messages.success(request, 'New member added.')
        
    add_member_form = MemberForm()
    context = { 'add_member_form': add_member_form,}
    return redirect('home' )

# functionality for deleting a member
def remove_member(request, pk):
    members = Member.objects.all()
    member = get_object_or_404(Member,pk=pk)
    if request.method == 'POST':
        member.delete()
        messages.success(request,f'{member} has been removed.')
        return redirect('home')
    context = {'member':members, 'member':member}
    return render(request, 'members/remove_member.html', context)
    
# functionality for making contribution for a member
def make_contribution(request):
    members = Member.objects.all()
    form = ContributionForm()
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ContributionForm()
    context = { 'form': form, 'members':members}
    return render(request, 'members/make_contribution.html', context)


#view all contributions made by all members
def view_contributions(request):
    return render(request, 'members/view_contributions.html', context)

# show all contributions and total contribution for each month
def show_contributions(request, month):
    contr = Contribution.objects.filter(month=month)
    month_contribution = Contribution.objects.filter(month=month)
    sum_month_contribution = month_contribution.aggregate(Sum('amount'))
    context = {
        'contr':contr,
        'month':month,
        'sum_month_contribution':sum_month_contribution,
    }
    return render(request, 'members/show_contributions.html', context)

# take a loan functionality
def take_loan(request):
    members = Member.objects.all()
    form = LoanForm()
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-loans')
    form = LoanForm()
    context = { 'form': form, 'members':members}
    return render(request, 'members/make_contribution.html', context)

# show all loans taken    
def show_loans(request):
    loans = Loan.objects.all()
    context = {
        'loans':loans,
        
    }
    return render(request, 'members/show_loans.html', context)


