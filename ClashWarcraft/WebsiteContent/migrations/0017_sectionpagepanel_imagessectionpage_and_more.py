# Generated by Django 5.0.1 on 2024-01-29 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageManager', '0001_initial'),
        ('WebsiteContent', '0016_alter_headerpage_buttons'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionpagepanel',
            name='imagesSectionPage',
            field=models.ManyToManyField(blank=True, to='ImageManager.uploadedimage'),
        ),
        migrations.AddField(
            model_name='sectionpagepanel',
            name='preSectionPanel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ImageUploaded2preSectionPanel', to='ImageManager.uploadedimage'),
        ),
        migrations.AlterField(
            model_name='sectionpagepanel',
            name='backgroundSectionPage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ImageUploaded2BackgroundSection', to='ImageManager.uploadedimage'),
        ),
    ]