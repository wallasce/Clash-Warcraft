# Generated by Django 5.0.1 on 2024-01-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteContent', '0014_rename_sectionpage_sectionpagepanel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpagepanel',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
