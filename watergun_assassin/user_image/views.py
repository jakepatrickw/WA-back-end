from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
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
    #filter_backends = [DjangoFilterBackend, SearchFilter]
    #filter_fields = ['user_id']
    

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
