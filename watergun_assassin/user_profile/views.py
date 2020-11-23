from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializer import UserProfileSerializer, UserUpdateProfileSerializer
from .models import UserProfile


class UserProfileList(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    #filter_backends = [DjangoFilterBackend, SearchFilter]
    #filter_fields = ['user_id']
    #search_fields = ['biography', 'catch_phrase']


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
    


    