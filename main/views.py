from main.models import Product, Contact, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from main.forms import ContactForm, ProductForm, VersionForm
from django.forms import inlineformset_factory, ValidationError


# Create your views here.
class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Стартовая страница проекта'}
    paginate_by = 5

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'name')
        # validate ordering here
        return ordering


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Продукт'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_obj = Version.objects.filter(product=self.object, is_active=True)
        if version_obj:
            context_data['version'] = version_obj
        return context_data


class ProductCreateView(CreateView):
    model = Product
    # fields = ('name', 'description', 'category', 'preview', 'price',)
    extra_context = {'title': 'Добавление продукта', 'header': 'Форма для создания продукта', 'button': 'Добавить'}
    success_url = reverse_lazy('main:index')
    form_class = ProductForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    # fields = ('description', 'price',)
    extra_context = {'title': 'Изменение продукта', 'header': 'Форма для изменения продукта', 'button': 'Изменить'}
    success_url = reverse_lazy('main:index')
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ContactListView(ListView):
    model = Contact
    extra_context = {'title': 'Контакты'}


class ContactCreateView(CreateView):
    model = Contact
    # fields = ('name', 'email',)
    extra_context = {'title': 'Добавление контакта', 'header': 'Добавление нового контакта!'}
    success_url = reverse_lazy('main:contact')
    form_class = ContactForm
