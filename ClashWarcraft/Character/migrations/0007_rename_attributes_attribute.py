# Generated by Django 4.2.7 on 2023-11-16 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Character", "0006_alter_character_skill"),
    ]

    operations = [
        migrations.RenameModel(old_name="Attributes", new_name="Attribute",),
    ]