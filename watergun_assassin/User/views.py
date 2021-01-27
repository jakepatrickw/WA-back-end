import logging 
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, \
                                    DestroyAPIView, UpdateAPIView, RetrieveDestroyAPIView, \
                                    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from .serializer import AuthenticationSerializer, AuthenticationUpdateSerializer, \
                        ImageSerializer, ImageUpdateSerializer, UserProfileSerializer, \
                        UserUpdateProfileSerializer
from .models import UserImage, UserProfile


class ReadUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthenticationUpdateSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


class ListCreateUser(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['id']
    search_fields = ['username', 'email']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CreateUser(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListUser(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['id']
    search_fields = ['username', 'email']


class UpdateUser(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthenticationUpdateSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


class ReadDestroyUser(RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


class UploadImage(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ImageSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListImage(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ImageSerializer
    queryset = UserImage.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['user_id']
    

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


class UserProfileList(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['user_id']
    search_fields = ['biography', 'catch_phrase']


class UserProfileCreate(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileLookup(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'user_id'
    

class UpdateUserInfo(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserUpdateProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'user_id'


class DestroyUserInfo(DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'user_id'
