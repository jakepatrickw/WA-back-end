from .models import Game, Player, Round
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game_title']


class GameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game_title']
    game_title = serializers.CharField(required=False)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player', 'game', 'is_admin']

    
class PlayerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player', 'game', 'is_admin']
    is_admin = serializers.BooleanField(required=False)


class RoundSerializer(serializers.ModelSerializer):
   class Meta:
        model = Round
        fields = ['round_number', 'assassinated', 'game']

    