from modeltranslation.translator import register, TranslationOptions

from blog.models import Article
from .models import *


@register(ProductManufacturerCountry)
class ProductManufacturerCountryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Collection)
class CollectionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "short_description",
        "description",
    )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Subcategory)
class SubcategoryTranslationOptions(TranslationOptions):
    fields = ("name", "width_rounding", "length_rounding")


@register(ProductColorItem)
class ProductColorItemTranslationOptions(TranslationOptions):
    fields = ("color",)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "body",
        # "manufacturer_country",
        # "fabric_type",
        # "property",
    )


@register(ProductOptionItem)
class ProductOptionItemTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "descr",
    )


@register(ProjectsGallery)
class ProjectsGalleryTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "subtitle",
        "short_description",
        "description",
    )


@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = (
        "body",
        "author",
        "company_name",
    )


@register(HeroGallery)
class HeroGalleryTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "body",
    )


@register(FabricType)
class FabricTypeTranslationOptions(TranslationOptions):
    fields = (
        "title",
    )


@register(ProductProperty)
class ProductPropertyTranslationOptions(TranslationOptions):
    fields = (
        "title",
    )
