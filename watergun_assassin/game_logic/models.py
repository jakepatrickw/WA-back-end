from django.db import models
from django.contrib.auth.models import User

class Players(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    is_admin = models.BooleanField()

class Game(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)




