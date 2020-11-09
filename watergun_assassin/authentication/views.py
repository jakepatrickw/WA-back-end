import logging 
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from .serializer import AuthenticationSerializer, AuthenticationUpdateSerializer


class CreateUser(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAllUser(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer
    queryset = User.objects.all()


class UserLookup(RetrieveAPIView):

    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

class DestroyUser(DestroyAPIView):

    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

class UpdateUser(UpdateAPIView):
    
    permission_classes = [AllowAny]
    serializer_class = AuthenticationUpdateSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
