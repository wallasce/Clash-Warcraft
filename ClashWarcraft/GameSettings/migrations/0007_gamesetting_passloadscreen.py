# Generated by Django 4.2.7 on 2023-12-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("GameSettings", "0006_delete_winner"),
    ]

    operations = [
        migrations.AddField(
            model_name="gamesetting",
            name="passLoadScreen",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
