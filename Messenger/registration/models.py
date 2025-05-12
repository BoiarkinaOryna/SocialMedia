from django.db import models

# Create your models here.
class Profile(models.Model):
    id = models.IntegerField(primary_key = True, null = False)
    user_name = models.CharField(max_length = 25, null = False)
    name = models.CharField(max_length = 25, null = False)
    surname = models.CharField(max_length= 25)
    avatar = models.ImageField(upload_to = 'images/avatar')
    email = models.EmailField(max_length = 35, null = False, unique = True)
    description = models.TextField(max_length = 500)
    birthday = models.DateField(auto_now = True)
    password = models.CharField(null = False, max_length = 50)