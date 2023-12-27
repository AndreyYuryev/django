from django.shortcuts import render
from blog_app.models import BlogRecord
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy


# Create your views here.
class BlogListView(ListView):
    model = BlogRecord
    extra_context = {'title': 'Стартовая страница блога'}
    paginate_by = 5


class BlogDetailView(DetailView):
    model = BlogRecord
    extra_context = {'title': 'Статья детально'}


class BlogCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'text', 'preview',)
    extra_context = {'title': 'Добавление статьи', 'header': 'Форма для создания статьи', 'action': 'Добавить'}
    success_url = reverse_lazy('blog_app:index')


class BlogUpdateView(UpdateView):
    model = BlogRecord
    fields = ('text',)
    extra_context = {'title': 'Изменение статьи', 'header': 'Форма для изменения текста статьи', 'action': 'Изменить'}
    success_url = reverse_lazy('blog_app:index')
