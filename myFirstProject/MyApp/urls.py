from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),  # '' means root URL
]
