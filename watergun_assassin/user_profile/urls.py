from django.urls import path
from . import views as profile_views

urlpatterns = [
    path('list/', profile_views.UserProfileList.as_view(), name = 'UserProfileList'),
    path('create/', profile_views.UserProfileCreate.as_view(), name = 'UserProfileCreate'),
    path('update/<int:user_id>', profile_views.UpdateUserInfo.as_view(), name = 'UpdateUserInfo'),
    path('lookup/<int:user_id>', profile_views.UserProfileLookup.as_view(), name = 'UserProfileLookup'),
    path('delete/<int:user_id>', profile_views.DestroyUserInfo.as_view(), name = 'DestroyUserInfo'),
]
