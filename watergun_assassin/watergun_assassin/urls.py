from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from user_profile import urls
from user_image import urls
from authentication import urls

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include('authentication.urls')),
    path('api/user/', include('user_profile.urls')),
    path('api/user/', include('user_image.urls'))
    ]
