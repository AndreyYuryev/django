from django.db import models


# Create your models here.
class BlogRecord(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    text = models.TextField(null=True,blank=True, verbose_name='содержимое')
    preview = models.ImageField(upload_to='blogs/', verbose_name='изображение', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=100, null=True, blank=True, verbose_name='slug')

    def __str__(self):
        return f'Статья: {self.title} '

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
