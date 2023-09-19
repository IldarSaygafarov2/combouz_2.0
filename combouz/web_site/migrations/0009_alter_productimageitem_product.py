# Generated by Django 4.2.5 on 2023-09-19 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web_site", "0008_product_placeholder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimageitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="web_site.product",
                verbose_name="Продукт",
            ),
        ),
    ]
