
from django.contrib import admin
from django.urls import path
from bot import views

urlpatterns = [
    path('send', views.SendMessage.as_view(), name='home')
]
