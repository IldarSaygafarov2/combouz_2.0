from cart.utils import get_cart_data
from django import template
from helpers import functions as func
from web_site.models import Category, Product

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
