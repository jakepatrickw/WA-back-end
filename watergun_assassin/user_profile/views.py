import json
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile

@csrf_exempt
def user_profile(request):
    try:
        personal_info = UserProfile(
                                    biography = request.POST['biography'],
                                    catch_phrase = request.POST['catch_phrase'],
                                    user_id = request.POST['user_id']
                                    )
        personal_info.save()
        return JsonResponse({'status':'ok'})
    except Exception as error:
        logging.error(error)

@csrf_exempt
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
