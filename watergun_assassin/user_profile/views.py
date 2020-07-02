from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from .models import UserProfile

@csrf_exempt
def user_profile(request):
    try:
        personal_info = UserProfile(biography = request.POST['biography'],
                                    catch_phrase = request.POST['catch_phrase'],
                                    user_id = request.POST['user_id']
                                    )
        personal_info.save()
        return JsonResponse({'status':'ok'})
    except Exception as error:
        logging.error(error)
