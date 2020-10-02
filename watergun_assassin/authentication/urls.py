from django.urls import path
from . import views as authentication_views

urlpatterns = [
    path('create/', authentication_views.create_user,name = 'create_user'),
    path('read/', authentication_views.read_user, name = 'read_user'),
    path('update/', authentication_views.update_user_name, name = 'update_username'),
    path('delete/', authentication_views.delete_user, name = 'delete_user')
    ]
