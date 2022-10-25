from django.contrib import admin
from django.urls import path
from .views import lobby, room

urlpatterns = [
    path('', lobby, name='lobby'),
    path('<str:room_name>/', room, name='room'),
]
