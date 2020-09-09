from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    user_address = models.CharField(max_length=100, default='No address inserted')
    user_mobile_no = models.BigIntegerField(default=9999999999)
    