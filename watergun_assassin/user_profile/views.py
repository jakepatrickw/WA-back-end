import json
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from .serializer import user_profile_serializer
from .models import UserProfile

class UserProfileList(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = user_profile_serializer
    queryset = UserProfile.objects.all()

class UserProfileCreate(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = user_profile_serializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserProfileLookup(RetrieveAPIView):

    permission_classes = [AllowAny]
    serializer_class = user_profile_serializer
    lookup_field = ['user_id']
        

class UpdateBio(UpdateAPIView):

    permission_classes = [AllowAny]
    serializer_class = user_profile_serializer

    #def put(self, request, *args, **kwargs):




# @api_view(['POST'])
# @permission_classes(['AllowAny'])
# def update_user_biography(request):
#     try:
#         logging.info(request.body)
#         payload = json.loads(request.body)
#         username = payload['username']
#         new_bio = payload['new_bio']
#         user = User.objects.get(username = username)
#         user_profile = UserProfile.objects.get(user_id = user)
#         user_profile.biography = new_bio
#         user_profile.save()
#         return JsonResponse({'status' : 'ok'})
#     except Exception as error:
#         logging.exception(error)
#         return JsonResponse({'status_code' : 400, 'status' : 'Bad request'})
