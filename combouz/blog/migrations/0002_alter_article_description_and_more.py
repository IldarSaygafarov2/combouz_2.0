# Generated by Django 4.2.5 on 2023-11-14 05:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Полное описание статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Полное описание статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Полное описание статьи'),
        ),
    ]
