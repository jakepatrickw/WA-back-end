from django.shortcuts import render
from django.http import JsonResponse
import logging
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import UserImage
from .serializer import ImageSerializer


class UploadImage(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# @api_view(['POST'])
# @permission_classes(['AllowAny'])
# def user_image(request):
#     try:
#         user_id = request.POST['user_id']
#         user = User.objects.get(id = user_id)
#         profile_pic = UserImage(picture = request.FILES['picture'],
#                                 user_id = user)
#         profile_pic.save()
#         return JsonResponse({'status':'ok'})
#     except Exception as error:
#         logging.error(error)
#         return JsonResponse({'status_code' : 400, 'status' : 'bad request'})
