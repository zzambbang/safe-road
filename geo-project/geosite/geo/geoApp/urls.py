from django.urls import path 
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    path('', views.home, name='home')
]


