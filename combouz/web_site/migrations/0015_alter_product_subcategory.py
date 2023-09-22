# Generated by Django 4.2.5 on 2023-09-22 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web_site", "0014_alter_product_subcategory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="web_site.subcategory",
                verbose_name="Подкатегория",
            ),
        ),
    ]