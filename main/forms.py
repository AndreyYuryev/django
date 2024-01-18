from django.forms import ModelForm, ValidationError, BaseModelFormSet
from main.models import Contact, Product, Version

RESCTRICTED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]


class ContactForm(ModelForm):
    # name = forms.CharField(max_length=20, label='Имя')
    # email = forms.EmailField(max_length=254, label='Почта')
    class Meta:
        model = Contact
        fields = ('name', 'email',)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'price',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in cleaned_data.split():
            if word in RESCTRICTED_WORDS:
                raise ValidationError(('Запрещенное слово %(value)s в названии продукта'), code='error1',
                                      params={'value': word})
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in cleaned_data.split():
            if word in RESCTRICTED_WORDS:
                raise ValidationError(('Запрещенное слово %(value)s в описании продукта'), code='error2',
                                      params={'value': word})
        return cleaned_data

class VersionForm(ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
    #     is_act = cleaned_data.get("is_active")
    #     print('is_active', is_act)
    #     # for form in self.forms:
    #     #     cleaned_data = form.cleaned_data
    #     #     print(cleaned_data)
    #     # # active_list = [form.cleaned_data['is_active'] for form in self.forms if 'is_active' in form.cleaned_data]
    #     # # if active_list.count(True) > 1:
    #     # #     raise ValidationError(('Уже существует активная версия'), code='error3')
