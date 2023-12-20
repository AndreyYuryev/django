from django.shortcuts import render
from main.models import Product, Category

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    products = []
    for indx in range(product_list.count()-1,product_list.count() - 5,-1):
        products.append(product_list[indx])
    return render(request, 'main/index.html', context={'products': products})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            return render(request, 'main/contact.html', context={'name': name, 'email': email})
    return render(request, 'main/contact.html')
