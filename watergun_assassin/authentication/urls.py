from django.urls import path
from . import views as authentication_views

urlpatterns = [
    path('lookup/<int:id>', authentication_views.UserLookup.as_view(), name = 'UserLookup'),
    path('read/', authentication_views.ListAllUser.as_view(), name = 'ListAllUser'),
    path('create/', authentication_views.CreateUser.as_view(), name = 'CreateUser'),
    path('update/<int:id>', authentication_views.UpdateUser.as_view(), name = 'UpdateUser'),
    path('delete/<int:id>', authentication_views.DestroyUser.as_view(), name = 'DestroyUser')
    ]
