from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', view_signup_user),
    path('login/',view_login_user),
    path('logout/',logout_user),
    path('profile/',user_profile),
    path('resume/',upload_resume,),
    path('resume/save',save_resume),
    path('feedback/', feedback),
    path('feedback/save', save_feedback),
]