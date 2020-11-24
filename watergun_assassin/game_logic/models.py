from django.db import models
from django.contrib.auth.models import User

class Players(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField()

class Game(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)




