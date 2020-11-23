from django.urls import path
from . import views as image_views

urlpatterns = [
    path('create/', image_views.UploadImage.as_view(), name = 'UploadImage'),
    path('list/', image_views.ListImage.as_view(), name = 'ListImage'),
    path('update/<int:user_id>', image_views.UpdateImage.as_view(), name = 'UpdateImage'),
    path('delete/<int:user_id>', image_views.DestroyImage.as_view(), name = 'DestroyImage'),
    path('lookup/<int:user_id>', image_views.LookupImage.as_view(), name = 'LookupImage')   
    ]
