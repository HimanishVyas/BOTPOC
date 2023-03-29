
from django.contrib import admin
from django.urls import path
from bot import views

urlpatterns = [
    path('home', views.home.as_view(), name='home')
]
