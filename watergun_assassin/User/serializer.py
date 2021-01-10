from .models import UserImage, UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers


class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'email']

class AuthenticationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'email']
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ['picture', 'user_id']

class ImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ['picture', 'user_id']
    picture = serializers.FileField(required=False)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_id', 'biography', 'catch_phrase']

class UserUpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['biography', 'catch_phrase']
    biography = serializers.CharField(required=False)
    catch_phrase = serializers.CharField(required=False)