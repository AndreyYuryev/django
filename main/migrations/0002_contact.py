# Generated by Django 5.0 on 2023-12-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='имя')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
    ]
