# Generated by Django 5.0.6 on 2024-06-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(help_text='Enter a valid URL address', verbose_name='Original URL')),
                ('short_url', models.URLField(blank=True, max_length=100, unique=True, verbose_name='Short URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
            ],
            options={
                'verbose_name': 'Short URL',
                'verbose_name_plural': 'Short URLs',
            },
        ),
    ]
