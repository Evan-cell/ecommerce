# Generated by Django 3.2.7 on 2022-03-02 08:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='image', max_length=255, verbose_name='image'),
        ),
    ]
