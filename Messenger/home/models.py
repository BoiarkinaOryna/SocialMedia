from django.db import models
from registration.models import Profile

# Create your models here.

class Image(models.Model):
    filename = models.CharField(max_length = 150)
    file = models.ImageField(upload_to = "images/post")
    uploaded_at = models.DateTimeField(auto_now = True)

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    def __str__(self):
        return self.tag_name 

class User_Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    theme = models.CharField(max_length=200, null = True, blank = True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    link = models.URLField(null = True, blank = True)
    images = models.ManyToManyField(Image, max_length = 9, blank = True)
    views = models.BigIntegerField(null = True, default = 0)
    likes = models.BigIntegerField(null = True, default = 0)

    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     print("save is in progress")
    #     super().save(*args, **kwargs)