from django.contrib import admin
from .models import Company,JobPost,JobSeeker,Feedback

# Register your models here.
admin.site.register(Company)
admin.site.register(JobPost)
admin.site.register(JobSeeker)
admin.site.register(Feedback)


