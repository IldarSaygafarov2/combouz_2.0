from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.translation import gettext as _

from accounts.models import CustomUser
from helpers.functions import convert_price
from . import choices


# Create your models here.


class Category(models.Model):
    """Category model."""

    name = models.CharField(
        verbose_name=_("Название категории"), max_length=255, unique=True
    )
    slug = models.SlugField(
        verbose_name=_("Ссылка категории"),
        default="",
        help_text="Данное поле заполнять не нужно.",
    )
    show_on_homepage = models.BooleanField(
        verbose_name="Показать на главной",
        default=False,
        help_text="При выборе данного пункта, все продукты этой категории будут показаны на главной странице",
    )
    make_bestseller = models.BooleanField(
        verbose_name="Сделать бестселлером",
        default=False,
        help_text="При выборе данного пункта, покажет все товары данной категории в секции 'Хиты продаж' ",
    )
    width_rounding = models.CharField(
        verbose_name="Округление по ширине для всех товаров категории",
        max_length=150,
        null=True,
        blank=True,
    )
    length_rounding = models.CharField(
        verbose_name="Округление по длине для всех товаров категории",
        max_length=150,
        null=True,
        blank=True,
    )

    product_width_from = models.IntegerField(verbose_name="Ширина от", default=0, null=True)
    product_width_to = models.IntegerField(verbose_name="Ширина до", default=0, null=True)

    product_length_from = models.IntegerField(verbose_name="Длина от", default=0, null=True)
    product_length_to = models.IntegerField(verbose_name="Длина до", default=0, null=True)

    category_usd_price = models.IntegerField(verbose_name="Стоимость в долларах", default=0)

    def get_uzs_price(self):
        return convert_price(self.category_usd_price)

    def count_products(self):
        return self.products.all().count()

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"category_slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    """Subcategory model."""

    name = models.CharField(verbose_name="Название подкатегории", max_length=255)
    slug = models.SlugField(
        verbose_name="Ссылка подкатегории",
        default="",
        help_text="Данное поле заполнять не нужно",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="subcategories",
    )

    image = models.ImageField(verbose_name="Фото подкатегории", upload_to="subcategories/", null=True)

    def get_absolute_url(self):
        return reverse("subcategory_detail", kwargs={"subcategory_slug": self.slug})

    def get_first_img(self):
        if self.image:
            return self.image.url

    def count_products(self):
        return self.products.all().count()

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class ProductColorItem(models.Model):
    color = models.CharField(verbose_name="Цвет продукта", max_length=100, unique=True)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class FabricType(models.Model):
    title = models.CharField(verbose_name="Тип ткани", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип ткани"
        verbose_name_plural = "Типы ткани"


class ProductProperty(models.Model):
    title = models.CharField(verbose_name="Свойство", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Свойство"
        verbose_name_plural = "Свойства"


class ProductDimming(models.Model):
    dimming = models.IntegerField(verbose_name="Затемнение", default=0)

    def __str__(self):
        return str(self.dimming)

    class Meta:
        verbose_name = "Затеменение"
        verbose_name_plural = "Затемнения"


class Product(models.Model):
    """Product model."""

    name = models.CharField(
        verbose_name="Название продукта", max_length=255, unique=True, default=""
    )
    usd_price = models.SmallIntegerField(verbose_name="Цена в y.e", default=0)
    uzs_price = models.IntegerField(
        verbose_name=" Цена в узбекских сумах",
        default=0,
        help_text="Данное поле заполнять не нужно, при добавлении цены в y.e данное поле будет заполнено автоматически",
    )
    body = models.TextField(verbose_name="Описание продукта", default="")
    placeholder = models.ImageField(
        verbose_name="Заставка",
        upload_to="products/placeholders/",
        null=True,
    )
    manufacturer_country = models.CharField(
        verbose_name="Страна производитель",
        default="",
        max_length=255,
    )
    fabric_type = models.ForeignKey(FabricType, on_delete=models.DO_NOTHING, related_name="products", null=True,
                                    verbose_name="Тип ткани")
    property = models.ForeignKey(ProductProperty, on_delete=models.DO_NOTHING, related_name="products", null=True,
                                 verbose_name="Свойство")
    dimming = models.ForeignKey(ProductDimming, on_delete=models.DO_NOTHING, related_name="products", null=True,
                                verbose_name="Затемнение")
    control = models.CharField(
        verbose_name="Управление",
        max_length=50,
        choices=choices.CONTROL_CHOICES,
        default="left",
    )
    cornice_type = models.CharField(
        verbose_name="Тип карниза",
        max_length=50,
        choices=choices.CORNICE_TYPE_CHOICES,
        default="aluminum",
    )
    control_type = models.CharField(
        verbose_name="Тип управления",
        max_length=50,
        choices=choices.CONTROL_TYPE_CHOICES,
        default="manual",
    )
    quantity = models.SmallIntegerField(verbose_name="Количество продукта", default=0)
    color = models.ForeignKey(
        ProductColorItem,
        on_delete=models.CASCADE,
        verbose_name="Цвет продукта",
        null=True,
    )
    discount = models.SmallIntegerField(
        verbose_name="Размер скидки", default=0, null=True, blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        default=None,
        null=True,
        related_name="products",
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        verbose_name="Подкатегория",
        default=None,
        null=True,
        related_name="products",
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    slug = models.SlugField(
        verbose_name="Ссылка продукта",
        default="",
        help_text="Данное поле заполнять не нужно",
    )

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"product_slug": self.slug})

    def add_to_cart(self):
        return reverse("cart:to_cart", kwargs={"product_id": self.pk, "action": "add"})

    def remove_from_cart(self):
        return reverse(
            "cart:to_cart",
            kwargs={"product_id": self.pk, "action": "delete"},
        )

    def get_first_img(self):
        images = self.images.all()
        if images:
            return images[0].image.url

    def generate_qty_range(self):
        return [x for x in range(1, self.quantity + 1)]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.uzs_price = convert_price(self.usd_price)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


# class ProductWidthItem(models.Model):
#     """ProductWidthItem model"""
#
#     width = models.CharField(
#         verbose_name="Ширина",
#         max_length=100,
#         default="",
#     )
#     product = models.ForeignKey(
#         Product,
#         on_delete=models.CASCADE,
#         verbose_name="Продукт",
#         related_name="width_list",
#     )
#
#     def __str__(self):
#         return f"{self.product}: {self.width}"
#
#     class Meta:
#         verbose_name = "Ширина продукта"
#         verbose_name_plural = "Ширина продукта"
#
#
# class ProductLengthItem(models.Model):
#     """ProductWidthItem model"""
#
#     length = models.CharField(
#         verbose_name="Длина",
#         max_length=100,
#         default="",
#     )
#     product = models.ForeignKey(
#         Product,
#         on_delete=models.CASCADE,
#         verbose_name="Продукт",
#         related_name="length_list",
#     )
#
#     def __str__(self):
#         return f"{self.product}: {self.length}"
#
#     class Meta:
#         verbose_name = "Длина продукта"
#         verbose_name_plural = "Длина продукта"


class ProductImageItem(models.Model):
    """ProductImageItem model."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="images",
    )
    image = models.ImageField(verbose_name="Фото продукта", upload_to="products/")

    class Meta:
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фотки продуктов"


