from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', view_signup_user),
]