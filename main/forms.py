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

    def clean_is_active(self):
        set_active = self.cleaned_data.get('is_active')
        # если было True оставляем
        # если изменение и уже есть активная версия - ошибка
        if set_active:
            active_count = 0
            formset_cleaned_data = super().clean()
            current_version = formset_cleaned_data['number']
            saved_active_version = Version.objects.filter(product=formset_cleaned_data['product'], is_active=True)
            for version in saved_active_version.values():
                if current_version != version.get('number'):
                    active_count += 1
            if active_count > 0:
                print('error')
                raise ValidationError(('Уже существует активная версия %(value)s'), code='error3',
                                      params={'value': current_version})
        return set_active
