from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    game_title = models.CharField(max_length=30)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)

class Rounds(models.Model):
    