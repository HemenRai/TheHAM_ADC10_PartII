from django.test import TestCase
from .models import Company,JobPost,JobSeeker,Feedback
# Create your tests here.

class ModelTestCase(TestCase):

    def test_valid_company_name(self):
        company1 = Company.objects.create(companyName="HAM Company",companyAddress="KTM", companyContactNo=9812345678)
        self.assertEqual(company1.valid_company_name(),True)
        
    def test_valid_company(self):
        company2 = Company.objects.create(companyName="HAM Company",companyAddress="KTM", companyContactNo=9812345678)
        self.assertNotEqual(company2.valid_company(),True)

    def test_valid_job_seeker(self):
        jobSeeker = JobSeeker.objects.create(jobSeekerName="Ashim Adhikari", jobSeekerAddress= "Pokhara",jobSeekerContactNo= 9812324576)
        self.assertEqual(jobSeeker.valid_job_seeker(),False)

    def test_valid_job_contact(self):
        jobSeeker = JobSeeker.objects.create(jobSeekerName="Ashim Adhikari", jobSeekerAddress= "Pokhara",jobSeekerContactNo= 9812324576)
        self.assertFalse(jobSeeker.valid_job_contact())

    def test_valid_job_name(self):
        jobPost1 = JobPost.objects.create(jobName="Web designer", jobType="Full time")
        self.assertTrue(jobPost1.valid_job_name())

    