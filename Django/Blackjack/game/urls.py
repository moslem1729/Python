from django.urls import path

from game import views

urlpatterns = [
    path('welcome', views.wellcome, name='home'),
    path('game', views.game, name='game')
]
