# Generated by Django 4.2.5 on 2023-11-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0012_product_usd_cornice_type_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_bestseller',
            field=models.BooleanField(blank=True, default=False, verbose_name='Хит продаж?'),
        ),
    ]
