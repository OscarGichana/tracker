# Generated by Django 3.0 on 2021-04-12 19:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20210412_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='pic',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='pic'),
        ),
    ]