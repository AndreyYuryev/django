from django.urls import path
from main.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ContactListView, ContactCreateView
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),

    path('contact/', ContactListView.as_view(), name='contact'),
    path('contact_create/', ContactCreateView.as_view(), name='contact_create'),
]