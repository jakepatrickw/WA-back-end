from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    biography = models.CharField(max_length=200)
    catch_phrase = models.CharField(max_length=30)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)


