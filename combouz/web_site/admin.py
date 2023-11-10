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
    ProductDimming,
    ImagesOnAboutPage,
    ProjectsGalleryImageItem,
    SocialItem,
    Collection
)


@admin.register(SocialItem)
class SocialItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ImagesOnAboutPage)
class ImagesOnAboutPageAdmin(admin.ModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(TranslationAdmin):
    list_display = ('pk', 'name', 'type', 'category')
    list_display_links = ('pk', 'name')
    list_filter = ('type', 'category')
    list_editable = ('type', 'category')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FabricType)
class FabricTypeAdmin(TranslationAdmin):
    list_display = ("title",)


@admin.register(ProductProperty)
class ProductPropertyAdmin(TranslationAdmin):
    list_display = ("title",)
    list_display_links = ("title",)


@admin.register(ProductDimming)
class ProductDimmingAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("pk", "name")
    list_display_links = ("pk", "name")


@admin.register(Subcategory)
class SubcategoryAdmin(TranslationAdmin):
    list_display = ("pk", "name",  "category")
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
        "uzs_price",
        "quantity",
        "category",
        "subcategory",
    )
    list_display_links = ("pk", "name")
    list_filter = ("category", "subcategory")
    list_editable = (
        "category",
        "subcategory"
    )
    prepopulated_fields = {"slug": ("name",)}


@admin.register(HeroGallery)
class HeroGalleryAdmin(TranslationAdmin):
    list_display = ("pk", "title", "body", "img_preview")
    list_display_links = ("pk", "title")
    list_editable = ("body",)


class ProjectsGalleryImageItemInline(admin.TabularInline):
    model = ProjectsGalleryImageItem
    extra = 1


@admin.register(ProjectsGallery)
class ProjectsGalleryAdmin(TranslationAdmin):
    list_display = ("pk", "title", "subtitle", "img_preview")
    list_display_links = ("pk", "title")
    list_editable = ("subtitle",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectsGalleryImageItemInline]


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
