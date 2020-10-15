from django.shortcuts import render
from django.http import JsonResponse
import logging
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import UserImage
from rest_framework.decorators import api_view

@api_view(['POST'])
@csrf_exempt
def user_image(request):
    try:
        user_id = request.POST['user_id']
        user = User.objects.get(id = user_id)
        profile_pic = UserImage(picture = request.FILES['picture'],
                                user_id = user)
        profile_pic.save()
        return JsonResponse({'status':'ok'})
    except Exception as error:
        logging.error(error)
        return JsonResponse({'status_code' : 400, 'status' : 'bad request'})
