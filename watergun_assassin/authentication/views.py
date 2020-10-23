import logging 
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .serializer import authentication_serializer


class CreateClass(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = authentication_serializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReadClass(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = authentication_serializer
    queryset = User.objects.all()


class UserLookup(RetrieveAPIView):

    permission_classes = [AllowAny]
    serializer_class = authentication_serializer
    lookup_field = ['id']
    
 


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_by_id(request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        logging.info(user_id)
        user = User.objects.get(id = user_id)
        serializer = authentication_serializer(user)
        return JsonResponse(serializer.data, safe=False)

# @api_view(['POST'])
# @permission_classes(['AllowAny'])
# def update_username(request):
#     try:
#         logging.info(request.body)
#         payload = json.loads(request.body)
#         old_username = payload['old_username']
#         new_username = payload['new_username']
#         user = User.objects.get(username = old_username)
#         user.username = new_username
#         user.save()
#         return JsonResponse({'status' : 'ok', 'username' : new_username})
#     except Exception as error:
#         logging.exception(error)
#         return JsonResponse({'status_code' : 400, 'status' : 'Bad Request'})

# @api_view(['DELETE'])
# @permission_classes(['AllowAny'])
# def delete_user(request):
#     try:
#         logging.info(request.body)
#         payload = json.loads(request.body)
#         username = payload['username']
#         logging.info(username)
#         user = User.objects.get(username = username)
#         user.delete()
#         return JsonResponse({'status':'ok'})
#     except Exception as error:
#         logging.exception(error)
#         return JsonResponse({'status_code':400, 'status':'Bad Request'})
