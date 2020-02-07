from django.urls import path
from .views import *

urlpatterns = [
    path('company/',view_get_post_company),
    path('company/<int:ID>',view_getByID),
    path('<int:pagenumber>/<int:size>',get_company_pagination),
]