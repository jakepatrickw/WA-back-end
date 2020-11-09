from django.urls import path
from . import views as image_views

urlpatterns = [
    path('image/', image_views.UploadImage.as_view(), name = 'UploadImage'),
    path('imagelist/', image_views.ListImage.as_view(), name = 'ListImage'),
    path('imageupdate/<int:user_id>', image_views.UpdateImage.as_view(), name = 'UpdateImage'),
    path('deleteimage/<int:user_id>', image_views.DestroyImage.as_view(), name = 'DestroyImage'),
    path('imagelookup/<int:user_id>', image_views.LookupImage.as_view(), name = 'LookupImage')   
    ]
