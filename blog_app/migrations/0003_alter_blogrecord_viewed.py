# Generated by Django 5.0 on 2023-12-27 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_blogrecord_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecord',
            name='viewed',
            field=models.IntegerField(auto_created=0, null=True),
        ),
    ]
