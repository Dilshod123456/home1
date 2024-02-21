from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', send_email, name='send_email'),
]
