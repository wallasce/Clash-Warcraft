# Generated by Django 5.0.1 on 2024-01-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteContent', '0017_sectionpagepanel_imagessectionpage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpagepanel',
            name='style',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
