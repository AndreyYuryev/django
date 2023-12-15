from django.urls import path
from main.views import index, contact

urlpatterns = [
    path('', index),
    path('contact', contact)
]