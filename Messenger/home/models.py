from django.db import models
from registration.models import Profile

# Create your models here.

class Image(models.Model):
    path = models.ImageField(upload_to = "post_images")

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    def __str__(self):
        return self.tag_name

class User_Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    theme = models.CharField(max_length=200, null = True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, null = True)
    link = models.URLField(null = True)
    images = models.ForeignKey(to = Image, on_delete = models.CASCADE, max_length = 9, null = True)
    views = models.BigIntegerField(null = True, default = 0)
    likes = models.BigIntegerField(null = True, default = 0)

    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.title