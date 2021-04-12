# Generated by Django 3.0 on 2021-04-12 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='neighborhood',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='neighborhood_posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Posts'),
        ),
    ]
