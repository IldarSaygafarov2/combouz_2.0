# Generated by Django 4.2.5 on 2023-09-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0021_alter_productlengthitem_length_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='author_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Автор отзыва'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='author_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Автор отзыва'),
        ),
    ]