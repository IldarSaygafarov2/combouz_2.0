from django import template

from cart.utils import get_cart_data
from helpers import functions as func
from web_site.models import Category, Product, ProductColorItem, Subcategory

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_width_or_length_range(category, range_type):
    range_list = []
    if range_type == 'width':
        range_list = list(range(category.product_width_from, category.product_width_to + 1))
    if range_type == 'length':
        range_list = list(range(category.product_length_from, category.product_length_to + 1))
    return range_list


@register.simple_tag()
def get_config():
    from constance import config

    return config


# def get_category_by_path(path: str):
#     items = [item for item in path.split("/") if item]
#     category = Category.objects.filter(slug=items[-1]).first()
#     if category is None:
#         return False
#     return category
#
#
# @register.simple_tag()
# def get_subcategories(path):
#     category = get_category_by_path(path)
#     if not category:
#         return Category.objects.all()
#     return Subcategory.objects.filter(category=category)


def get_products_by_category(category=None):
    if category is None:
        return Subcategory.objects.all()

    return Subcategory.objects.filter(category=category)


@register.simple_tag()
def convert_price(product_price):
    return func.format_price(product_price)


@register.simple_tag()
def get_cart_qty(request):
    cart = get_cart_data(request)
    return cart["cart_total_quantity"]


@register.simple_tag()
def get_all_products_count():
    return Product.objects.all().count()


@register.simple_tag()
def get_sort_fields():
    products = Product.objects.all()
    colors = set([ProductColorItem.objects.get(pk=color["color_id"]) for color in products.values()])
    dimming = [i.dimming for i in Product.objects.all()]
    countries = [country["manufacturer_country"] for country in products.values()]
    return {
        "colors": colors,
        "dimming": dimming,
        "countries": countries
    }


@register.simple_tag()
def count_products_by_color(color):
    products = Product.objects.filter(color=color)
    return products.count()


@register.simple_tag()
def count_products_by_dimming(dimming):
    products = Product.objects.filter(dimming=dimming)
    return products.count()


@register.simple_tag()
def count_products_by_country(country):
    products = Product.objects.filter(manufacturer_country=country)
    return products.count()
