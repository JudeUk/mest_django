
from django.urls import path
from .views import *


urlpatterns = [
    path("user/", user_profile ),
     path("user_old/", user_profile )
   
]