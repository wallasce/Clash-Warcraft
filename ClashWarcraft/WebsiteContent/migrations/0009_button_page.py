# Generated by Django 5.0.1 on 2024-01-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteContent', '0008_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='page',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
