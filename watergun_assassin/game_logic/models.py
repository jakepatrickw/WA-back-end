from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    game_title = models.CharField(max_length=30)


class Player(models.Model):
    player = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, null=False, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)


class Round(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    round_number = models.IntegerField(default=0)
    assassinated = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)


class RoundPairing(models.Model):
    round_number = models.ForeignKey(Round, on_delete=models.CASCADE, null=False)
    assassin = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)
    target = models.ForeignKey(Player, null=True, on_delete=models.CASCADE, related_name='target')
