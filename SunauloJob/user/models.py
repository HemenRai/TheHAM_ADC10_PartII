from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    companyName= models.CharField(max_length=60)
    companyAddress = models.CharField(max_length=60)
    companyContactNo = models.IntegerField()

    def __str__(self):
        return f"{self.companyName} is located at {self.companyAddress} and phone number is {self.companyContactNo}"

    

class JobPost(models.Model):
    jobName = models.CharField(max_length=60)
    jobType = models.CharField(max_length=20)
    postedDate = models.DateField()
    deadline = models.DateField()
    jobPost = models.FileField()
    jobProvider = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    
    
    
class JobSeeker(models.Model):
    jobSeekerName= models.CharField(max_length=60)
    jobSeekerAddress = models.CharField(max_length=60)
    jobSeekerContactNo = models.IntegerField()
    applyJob = models.ManyToManyField(JobPost, related_name = "applyJob")


    
class Feedback(models.Model):
    title = models.CharField(max_length=60)
    comments = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

