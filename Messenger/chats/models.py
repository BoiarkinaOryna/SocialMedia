from django.db import models
from registration.models import Profile

# Create your models here.
class Friends(models.Model):
    user1 = models.ForeignKey(to = Profile, on_delete = models.CASCADE, related_name='friends_as_user1')
    user2 = models.ForeignKey(to = Profile, on_delete = models.CASCADE, related_name='friends_as_user2')
