# Generated by Django 5.0.6 on 2024-06-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0004_remove_institute_change_zoom_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='change_zoom_url',
            field=models.BooleanField(default=False),
        ),
    ]
