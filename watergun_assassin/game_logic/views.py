from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, \
                                    ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from .serializer import GameSerializer, GameUpdateSerializer, \
                        PlayerSerializer, PlayerUpdateSerializer #RoundSerializer
from .models import Game, Player #Round


class CreateGame(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = GameSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReadGame(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['id']
    search_fields = ['admin']

class ListGame(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class DestroyGame(DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    lookup_field = ['id']


class UpdateGame(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = GameUpdateSerializer
    queryset = Game.objects.all()
    lookup_field = ['id']


class CreatePlayer(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlayerSerializer

    def update(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReadPlayer(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['player']
    search_fields = ['game']


class ListPlayer(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class DestroyPlayer(DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    lookup_field = ['player']


class UpdatePlayer(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PlayerUpdateSerializer
    queryset = Player.objects.all()
    lookup_field = ['player']


# class ReadRound(ListAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = RoundSerializer
#     queryset = Round.objects.all()


# class CreateRound(CreateAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = RoundSerializer

#     def update(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
