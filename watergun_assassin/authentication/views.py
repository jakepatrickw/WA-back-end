from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_user(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        print(username,password,email)
        User.objects.create_user(username,email,password)
        return JsonResponse({'status':'ok'})
    except:
        return JsonResponse({'status_code':400,'status':'Bad Request'})
        
        
"""@csrf_exempt
    def create_user(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    required_info = User.objects.create_user(username,email,password)
    if request == required_info:
        return JsonResponse({'code':200,'status':'ok'})
    else:
        return JsonResponse({'code':400,'status':'bad request'})"""

    
