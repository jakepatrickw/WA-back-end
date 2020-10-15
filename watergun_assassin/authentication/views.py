import logging 
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.decorators import api_view 

@api_view(['POST'])
@csrf_exempt
def create_user(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(username, email, password)
        logging.info('user record created for ' + email)
        return JsonResponse({'status':'ok'})
    except Exception as error:
        logging.error(error)
        return JsonResponse({'status_code':400, 'status':'Bad Request'})

@api_view(['GET'])
@csrf_exempt
def read_user(request):
    try:
        username = request.GET['username']
        logging.info(username)
        user = User.objects.get(username = username)
        logging.info(user) 
        logging.info(user.email)
        return JsonResponse({'status' : 'ok', 'username' : username,
                            'email' : user.email, 'password' : user.password})
    except Exception as error:
        logging.exception(error)
        return JsonResponse({'status_code':400, 'status':'Bad Request'})

@api_view(['POST'])
@csrf_exempt
def update_username(request):
    try:
        logging.info(request.body)
        payload = json.loads(request.body)
        old_username = payload['old_username']
        new_username = payload['new_username']
        logging.info(old_username)
        logging.info(new_username)
        user = User.objects.get(username = old_username)
        user.username = new_username
        user.save()
        return JsonResponse({'status' : 'ok', 'username' : new_username})
    except Exception as error:
        logging.exception(error)
        return JsonResponse({'status_code' : 400, 'status' : 'Bad Request'})

@api_view(['DELETE'])
@csrf_exempt
def delete_user(request):
    try:
        logging.info(request.body)
        payload = json.loads(request.body)
        username = payload['username']
        logging.info(username)
        user = User.objects.get(username = username)
        user.delete()
        return JsonResponse({'status':'ok'})
    except Exception as error:
        logging.exception(error)
        return JsonResponse({'status_code':400, 'status':'Bad Request'})
