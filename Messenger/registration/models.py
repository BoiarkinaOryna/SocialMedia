from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
    username = models.CharField(max_length = 25, null = True, unique = False)
    avatar = models.ImageField(upload_to = 'images/avatar')
    email = models.EmailField(max_length = 35, null = False, unique = True)
    description = models.TextField(max_length = 500)
    birthday = models.DateField(auto_now = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username