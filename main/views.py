from main.models import Product, Contact
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy


# Create your views here.
class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Стартовая страница проекта'}
    paginate_by = 5

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'created_at')
        # validate ordering here
        return ordering


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Продукт'}


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'preview', 'price',)
    extra_context = {'title': 'Добавление продукта', 'header': 'Форма для создания продукта'}
    success_url = reverse_lazy('main:index')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('description', 'price',)
    extra_context = {'title': 'Изменение продукта', 'header': 'Форма для изменения продукта'}
    success_url = reverse_lazy('main:index')


class ContactListView(ListView):
    model = Contact
    extra_context = {'title': 'Контакты'}


class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'email',)
    extra_context = {'title': 'Добавление контакта', 'header': 'Добавление нового контакта!'}
    success_url = reverse_lazy('main:contact')
