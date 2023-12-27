from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, label='Имя')
    email = forms.EmailField(max_length=254, label='Почта')


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    preview = forms.ImageField(label='картинка')
    category = forms.CharField(max_length=100, label='Категория')
    price = forms.DecimalField(decimal_places=2, max_digits=16, label='Цена')