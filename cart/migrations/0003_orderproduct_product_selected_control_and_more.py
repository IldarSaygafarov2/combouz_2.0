# Generated by Django 4.2.5 on 2023-12-13 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_orderproduct_product_selected_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='product_selected_control',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='product_selected_control_type',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='product_selected_cornice_type',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]