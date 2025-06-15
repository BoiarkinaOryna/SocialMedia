from django.db import models
from home.models import Image, Tag
# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(default = '2006-10-25 14:30:59')
    preview_image = models.ImageField(upload_to = 'images/album_previews', null = True, blank = True)
    images = models.ManyToManyField(Image)
    topic = models.ForeignKey(Tag, on_delete = models.CASCADE, null = True)
    shown = models.BooleanField(default = True)

