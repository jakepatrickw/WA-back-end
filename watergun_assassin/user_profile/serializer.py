from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User

class user_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['biography', 'catch_phrase', 'user_id']