class ProductOptionItem(models.Model):
    """ProductOptionItem model."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="options",
    )
    title = models.CharField(
        verbose_name="Название характеристики",
        max_length=100,
    )
    descr = models.TextField(verbose_name="Описание характеристики")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"


class HeroGallery(models.Model):
    """HeroGallery model."""

    title = models.CharField(verbose_name="Заголовок слайдера", max_length=255)
    body = models.TextField(verbose_name="Описание слайдера")
    img = models.ImageField(verbose_name="Фото слайда", upload_to="slides/", default="")

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.img.url}" width = "150" height="150"/>')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"


class ProjectsGallery(models.Model):
    """ProjectsGallery model."""

    title = models.CharField(
        verbose_name="Название проекта", max_length=255, unique=True
    )
    subtitle = models.CharField(verbose_name="Подзаголовок проекта", max_length=255)
    image = models.ImageField(verbose_name="Фотография", upload_to="projects_gallery/")

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "45" height="45"/>')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Question(models.Model):
    """Question model."""

    name = models.CharField(
        verbose_name="Название вопроса", max_length=255, unique=True
    )
    video_link = models.URLField(verbose_name="Ссылка на видео")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Feedback(models.Model):
    """Feedback model."""

    body = models.TextField(verbose_name="Текст отзыва")
    author = models.CharField(verbose_name="Автор отзыва", max_length=255)
    author_avatar = models.ImageField(
        verbose_name="Фото автора", upload_to="feedbacks/avatars/"
    )
    company_name = models.CharField(verbose_name="Компания автора", max_length=255)

    def img_preview(self):  # new
        return mark_safe(
            f'<img src = "{self.author_avatar.url}" width = "45" height="45" style="border-radius: 50%"/>'
        )

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Client(models.Model):
    """Client model."""

    name = models.CharField(
        verbose_name="Название клиента", max_length=255, unique=True
    )
    image = models.ImageField(verbose_name="Фото компании", upload_to="clients/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="comments"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField(verbose_name="Текст комментария")

    def __str__(self):
        return f"{self.author}: {self.product}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class CommentItem(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    img = models.ImageField(
        verbose_name="Фото",
        upload_to="comments/",
        blank=True,
        null=True,
    )
