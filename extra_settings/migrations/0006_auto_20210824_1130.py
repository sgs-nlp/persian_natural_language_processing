# Generated by Django 3.2.5 on 2021-08-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_settings', '0005_auto_20210824_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinfo',
            name='_load_complate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fileinfo',
            name='from_which_row',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fileinfo',
            name='up_to_which_row',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
