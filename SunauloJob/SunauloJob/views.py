from django.shortcuts import render, redirect
from django.db.models import Q
from postjob.models import Post

def view_home(request):
    return render(request,"home.html")

def search_data(request):
    search_term = ''
    search_term= request.POST['search']
    match = Post.objects.filter(Q(title__icontains=search_term) | Q(category__icontains=search_term) | Q(job_type__icontains=search_term))
    context_variable = {
        'posts':match
    }
    return render(request,'viewdata.html',context_variable)
