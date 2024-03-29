from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.translation import gettext as _

from accounts.models import CustomUser
from helpers.functions import convert_price, format_price

# from . import choices


CONTROL_CHOICES = (
    ('left', "Слева"),
    ('center', "По середине"),
    ('right', "Справа"),
)


class ImagesOnAboutPage(models.Model):
    image = models.ImageField(verbose_name="Фото", upload_to="pages/about/")

    def __str__(self):
        return f"Фото: {self.pk}"

    class Meta:
        verbose_name = "Фотка на странице 'О компании'"
        verbose_name_plural = "Фотки на странице 'О компании'"


class Kind(models.Model):
    """Kind model."""

    name = models.CharField(
        verbose_name=_("Название вида"), max_length=255, unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"


class Category(models.Model):
    """Subcategory model."""

    class CorniceTypeChoices(models.TextChoices):
        aluminium = "aluminium", 'Алюминиевый'
        plastic = "plastic", 'Пластиковый'

    class ControlTypeChoices(models.TextChoices):
        manual = "manual", "Ручной"
        electrically_driven = "electrically_driven", "С электроприводом"

    name = models.CharField(verbose_name="Название категории", max_length=255)
    slug = models.SlugField(
        verbose_name="Ссылка категории",
        default="",
        help_text="Данное поле заполнять не нужно",
    )
    category_common_price_usd = models.SmallIntegerField(
        verbose_name="Цена (y.e) от",
        default=0,
        help_text="Данное поле используется чтобы отобразить среднюю стоимость продуктов данной категории на Главной странице")
    category_common_price_uzs = models.IntegerField(
        verbose_name="Цена (сум) от",
        default=0,
        help_text="Данное поле заполнять не нужно. Оно заполнится само при сохранении данного продукта")
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, verbose_name="Вид", related_name="subcategories")
    image = models.ImageField(verbose_name="Фото категории", upload_to="subcategories/", null=True)
    width_rounding = models.CharField(verbose_name="Округление по ширине для всех товаров категории", max_length=150,
                                      null=True, blank=True)
    length_rounding = models.CharField(
        verbose_name="Округление по длине для всех товаров категории", max_length=150, null=True, blank=True)

    product_width_from = models.IntegerField(verbose_name="Ширина от", default=0, null=True)
    product_width_to = models.IntegerField(verbose_name="Ширина до", default=0, null=True)

    product_length_from = models.IntegerField(verbose_name="Длина от", default=0, null=True)
    product_length_to = models.IntegerField(verbose_name="Длина до", default=0, null=True)

    cornice_type = models.CharField(
        verbose_name="Тип карниза",
        max_length=50,
        choices=CorniceTypeChoices.choices,
        default=CorniceTypeChoices.aluminium,
    )
    control_type = models.CharField(
        verbose_name="Тип управления",
        max_length=50,
        choices=ControlTypeChoices.choices,
        default=ControlTypeChoices.manual,
    )

    def get_absolute_url(self):
        return reverse("subcategory_detail", kwargs={"subcategory_slug": self.slug})

    def get_first_img(self):
        if self.image:
            return self.image.url

    def count_products(self):
        return self.products.all().count()

    def get_price(self):
        return format_price(self.category_common_price_uzs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.category_common_price_uzs = convert_price(self.category_common_price_usd, _format=False)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


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


class ProductManufacturerCountry(models.Model):
    name = models.CharField(verbose_name="Название страны", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна производитель"
        verbose_name_plural = "Страны производители"


class Product(models.Model):
    """Product model."""

    name = models.CharField(
        verbose_name="Название продукта", max_length=255, unique=True, default=""
    )
    # Базовая цена продукта
    usd_price = models.PositiveIntegerField(
        verbose_name="Базовая цена в долларах",
        default=0,
        null=True,
        blank=True
    )
    uzs_price = models.PositiveIntegerField(
        verbose_name="Базовая цена в сумах",
        default=0,
        help_text="Данное поле заполнять не нужно, цена будет рассчитываться от базовой цены в долларах"
    )
    # Цена продукта с электроприводом
    usd_electrical_price = models.PositiveIntegerField(
        verbose_name="Цена с электроприводом в долларах",
        default=0,
    )
    uzs_electrical_price = models.PositiveIntegerField(
        verbose_name="Цена с электроприводом в суммах",
        default=0,
        help_text="Данное поле заполнять не нужно, цена будет рассчитываться от цены элекртопривода в долларах",
    )
    body = models.TextField(verbose_name="Описание продукта", default="")
    placeholder = models.ImageField(
        verbose_name="Заставка",
        upload_to="products/placeholders/",
        null=True,
    )
    manufacturer_country = models.ForeignKey(ProductManufacturerCountry, on_delete=models.CASCADE, null=True,
                                             related_name="products", verbose_name="Страна производитель")
    fabric_type = models.ForeignKey(FabricType, on_delete=models.DO_NOTHING, related_name="products", null=True,
                                    verbose_name="Тип ткани")
    property = models.ForeignKey(ProductProperty, on_delete=models.DO_NOTHING, related_name="products", null=True,
                                 verbose_name="Свойство")
    dimming = models.ForeignKey(ProductDimming, on_delete=models.DO_NOTHING, related_name="products", null=True,
                                verbose_name="Затемнение")
    control = models.CharField(
        verbose_name="Управление",
        max_length=50,
        choices=CONTROL_CHOICES,
        default="left",
    )
    has_center_control = models.BooleanField(verbose_name='Есть ли управление по центру', default=False)
    has_rounding = models.BooleanField(verbose_name='Есть ли округление до пол квадрата', default=False)
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

    kind = models.ForeignKey(
        Kind,
        on_delete=models.CASCADE,
        verbose_name="Вид",
        default=None,
        null=True,
        related_name="products",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        default=None,
        null=True,
        related_name="products",
    )
    is_bestseller = models.BooleanField(
        verbose_name="Хит продаж?",
        blank=True,
        default=False
    )
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE, null=True, related_name="products",
                                   verbose_name="Коллекция")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    slug = models.SlugField(
        verbose_name="Ссылка продукта",
        default="",
        help_text="Данное поле заполнять не нужно",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        self.uzs_price = convert_price(self.usd_price, _format=False)
        self.uzs_electrical_price = convert_price(self.usd_electrical_price, _format=False)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"product_slug": self.slug})

    def add_to_cart(self):
        return reverse("cart:to_cart", kwargs={"product_id": self.pk, "action": "add"})

    def get_first_img(self):
        images = self.images.all()
        if images:
            return images[0].image.url

    def generate_qty_range(self):
        return [x for x in range(1, self.quantity + 1)]

    def get_price(self, _format=True):
        if not _format:
            return self.uzs_price
        return format_price(self.uzs_price)

    def get_electrical_price(self, _format=False):
        electrical_price = self.uzs_electrical_price - self.uzs_price
        price = 0 if self.category.control_type != 'electrically_driven' else electrical_price

        if not _format:
            return price

        return format_price(price)

    def get_price_with_discount(self, _format=True):
        if not self.discount:
            return self.get_price(_format)

        discount_amount = (self.uzs_price / 100) * self.discount
        final_price = round(self.uzs_price - discount_amount)
        if not _format:
            return final_price

        return format_price(final_price)

    def get_list_by_width_size(self):
        width_list = list(range(self.category.product_width_from, self.category.product_width_to + 1))
        return width_list

    def get_list_by_height_size(self):
        height_list = list(range(self.category.product_length_from, self.category.product_length_to + 1))
        return height_list


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
    subtitle = models.CharField(verbose_name="Подзаголовок проекта", max_length=255,
                                help_text="Показывается на главной странице")
    short_description = models.TextField(verbose_name="Краткое описание проекта", null=True,
                                         help_text="Краткое описание для проекта, показывается на странице проектов")
    image = models.ImageField(verbose_name="Фотография", upload_to="projects_gallery/")
    description = RichTextField(verbose_name="Описание проекта", null=True)
    slug = models.SlugField(verbose_name="Слаг", null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={"slug": self.slug})

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "45" height="45"/>')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class ProjectsGalleryImageItem(models.Model):
    project = models.ForeignKey(ProjectsGallery, on_delete=models.CASCADE, verbose_name="Проект", related_name="images")
    photo = models.ImageField(verbose_name="Дополнительное фото", upload_to="projects_gallery/addons/")

    class Meta:
        verbose_name = "Дополнительное фото"
        verbose_name_plural = "Дополнительные фото"


class Question(models.Model):
    """Question model."""

    name = models.CharField(
        verbose_name="Название вопроса", max_length=255, unique=True
    )
    video_link = models.URLField(verbose_name="Ссылка на видео")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


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


class SocialItem(models.Model):
    link = models.CharField(verbose_name="Ссылка на соц сеть", max_length=500)
    icon = models.ImageField(verbose_name="Фото соц сети.", upload_to="socials/icons/",
                             help_text="Фото должно быть расширения PNG")

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"


class Collection(models.Model):
    name = models.CharField(verbose_name="Название коллекции", max_length=150)
    type = models.ForeignKey(Kind, on_delete=models.CASCADE, related_name="types", verbose_name="Вид")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories",
                                 verbose_name="Категория")
    slug = models.SlugField(verbose_name="Ссылка коллекции", default="", help_text="Данное поле заполнять не нужно")

    def count_products(self):
        return self.products.all().count()

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"
