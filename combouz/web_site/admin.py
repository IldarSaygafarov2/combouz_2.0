from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    Category,
    Client,
    Feedback,
    HeroGallery,
    Product,
    ProductColorItem,
    ProductImageItem,
    ProductOptionItem,
    ProjectsGallery,
    Question,
    Subcategory,
    Comment,
    FabricType,
    ProductProperty,
    ProductDimming
)


@admin.register(FabricType)
class FabricTypeAdmin(TranslationAdmin):
    fields = ("title",)


@admin.register(ProductProperty)
class ProductPropertyAdmin(TranslationAdmin):
    fields = ("title",)


@admin.register(ProductDimming)
class ProductDimmingAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    fieldsets = [
        (
            "Общее",
            {
                "fields": ["name", "slug", "show_on_homepage", "make_bestseller"]
            }
        ),
        (
            "Округление",
            {
                "fields": ["width_rounding", "length_rounding"]
            }
        ),
        (
            "Ширина продуктов",
            {
                "fields": ["product_width_from", "product_width_to"]
            }
        ),
        (
            "Длина продуктов",
            {
                "fields": ["product_length_from", "product_length_to"]
            }
        )
    ]

    prepopulated_fields = {"slug": ("name",)}
    list_display = ("pk", "name", "show_on_homepage", "make_bestseller")
    list_display_links = ("pk", "name")
    list_editable = ("show_on_homepage", "make_bestseller")


@admin.register(Subcategory)
class SubcategoryAdmin(TranslationAdmin):
    list_display = ("pk", "name", "category")
    list_display_links = ("pk", "name")
    list_filter = ("category",)
    list_editable = ("category",)
    prepopulated_fields = {"slug": ("name",)}


class ProductImageItemAdmin(admin.TabularInline):
    model = ProductImageItem
    extra = 1


class ProductOptionItemAdmin(admin.TabularInline):
    model = ProductOptionItem
    extra = 1


@admin.register(ProductColorItem)
class ProductColorItemAdmin(TranslationAdmin):
    pass


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [
        ProductImageItemAdmin,
        ProductOptionItemAdmin,
    ]
    list_display = (
        "pk",
        "name",
        "usd_price",
        "uzs_price",
        "quantity",
        "category",
        "subcategory",
    )
    list_display_links = ("pk", "name")
    list_filter = ("category", "subcategory")
    list_editable = ("usd_price", "category", "subcategory")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(HeroGallery)
class HeroGalleryAdmin(TranslationAdmin):
    list_display = ("pk", "title", "body", "img_preview")
    list_display_links = ("pk", "title")
    list_editable = ("body",)


@admin.register(ProjectsGallery)
class ProjectsGalleryAdmin(TranslationAdmin):
    list_display = ("pk", "title", "subtitle", "img_preview")
    list_display_links = ("pk", "title")
    list_editable = ("subtitle",)


@admin.register(Feedback)
class FeedbackAdmin(TranslationAdmin):
    list_display = ("pk", "author", "company_name", "img_preview")
    list_editable = (
        "author",
        "company_name",
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
