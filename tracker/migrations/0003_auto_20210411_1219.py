# Generated by Django 3.0 on 2021-04-11 09:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0002_neighbourhood'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NeighbourHood',
            new_name='Neighborhood',
        ),
    ]
