from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
    # id = models.IntegerField(primary_key = True, null = False)
    # user_name = models.CharField(max_length = 25, null = False)
    # name = models.CharField(max_length = 25, null = False)
    # surname = models.CharField(max_length= 25)
    # username = models.CharField(max_length = 25, null = True, unique = False)
    avatar = models.ImageField(upload_to = 'images/avatar')
    email = models.EmailField(max_length = 35, null = False, unique = True)
    description = models.TextField(max_length = 500)
    birthday = models.DateField(auto_now = True)
    # password = models.CharField(null = False, max_length = 50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []