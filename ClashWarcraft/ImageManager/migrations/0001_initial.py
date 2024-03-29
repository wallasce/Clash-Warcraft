# Generated by Django 5.0.1 on 2024-01-24 19:19

import ImageManager.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to=ImageManager.models.directory_path)),
            ],
        ),
    ]
