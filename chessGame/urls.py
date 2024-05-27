from django.contrib import admin
from django.urls import path, include
from game import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.chooseMode, name='chooseMode'),
    path('play', views.playLocal, name='playLocal'),
    path('ai', views.playAI, name='playAI'),
    path('board', views.board),
    path('reset', views.resetBoard, name='resetBoard'),
    path('home/', views.chooseMode, name='home'),
    path('home/', views.home, name='home'),
    path('instructions/', views.instructions, name='instructions'),
    path('select_color/', views.selectColor, name='selectColor'),
    path('quit_confirmation/', views.quit_confirmation, name='quit-confirmation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
