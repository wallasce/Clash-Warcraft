# Generated by Django 4.2.7 on 2023-11-24 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("GameSettings", "0005_rename_winner_winner_sidewinner"),
    ]

    operations = [
        migrations.DeleteModel(name="Winner",),
    ]