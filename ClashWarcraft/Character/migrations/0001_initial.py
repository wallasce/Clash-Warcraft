# Generated by Django 4.2.7 on 2023-11-11 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attributes",
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
                ("armor", models.FloatField()),
                ("power", models.FloatField()),
                ("stamina", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Path",
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
                ("imageSelection", models.CharField(max_length=50)),
                ("imageGame", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Character",
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
                ("name", models.CharField(max_length=50)),
                ("faction", models.CharField(max_length=8)),
                ("kind", models.CharField(max_length=15)),
                ("type", models.CharField(max_length=6)),
                (
                    "attributes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Character.attributes",
                    ),
                ),
                (
                    "path",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Character.path"
                    ),
                ),
            ],
        ),
    ]