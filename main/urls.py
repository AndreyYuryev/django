from django.urls import path
from main.views import index, contact, product

urlpatterns = [
    path('', index),
    path('contact', contact),
    path('product', product)
]