# Generated by Django 4.2.5 on 2023-11-12 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0003_remove_product_control_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='web_site.collection', verbose_name='Коллекция'),
        ),
    ]
