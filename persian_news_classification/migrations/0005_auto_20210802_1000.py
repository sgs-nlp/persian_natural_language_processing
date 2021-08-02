# Generated by Django 3.2.5 on 2021-08-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persian_news_classification', '0004_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='keywords',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='categories_list',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='category_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='content_string_code_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='content_string_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='content_words_code_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='content_words_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='content_words_without_stopword_code_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='content_words_without_stopword_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='keywords_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='stopwords_list',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='titr_string_code_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='titr_string_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='titr_words_code_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='titr_words_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='titr_words_without_stopword_code_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='titr_words_without_stopword_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='vector_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]