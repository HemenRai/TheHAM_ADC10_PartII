from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=50)
    category= models.CharField(max_length=50)
    job_type= models.CharField(max_length=50)
    salary= models.IntegerField()
    description = models.TextField()
    file = models.FileField()

    def __str__(self):
        return str(self.id)+ " " +self.title + " " +self.category + " " + self.job_type + " " + str(self.salary) +" " + self.description