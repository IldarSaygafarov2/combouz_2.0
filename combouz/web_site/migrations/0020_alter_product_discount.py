# Generated by Django 4.2.5 on 2023-09-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0019_herogallery_body_en_herogallery_body_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.SmallIntegerField(blank=True, default=0, null=True, verbose_name='Размер скидки'),
        ),
    ]
