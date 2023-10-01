from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "width_rounding", "length_rounding")


@register(Subcategory)
class SubcategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(ProductColorItem)
class ProductColorItemTranslationOptions(TranslationOptions):
    fields = ("color",)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "body",
        "manufacturer_country",
        "fabric_type",
        "property",
    )


@register(ProductWidthItem)
class ProductWidthItemTranslationOptions(TranslationOptions):
    fields = (
        "width",
    )


@register(ProductLengthItem)
class ProductLengthItemTranslationOptions(TranslationOptions):
    fields = (
        "length",
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
