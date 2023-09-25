# Generated by Django 4.2.5 on 2023-09-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0020_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlengthitem',
            name='length',
            field=models.CharField(default='', max_length=100, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='productlengthitem',
            name='length_en',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='productlengthitem',
            name='length_ru',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='productoptionitem',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название характеристики'),
        ),
        migrations.AlterField(
            model_name='productoptionitem',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название характеристики'),
        ),
        migrations.AlterField(
            model_name='productoptionitem',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название характеристики'),
        ),
        migrations.AlterField(
            model_name='productwidthitem',
            name='width',
            field=models.CharField(default='', max_length=100, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='productwidthitem',
            name='width_en',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='productwidthitem',
            name='width_ru',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Ширина'),
        ),
    ]
