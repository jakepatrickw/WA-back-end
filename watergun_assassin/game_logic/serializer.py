from .models import Game, Player
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


# class RoundsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rounds
#         fields = ['assassin', 'target', 'game', 'rounds', 'assassinated']

    