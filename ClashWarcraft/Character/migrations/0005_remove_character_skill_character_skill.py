# Generated by Django 4.2.7 on 2023-11-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Skill", "0001_initial"),
        ("Character", "0004_character_skill"),
    ]

    operations = [
        migrations.RemoveField(model_name="character", name="skill",),
        migrations.AddField(
            model_name="character",
            name="skill",
            field=models.ManyToManyField(blank=True, null=True, to="Skill.skill"),
        ),
    ]