from django.urls import path
from . import views as image_views

urlpatterns = [
    path('image/', image_views.UploadImage.as_view(), name = 'user_image')    
    ]
