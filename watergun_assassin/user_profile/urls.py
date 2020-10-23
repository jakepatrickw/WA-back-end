from django.urls import path
from . import views as profile_views

urlpatterns = [
    path('list/', profile_views.UserProfileList.as_view(), name = 'UserProfileList'),
    path('profile/', profile_views.UserProfileCreate.as_view(), name = 'UserProfileCreate'),
    #path('updatebio/', profile_views.update_user_biography, name = 'update_biography')
]
