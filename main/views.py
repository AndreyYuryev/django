from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            return render(request, 'main/contact.html', context={'name': name, 'email': email})
    return render(request, 'main/contact.html')
