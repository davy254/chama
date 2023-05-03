from django.test import Client, TestCase
from django.urls import reverse
from core.models import Contribution
from .models import Member,Loan
from .forms import MemberForm

# Create your tests here.

class ContributionModelTest(TestCase):
    def setUp(self):
        self.member = Member.objects.create(first_name="David", last_name="Batista")
        self.contribution = Contribution.objects.create(member= self.member, 
                                                        month = "May",
                                                        amount= 200,
                                                        contributed = True
                                                         )
        self.client = Client()



    def test_create_member_view(self):
        url = reverse('new-member')
        response = self.client.post(url, {'first_name':self.member.first_name,
                                            'last_name': self.member.last_name})
        self.assertEqual(response.status_code, 200)