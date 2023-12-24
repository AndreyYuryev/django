from django.shortcuts import render
from main.models import Product, Category, Contact


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    products = []
    for indx in range(product_list.count() - 1, product_list.count() - 5, -1):
        products.append(product_list[indx])
    return render(request, 'main/index.html', context={'products': products})


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
            return render(request, 'main/contact.html', context={'name': name, 'email': email, 'contacts': contacts})
    contacts = Contact.objects.all()
    return render(request, 'main/contact.html', context={'contacts': contacts})


def product(request):
    product_id = 1
    product = Product.objects.get(id=product_id)
    product_info = {'product': product}
    return render(request, 'main/product.html', context=product_info)
