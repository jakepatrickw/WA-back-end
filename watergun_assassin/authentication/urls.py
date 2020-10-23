from django.urls import path
from . import views as authentication_views

urlpatterns = [
    path('lookup', authentication_views.UserLookup.as_view(), name = 'UserLookup'),
    path('read/', authentication_views.ReadClass.as_view(), name = 'ReadClass'),
    path('create/', authentication_views.CreateClass.as_view(), name = 'CreateClass'),
    #path('update/', authentication_views.update_username, name = 'update_username'),
    path('delete/', authentication_views.DestroyUser.as_view(), name = 'DestroyUser')
    ]
