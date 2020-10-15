import json
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes

from .models import UserProfile

class user_profile_list(generics.ListAPIView):
    queryset = UserProfile.objects.all()

@api_view(['POST'])
@permission_classes(['AllowAny'])
def user_profile(request):
    try:
        personal_info = UserProfile(
                    biography = User.objects.get('biography'),
                    catch_phrase = User.objects.get('catch_phrase'),
                    user_id = User.objects.get('user_id')
                    )
        personal_info.save()
        return JsonResponse({'status':'ok'})
    except Exception as error:
        logging.error(error)

@api_view(['POST'])
@permission_classes(['AllowAny'])
def update_user_biography(request):
    try:
        logging.info(request.body)
        payload = json.loads(request.body)
        username = payload['username']
        new_bio = payload['new_bio']
        user = User.objects.get(username = username)
        user_profile = UserProfile.objects.get(user_id = user)
        user_profile.biography = new_bio
        user_profile.save()
        return JsonResponse({'status' : 'ok'})
    except Exception as error:
        logging.exception(error)
        return JsonResponse({'status_code' : 400, 'status' : 'Bad request'})
