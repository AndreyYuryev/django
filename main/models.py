from django.db import models
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField()

    def __str__(self):
        return f'Категория: {self.id} Наименование: {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField()
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=16)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name='автор')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')

    def __str__(self):
        return f'Продукт: {self.id} {self.name} по цене {self.price} в категории {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [('set_published', 'Опубликовать продукт'),
                       ('edit_category', 'Изменить категорию'),
                       ('edit_description', 'Изменить описание'),
                       ('edit_version', 'Изменение версии')]


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='имя')
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'Имя: {self.name} Email: {self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='номер версии')
    title = models.CharField(max_length=100, verbose_name='название')
    is_active = models.BooleanField(default=False, verbose_name='активная версия')

    def __str__(self):
        return f'{self.number} {self.title} {self.is_active}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
