# Generated by Django 4.2.7 on 2023-11-14 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Skill", "0001_initial"),
        ("Character", "0003_remove_character_path_delete_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="skill",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Skill.skill",
            ),
        ),
    ]