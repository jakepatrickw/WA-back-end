from .models import UserImage
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ['picture', 'user_id']

class ImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ['picture', 'user_id']
    picture = serializers.FileField(required=False)
