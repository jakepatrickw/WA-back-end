from django.db import models
from django.contrib.auth.models import User



class Game(models.Model):
    game_title = models.CharField(max_length=30)


class Player(models.Model):
    player = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    game = models.OneToOneField(Game, null=False, on_delete=models.CASCADE)
    is_admin = models.BooleanField()

# class Round(models.Model):
#     assassin = models.OneToOneField(Player, null=True, on_delete=models.CASCADE, related_name='player')
#     target = models.OneToOneField(Player, null=True, on_delete=models.CASCADE, related_name='target')
#     game = models.OneToOneField(Game, on_delete=models.CASCADE)
#     rounds = 1
#     assassinated = models.BooleanField(null=False, default=False)

