from django.db import models
from django.contrib.auth.models import AbstractUser
# from .manager import *


class User(AbstractUser):
    # USERNAME_FIELD = 'username'
    phone = models.CharField(max_length=12)
    address = models.TextField()
    # objects = UserManager()

    class Meta():
        db_table = 'user' 



