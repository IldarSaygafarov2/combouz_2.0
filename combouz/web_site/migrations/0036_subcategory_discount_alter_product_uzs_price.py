# Generated by Django 4.2.5 on 2023-10-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_site", "0035_imagesonaboutpage"),
    ]

    operations = [
        migrations.AddField(
            model_name="subcategory",
            name="discount",
            field=models.SmallIntegerField(
                default=0,
                help_text="Размер скидки для всех товаров этой подкатегории",
                verbose_name="Размер скидки",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="uzs_price",
            field=models.IntegerField(
                blank=True,
                default=0,
                help_text="Данное поле заполнять не нужно.",
                null=True,
                verbose_name=" Цена в узбекских сумах",
            ),
        ),
    ]
