# Generated by Django 3.2.5 on 2021-08-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistical_pnc', '0008_auto_20210814_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='vector',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
