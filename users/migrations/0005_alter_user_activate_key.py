# Generated by Django 5.0 on 2024-01-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activate_key',
            field=models.IntegerField(blank=True, max_length=10, null=True, verbose_name='ключ активации'),
        ),
    ]
