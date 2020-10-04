from django.urls import path
from . import views as image_views

urlpatterns = [
    path('image/', image_views.user_image, name = 'user_image')    
    ]
