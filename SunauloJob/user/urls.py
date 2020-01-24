from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',view_login_user),
    path('profile/',user_profile),
]