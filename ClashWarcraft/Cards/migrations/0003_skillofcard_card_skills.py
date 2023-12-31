# Generated by Django 4.2.7 on 2023-12-26 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Skill", "0001_initial"),
        ("Cards", "0002_card_mobcard_alter_card_charactercard"),
    ]

    operations = [
        migrations.CreateModel(
            name="skillOfCard",
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
                ("remainingCooldown", models.IntegerField(blank=True, default=0)),
                (
                    "skill",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Skill.skill",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="card",
            name="skills",
            field=models.ManyToManyField(blank=True, to="Cards.skillofcard"),
        ),
    ]
