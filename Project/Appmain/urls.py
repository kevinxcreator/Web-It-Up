from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('segregate/', views.segregate, name="segregate"),
    path('bin/', views.bin, name="bin")
]