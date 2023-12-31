# Generated by Django 4.2.7 on 2023-11-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GameSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("passHomeScreen", models.BooleanField()),
                ("gameMode", models.CharField(max_length=3)),
                ("faction", models.CharField(max_length=8)),
            ],
        ),
    ]
