from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    game_title = models.CharField(max_length=30)


class Player(models.Model):
    player = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    game = models.OneToOneField(Game, null=False, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)


# class Round(models.Model):
#     game = models.OneToOneField(Game, on_delete=models.CASCADE)
#     round_number = models.IntegerField(default=0)
#     assassinated = models.OneToOneField(Player, on_delete=models.CASCADE, null=True)


# class RoundPairing(models.Model):
#     round_number = models.OneToOneField(Round, on_delete=models.CASCADE, null=False)
#     assassin = models.OneToOneField(Player, null=True, on_delete=models.CASCADE, related_name='player')
#     target = models.OneToOneField(Player, null=True, on_delete=models.CASCADE, related_name='target')
