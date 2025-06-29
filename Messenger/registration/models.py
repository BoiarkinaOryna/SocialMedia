from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    date_of_birth = models.DateField(null=True)
    signature = models.ImageField(upload_to = 'images/signatures', blank = True, null = True)

    def __str__(self):
        return self.user.username