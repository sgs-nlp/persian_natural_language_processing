# Generated by Django 3.2.5 on 2021-08-08 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistical_pnc', '0002_auto_20210808_1343'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Context',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='context',
            new_name='content',
        ),
    ]
