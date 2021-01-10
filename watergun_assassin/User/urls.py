from django.urls import path
from . import views


urlpatterns = [
    path('user/lookup/<int:id>', views.UserLookup.as_view(), name = 'UserLookup'),
    path('user/read/', views.ReadUser.as_view(), name = 'ReadUser'),
    path('user/create/', views.CreateUser.as_view(), name = 'CreateUser'),
    path('user/update/<int:id>', views.UpdateUser.as_view(), name = 'UpdateUser'),
    path('user/delete/<int:id>', views.DestroyUser.as_view(), name = 'DestroyUser'),
    path('image/create/', views.UploadImage.as_view(), name = 'UploadImage'),
    path('image/list/', views.ListImage.as_view(), name = 'ListImage'),
    path('image/update/<int:user_id>', views.UpdateImage.as_view(), name = 'UpdateImage'),
    path('image/delete/<int:user_id>', views.DestroyImage.as_view(), name = 'DestroyImage'),
    path('image/lookup/<int:user_id>', views.LookupImage.as_view(), name = 'LookupImage'),
    path('profile/list/', views.UserProfileList.as_view(), name = 'UserProfileList'),
    path('profile/create/', views.UserProfileCreate.as_view(), name = 'UserProfileCreate'),
    path('profile/update/<int:user_id>', views.UpdateUserInfo.as_view(), name = 'UpdateUserInfo'),
    path('profile/lookup/<int:user_id>', views.UserProfileLookup.as_view(), name = 'UserProfileLookup'),
    path('profile/delete/<int:user_id>', views.DestroyUserInfo.as_view(), name = 'DestroyUserInfo'), 
    ]
