from django.http import JsonResponse
from rest_framework.decorators import api_view

from web_site.models import Product
from helpers.functions import format_price


@api_view(['POST'])
def get_something(request):
    data = request.data
    # product data
    product = Product.objects.get(pk=data['productId'])
    product_price = product.get_price(_format=False)

    # width and height
    width = int(''.join([i for i in data['width'] if i.isdigit()]))
    height = int(''.join([i for i in data['height'] if i.isdigit()]))
    decimal_size = (width / 100) * (height / 100)
    price = product_price
    if decimal_size < 0.5:
        price = product_price / 2
    elif 0.5 < decimal_size < 1.0:
        price = product_price
    elif decimal_size > 1.0:
        price = decimal_size * product_price

    print('PRICE', price)
    print('DECIMAL SIZE', decimal_size)
    return JsonResponse({"price": price})
