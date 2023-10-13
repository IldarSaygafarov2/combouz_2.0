# Generated by Django 4.2.5 on 2023-10-13 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_site", "0033_remove_product_usd_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="uzs_price",
            field=models.IntegerField(
                blank=True,
                default=0,
                help_text="Данное поле заполнять не нужно, при добавлении цены в y.e данное поле будет заполнено автоматически",
                null=True,
                verbose_name=" Цена в узбекских сумах",
            ),
        ),
    ]