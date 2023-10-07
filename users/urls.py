from importlib.resources import path
from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('user_login', user_login.as_view()),
    path('user_signup', user_signup.as_view())
]