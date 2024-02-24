from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    Kind,
    Client,
    Feedback,
    HeroGallery,
    Product,
    ProductColorItem,
    ProductImageItem,
    ProductOptionItem,
    ProjectsGallery,
    Question,
    Category,
    Comment,
    FabricType,
    ProductProperty,
    ProductDimming,
    ImagesOnAboutPage,
    ProjectsGalleryImageItem,
    SocialItem,
    Collection,
    ProductManufacturerCountry
)


@admin.register(SocialItem)
class SocialItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ImagesOnAboutPage)
class ImagesOnAboutPageAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductManufacturerCountry)
class ProductManufacturerCountryAdmin(TranslationAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')


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


@admin.register(Kind)
class KindAdmin(TranslationAdmin):
    list_display = ("pk", "name")
    list_display_links = ("pk", "name")


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    fieldsets = [
        (
            'Общее',
            {
                'fields': ['name', 'kind', 'image', 'category_common_price_usd', 'category_common_price_uzs', 'slug']
            }
        ),
        (
            "Ширина",
            {
                'fields': ['width_rounding']
            }
        ),
        (
            "Длина",
            {
                'fields': ['length_rounding']
            }
        ),
        (
            'Размеры',
            {
                'fields': ['product_width_from', 'product_width_to', 'product_length_from', 'product_length_to']
            }
        ),
        (
            'Опции',
            {
                "fields": ['cornice_type', 'control_type']
            }
        )
    ]
    list_display = ("pk", "name", "category_common_price_usd", "category_common_price_uzs", "kind")
    list_display_links = ("pk", "name")
    list_filter = ("kind",)
    list_editable = ("kind", "category_common_price_usd")
    readonly_fields = ("category_common_price_uzs",)
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
    fieldsets = [
        (
            "Общее",
            {
                "fields": ['name', 'body', 'quantity', 'placeholder', 'discount', 'is_bestseller', 'slug']
            }
        ),
        (
            "Опции",
            {
                "fields": [
                    'kind',
                    'category',
                    'collection',
                    'manufacturer_country',
                    'control',
                    'has_center_control',
                    'has_rounding',
                    'fabric_type',
                    'property',
                    'dimming',
                    'color'
                ]
            }
        ),
        (
            "Цены",
            {
                "fields": [
                    'usd_price',
                    'uzs_price',
                    'usd_electrical_price',
                    'uzs_electrical_price',
                ]
            }
        )
    ]
    inlines = [
        ProductImageItemAdmin,
        ProductOptionItemAdmin,
    ]
    list_display = (
        "pk",
        "name",
        "usd_price",
        "kind",
        "category",
        "collection",
        "is_bestseller"
    )
    list_display_links = ("pk", "name")
    list_filter = ("kind", "category", "collection")
    list_editable = (
        "usd_price",
        "kind",
        "category",
        "collection",
        "is_bestseller"
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
