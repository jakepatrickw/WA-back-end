import logging 
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from .serializer import AuthenticationSerializer, AuthenticationUpdateSerializer


class CreateUser(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReadUser(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = AuthenticationSerializer
    queryset = User.objects.all()
    #filter_backends = [DjangoFilterBackend, SearchFilter]
    #filter_fields = ['id']
    #search_fields = ['username', 'email']


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

