# Generated by Django 4.2.7 on 2023-12-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cards", "0003_skillofcard_card_skills"),
    ]

    operations = [
        migrations.AddField(
            model_name="skillofcard",
            name="effectOn",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
