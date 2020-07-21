import logging 
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

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