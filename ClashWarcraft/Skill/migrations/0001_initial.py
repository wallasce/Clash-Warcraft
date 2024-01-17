# Generated by Django 4.2.7 on 2023-11-14 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Skill",
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
                ("skillOff", models.CharField(blank=True, max_length=50)),
                ("level", models.IntegerField(blank=True)),
                ("type", models.CharField(blank=True, max_length=25)),
                ("cooldown", models.IntegerField(blank=True)),
                ("baseEffect", models.FloatField(blank=True)),
            ],
        ),
    ]