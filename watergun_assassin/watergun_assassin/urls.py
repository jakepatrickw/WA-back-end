from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from User import urls

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('User.urls'))
    ]
