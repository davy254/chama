from django import forms
from .models import Loan, Member, Contribution

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name']

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = '__all__'

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'



