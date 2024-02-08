from django import template

from cart.utils import get_cart_data
from helpers import functions as func
from web_site.models import Kind, Product, ProductColorItem, Category, Collection

register = template.Library()


@register.simple_tag()
def get_categories():
    return Kind.objects.all()


@register.simple_tag()
def get_width_or_length_range(category, range_type):
    range_list = []
    if range_type == 'width':
        range_list = list(range(category.product_width_from, category.product_width_to + 1))
    if range_type == 'length':
        range_list = list(range(category.product_length_from, category.product_length_to + 1))
    return range_list


@register.simple_tag()
def filter_number(number):
    return func.get_digits_from_number(number)


def get_products_by_category(category=None):
    if category is None:
        return Category.objects.all()

    return Category.objects.filter(category=category)


@register.simple_tag()
def convert_price(product_price):
    price = func.format_price(product_price)
    print(price)
    return price


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
    dimming = [i.dimming for i in products]
    countries = [product.manufacturer_country for product in products]
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


@register.simple_tag()
def get_subcategory_collections(subcategory_id):
    subcategory = Category.objects.get(pk=subcategory_id)
    collections = Collection.objects.filter(category=subcategory)
    return collections
