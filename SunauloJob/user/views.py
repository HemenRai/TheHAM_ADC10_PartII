from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import *



# Create your views here.

def view_signup_user(request):
    if request.method=="GET":
        return render(request,'registration/signup.html')

    else:
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()    
    return redirect("/")



# Create your views here.
def view_login_user(request):
    if request.method =="GET":
        return render (request,'registration/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user,backend=None)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid input. Please input valid information.')
            return redirect("/user/login")
            

def logout_user(request):
    logout(request)  
    return redirect ("/")


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,"profile.html")
    else:
        return redirect("/user/login")


def upload_resume(request):
    if request.method=="GET":
        return render(request, 'resume/resume.html')  

def save_resume(request):
    if request.method=="POST":
        uploaded_resume = request.FILES.get("file")
        fs = FileSystemStorage()
        get_resume = fs.save(uploaded_resume.name, uploaded_resume)
        post_resume = Resume(file=get_resume)
        post_resume.save()
        return redirect ("/user/profile")


def feedback(request):
    return render(request,'feedback/feedback.html')

def save_feedback(request):
    if request.method == "POST":
        get_title = request.POST ['title']
        get_comments = request.POST ['comments']
        post_feedback = Feedback(title=get_title,comments =get_comments,)
        post_feedback.save()
        return HttpResponse ("Thank You For Your Feedback!!")