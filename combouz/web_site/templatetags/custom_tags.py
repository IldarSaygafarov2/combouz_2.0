from django import template
from helpers import functions as func
from web_site.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = Category.objects.all()
    return categories


@register.simple_tag()
def convert_price(product_price):
    return func.format_price(product_price)
