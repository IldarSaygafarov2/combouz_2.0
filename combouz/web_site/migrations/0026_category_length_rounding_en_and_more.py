# Generated by Django 4.2.5 on 2023-10-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_site", "0025_remove_category_size_rounding_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="length_rounding_en",
            field=models.CharField(
                blank=True,
                max_length=150,
                null=True,
                verbose_name="Округление по длине для всех товаров категории",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="length_rounding_ru",
            field=models.CharField(
                blank=True,
                max_length=150,
                null=True,
                verbose_name="Округление по длине для всех товаров категории",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="width_rounding_en",
            field=models.CharField(
                blank=True,
                max_length=150,
                null=True,
                verbose_name="Округление по ширине для всех товаров категории",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="width_rounding_ru",
            field=models.CharField(
                blank=True,
                max_length=150,
                null=True,
                verbose_name="Округление по ширине для всех товаров категории",
            ),
        ),
    ]