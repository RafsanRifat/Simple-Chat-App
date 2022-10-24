from django.contrib import admin
from django.urls import path
from .views import lobby

urlpatterns = [
    path('', lobby, name='lobby')
]
