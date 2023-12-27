from django.urls import path
from blog_app.apps import BlogAppConfig
from blog_app.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView


app_name = BlogAppConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog'),
    path('blog_create/',  BlogCreateView.as_view(), name='create'),
    path('blog_update/<int:pk>',  BlogUpdateView.as_view(), name='update'),
]