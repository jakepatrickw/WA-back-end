from django.shortcuts import render
from django.http import JsonResponse
import logging
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .models import UserImage
from .serializer import ImageSerializer, ImageUpdateSerializer


class UploadImage(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = ImageSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ListImage(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = ImageSerializer
    queryset = UserImage.objects.all()

class LookupImage(RetrieveAPIView):

    permission_classes = [AllowAny]
    serializer_class = ImageSerializer
    queryset = UserImage.objects.all()
    lookup_field = 'user_id'

class UpdateImage(UpdateAPIView):

    permission_classes = [AllowAny]
    serializer_class = ImageUpdateSerializer
    queryset = UserImage.objects.all()
    lookup_field = 'user_id'


class DestroyImage(DestroyAPIView):

    permission_classes = [AllowAny]
    serializer_class = ImageSerializer
    queryset = UserImage.objects.all()
    lookup_field = 'user_id'
