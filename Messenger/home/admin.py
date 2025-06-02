from django.contrib import admin
from .models import User_Post, Tag, Image

# Register your models here.

admin.site.register(Tag)
admin.site.register(User_Post)
admin.site.register(Image)