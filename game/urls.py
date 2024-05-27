from django.urls import path
from . import views

urlpatterns = [
    path('', views.chooseMode, name='chooseMode'),
    path('play', views.playLocal, name='playLocal'),
    path('ai', views.playAI, name='playAI'),
    path('board', views.board),
    path('reset', views.resetBoard, name='resetBoard'),
    path('select_color/', views.selectColor, name='selectColor'),
    path('instructions/', views.instructions, name='instructions'),
    path('quit-confirmation/', views.quit_confirmation, name='quit-confirmation'),
    path('quit-game/', views.quit_game, name='quit-game'), 
    path('home/', views.home, name='home'),
]
