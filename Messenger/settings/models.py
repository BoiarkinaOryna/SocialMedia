from django.db import models
from home.models import Image
# Create your models here.

class Album(models.Model):
    image = models.ManyToManyField(Image, null = True)
    name = models.CharField(max_length = 375)
    theme = models.CharField(max_length = 375)
    year = models.PositiveIntegerField()