# Generated by Django 4.2.7 on 2023-11-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Skill", "0001_initial"),
        ("Character", "0005_remove_character_skill_character_skill"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="skill",
            field=models.ManyToManyField(to="Skill.skill"),
        ),
    ]
