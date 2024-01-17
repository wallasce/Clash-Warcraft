# Generated by Django 5.0.1 on 2024-01-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('subtitle', models.CharField(max_length=75)),
                ('heading', models.CharField(max_length=45)),
                ('subheading', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=1000)),
                ('raid', models.IntegerField()),
            ],
        ),
    ]
