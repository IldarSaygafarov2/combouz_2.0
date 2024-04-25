# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from django.template.defaultfilters import slugify
from django.urls import reverse


class Article(models.Model):
    name = models.CharField(max_length=500, verbose_name="Заголовок статьи", unique=True)
    photo = models.ImageField(verbose_name="Фото", upload_to="blog/")
    short_description = models.CharField(max_length=500, verbose_name="Краткое описание")
    description = RichTextUploadingField(verbose_name="Полное описание статьи")
    slug = models.SlugField(verbose_name="Слаг", null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
