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
    ProductLengthItem,
    ProductOptionItem,
    ProductWidthItem,
    ProjectsGallery,
    Question,
    Subcategory,
    Comment,
)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("pk", "name")
    list_display_links = ("pk", "name")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subcategory)
class SubcategoryAdmin(TranslationAdmin):
    list_display = ("pk", "name", "category")
    list_display_links = ("pk", "name")
    list_filter = ("category",)
    prepopulated_fields = {"slug": ("name",)}


class ProductImageItemAdmin(admin.TabularInline):
    model = ProductImageItem
    extra = 1


class ProductLengthItemAdmin(admin.TabularInline):
    model = ProductLengthItem
    extra = 1


class ProductOptionItemAdmin(admin.TabularInline):
    model = ProductOptionItem
    extra = 1


class ProductWidthItemAdmin(admin.TabularInline):
    model = ProductWidthItem
    extra = 1


@admin.register(ProductColorItem)
class ProductColorItemAdmin(TranslationAdmin):
    pass


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [
        ProductLengthItemAdmin,
        ProductWidthItemAdmin,
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
