from django.shortcuts import render
from main.models import Product, Category, Contact
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    products = []
    products.extend(product_list)
    return render(request, 'main/index.html', context={'products': products, 'title': 'Главная'})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            contact = Contact.objects.filter(name=name)
            print(contact)
            if not contact:
                Contact.objects.create(name=name, email=email)
            contacts = Contact.objects.all()
            return render(request, 'main/contact.html', context={'name': name, 'email': email, 'contacts': contacts, 'title': 'Контакты'})
    contacts = Contact.objects.all()
    return render(request, 'main/contact.html', context={'contacts': contacts, 'title': 'Контакты'})


def product(request, product_id: int):
    try:
        product = Product.objects.get(pk=product_id)
        product_info = {'product': product, 'title': 'Продукт'}
        return render(request, 'main/product.html', context=product_info)
    except ObjectDoesNotExist:
        product_info = {'product': Product.objects.get(pk=1), 'title': 'Продукт'}
        return render(request, 'main/product.html', context=product_info)