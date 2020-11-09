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
    email = serializers.CharField(required=False)
    