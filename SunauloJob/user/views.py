from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import *



# Create your views here.

def view_signup_user(request):
    if request.method=="GET":
        return render(request,'registration/signup.html')

    else:
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()    
        return HttpResponse("Registration Successful")

def logout_user(request):
    logout(request)  
    return redirect ("/user/login")

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
            return redirect("/user/profile")
        else:
            return HttpResponse("Authentication Failed")


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,"profile.html")
    else:
        return redirect("/user/login")
