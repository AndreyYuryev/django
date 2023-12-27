from django.shortcuts import render
from blog_app.models import BlogRecord
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


# Create your views here.
class BlogListView(ListView):
    model = BlogRecord
    extra_context = {'title': 'Стартовая страница блога'}
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = BlogRecord
    extra_context = {'title': 'Статья детально'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.viewed += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'text', 'preview',)
    extra_context = {'title': 'Добавление статьи', 'header': 'Форма для создания статьи', 'action': 'Добавить'}
    success_url = reverse_lazy('blog_app:index')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = BlogRecord
    fields = ('text', 'is_published')
    extra_context = {'title': 'Изменение статьи', 'header': 'Форма для изменения текста статьи', 'action': 'Изменить'}
    success_url = reverse_lazy('blog_app:index')

    def get_success_url(self):
        return reverse('blog_app:blog', args=[self.kwargs.get('pk')])
