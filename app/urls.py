from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name='home'), path('/', views.home, name='home'),
  path('test/', views.test, name='home'), path('test', views.test, name='home'),
  path('add/', views.add, name='home'), path('add', views.add, name='home')
]