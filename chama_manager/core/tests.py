from django.test import TestCase
from .models import Contribution
from members.models import Member,Loan

# Create your tests here.

class ContributionModelTest(TestCase):
    def setUp(self):
        self.member = Member.objects.create(first_name="David", last_name="Munyiri")
        self.contribution = Contribution.objects.create(member= self.member, 
                                                        month = "May",
                                                        amount= 200,
                                                        contributed = True
                                                         )
        self.loan = Loan.objects.create(paid = "PENDING",
                                        month = "Dec",
                                        member = self.member,
                                        amount = 1000,
                                        )

    def test_member_creation(self):
        self.assertEqual(self.member.first_name, "David")
        self.assertEqual(self.member.last_name, "Munyiri")


    def test_contribution_made(self):
        self.assertEqual(self.contribution.member, self.member)
        self.assertEqual(self.contribution.amount, 200)
        self.assertEqual(self.contribution.month, "May")
        self.assertEqual(self.contribution.contributed, True)

    def test_member_loan_taking(self):
        self.assertEqual(self.loan.member, self.member)
        self.assertEqual(self.loan.amount, 1000)
        self.assertEqual(self.loan.month, "Dec")
        self.assertEqual(self.loan.paid, "PENDING")




        
