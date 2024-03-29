from django.urls import path
from . import views

urlpatterns = [
    path('game/lookup/<int:id>/', views.ReadGame.as_view(), name='ReadGame'),
    path('game/list/', views.ListGame.as_view(), name='ListGame'),
    path('game/create/', views.CreateGame.as_view(), name='CreateGame'),
    path('game/destroy/', views.DestroyGame.as_view(), name='DestroyGame'),
    path('game/update/', views.UpdateGame.as_view(), name='UpdateGame'),
    path('player/lookup/<int:player>', views.ReadPlayer.as_view(), name='ReadPlayer'),
    path('player/list/', views.ListPlayer.as_view(), name='ListPlayer'),
    path('player/create/', views.CreatePlayer.as_view(), name='CreatePlayer'),
    path('player/destroy/', views.DestroyPlayer.as_view(), name='DestroyPlayer'),
    path('player/update/', views.UpdatePlayer.as_view(), name='UpdatePlayer'),
    #path('round/read/', views.ReadRound.as_view(), name='ReadRound'),
    #path('round/create/', views.CreateRound.as_view(), name='CreateRound')
]