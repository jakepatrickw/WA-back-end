from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from .serializer import GameSerializer, GameUpdateSerializer, PlayerSerializer, PlayerUpdateSerializer
from .models import Game, Player


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

