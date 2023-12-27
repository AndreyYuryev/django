# Generated by Django 5.0 on 2023-12-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_rename_published_blogrecord_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecord',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
        migrations.AlterField(
            model_name='blogrecord',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='содержимое'),
        ),
        migrations.AlterField(
            model_name='blogrecord',
            name='title',
            field=models.CharField(max_length=150, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='blogrecord',
            name='viewed',
            field=models.IntegerField(default=0, verbose_name='просмотры'),
        ),
    ]
