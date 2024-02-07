import requests
from rest_framework import status
from rest_framework.response import Response



def format_price(price):
    return f"{price:,d}".replace(',', ' ')


def convert_price(product_price, _format=True):
    api_key = "0a1fb85a88eafb2934c0bae7"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    resp = requests.get(url).json()
    uzs = resp["conversion_rates"]["UZS"]
    if _format:
        return format_price(round(product_price * uzs))
    return round(product_price * uzs)


def get_digits_from_number(number):
    phone = ''.join(list(filter(str.isdigit, number)))
    return f'+{phone}'


def calculate_price(obj, **kwargs):
    product = obj.objects.filter(pk=kwargs['product_id'])
    if not product.exists():
        return Response(status=status.HTTP_404_NOT_FOUND, data={
            'description': 'Product with id={} not found'.format(kwargs['product_id'])
        })

    product = product.first()
    product_price = product.get_price(_format=False)

    # addon price
    cornice_price = product.uzs_cornice_type_price if kwargs['cornice_type'] == 'aluminium' else product_price
    control_price = product.uzs_electrical_price if kwargs['control_type'] == 'electro' else product_price

    # sizes
    width = kwargs['width']
    height = kwargs['height']

    if type(width) is str or type(height) is str:
        width = int(''.join([i for i in kwargs['width'] if i.isdigit()]))
        height = int(''.join([i for i in kwargs['height'] if i.isdigit()]))

    decimal_size = (width / 100) * (height / 100)

    size_price = product_price
    if decimal_size < 0.5:
        size_price = int(product_price) / 2
    elif 0.5 < decimal_size < 1.0:
        size_price = product_price
    elif decimal_size > 1.0:
        size_price = decimal_size * product_price

    total_price = int(
        (size_price + (cornice_price - product_price) + (control_price - product_price)) * int(kwargs['quantity'])
    )

    return total_price