# Generated by Django 4.2.5 on 2023-09-19 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web_site", "0009_alter_productimageitem_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productlengthitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="length_list",
                to="web_site.product",
                verbose_name="Продукт",
            ),
        ),
        migrations.AlterField(
            model_name="productoptionitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="options",
                to="web_site.product",
                verbose_name="Продукт",
            ),
        ),
        migrations.AlterField(
            model_name="productwidthitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="width_list",
                to="web_site.product",
                verbose_name="Продукт",
            ),
        ),
    ]
