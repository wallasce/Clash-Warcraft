# Generated by Django 5.0.1 on 2024-01-27 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageManager', '0001_initial'),
        ('WebsiteContent', '0012_delete_sectionpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('subtitle', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=155)),
                ('page', models.CharField(max_length=55)),
                ('style', models.CharField(blank=True, max_length=55, null=True)),
                ('backgroundSectionPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ImageManager.uploadedimage')),
                ('imageSectionPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ImageUploaded2ImageSectionPage', to='ImageManager.uploadedimage')),
            ],
        ),
    ]