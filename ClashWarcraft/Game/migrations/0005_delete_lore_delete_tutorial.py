# Generated by Django 5.0.1 on 2024-03-06 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0004_tutorial_theme'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lore',
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
