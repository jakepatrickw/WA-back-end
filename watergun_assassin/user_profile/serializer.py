from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User

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



