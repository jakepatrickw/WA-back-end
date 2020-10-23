from .models import UserImage
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    model = UserImage
    fields = ['picture', 'user_id']
