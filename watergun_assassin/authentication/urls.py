from django.urls import path
from . import views as authentication_views

urlpatterns = [
    #path('create/', authentication_views.create_user,name = 'create_user'),
    path('lookup', authentication_views.UserLookup.as_view(), name = 'UserLookup'),
    #path('lookup/', authentication_views.get_user_by_id, name = 'get_user_by_id'),
    path('read/', authentication_views.ReadClass.as_view(), name = 'ReadClass'),
    path('create/', authentication_views.CreateClass.as_view(), name = 'CreateClass')
    #path('update/', authentication_views.update_username, name = 'update_username'),
    #path('delete/', authentication_views.delete_user, name = 'delete_user')
    ]
