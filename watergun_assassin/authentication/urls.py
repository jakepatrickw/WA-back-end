from django.urls import path
from . import views as authentication_views

urlpatterns = [
    path('create/', authentication_views.create_user,name = 'create_user')
    ]
