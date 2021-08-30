# Generated by Django 3.2.5 on 2021-08-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileinfo',
            name='file',
        ),
        migrations.AddField(
            model_name='fileinfo',
            name='file_path',
            field=models.FilePathField(default=12),
            preserve_default=False,
        ),
    ]