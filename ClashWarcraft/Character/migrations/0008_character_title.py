# Generated by Django 5.0.1 on 2024-01-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Character', '0007_rename_attributes_attribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='title',
            field=models.CharField(blank=True, default='', max_length=35),
        ),
    ]