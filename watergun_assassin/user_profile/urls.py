from django.urls import path
from . import views as profile_views

urlpatterns = [
    path('profile/', profile_views.user_profile, name='user_profile')
    ]
