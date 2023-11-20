from calendar import c
from django.test import Client, TestCase
from django.urls import reverse
from core.models import Contribution
from .models import Member,Loan
from .forms import ContributionForm, MemberForm

# Create your tests here.

class CreateViewTest(TestCase):
    def setUp(self):
        """
        seting up test fitures
        """
        self.form = {'first_name': 'Kevin', 'last_name': 'Hart'}
        self.member = Member.objects.create(first_name="David", last_name="Batista")
        self.contribution = Contribution.objects.create(member= self.member, 
                                                        month = "May",
                                                        amount= 200,
                                                        contributed = True
                                                         )
        self.client = Client()

    #testing form is submitting valid data
    def test_valid_form_submission(self):
        url = reverse('new-member')
        form = MemberForm(data=self.form) 
        self.assertTrue(form.is_valid())
        
    # testing that form is displayed
    def test_form_displayed(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains(response, 'form')


    # testing new member creation via form submission
    def test_create_member_view(self):
        url = reverse('new-member')
        response = self.client.post(url, data=self.form)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Member.objects.count(), 2)
        self.assertRedirects(response, reverse('home'))


    # testing remove meber function
    def test_remove_member_view(self):
        url = reverse('remove-member', args=[self.member.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Member.objects.count(), 0)
        self.assertRedirects(response, reverse('home'))


    # testing make contribution function

        
        
