from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializer import UserProfileSerializer, UserUpdateProfileSerializer
from .models import UserProfile


class UserProfileList(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserProfileCreate(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileLookup(RetrieveAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'id'

        
class UpdateUserInfo(UpdateAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserUpdateProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'id'

class DestroyUserInfo(DestroyAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'id'
    