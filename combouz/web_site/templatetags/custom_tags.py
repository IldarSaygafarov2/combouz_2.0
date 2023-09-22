from django import template

from cart.utils import get_cart_data
from helpers import functions as func
from web_site.models import Category, Product, ProductColorItem, ProductOptionItem

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = Category.objects.all()
    return categories


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
    dimming = set([item["dimming"] for item in products.values()])
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
