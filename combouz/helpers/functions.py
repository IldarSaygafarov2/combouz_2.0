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
    product_price = product.get_price_with_discount(_format=False)
    # addon price
    # cornice_price = product.uzs_cornice_type_price if kwargs['cornice_type'] == 'aluminium' else 0
    control_price = product.uzs_electrical_price if kwargs['control_type'] == 'electro' else 0

    # sizes
    width = kwargs['width']
    height = kwargs['height']

    if type(width) is str or type(height) is str:
        width = int(''.join([i for i in kwargs['width'] if i.isdigit()]))
        height = int(''.join([i for i in kwargs['height'] if i.isdigit()]))

    decimal_size = (width / 100) * (height / 100)
    print(decimal_size)

    size_price = product_price

    if product.has_rounding:
        if decimal_size < 0.5:
            size_price = int(product_price) / 2
        elif 0.5 < decimal_size < 1.0:
            size_price = product_price
        elif decimal_size > 1.0:
            size_price = decimal_size * product_price
    elif decimal_size > 1.0:
        size_price = decimal_size * product_price
    else:
        size_price = product_price

    total_price = int(size_price)*int(kwargs['quantity'])
    if control_price == 0:
        return total_price
    elif control_price != 0:
        return total_price + (control_price * int(kwargs['quantity']))

    # if cornice_price == 0:
    #     return total_price
    # elif cornice_price != 0:
    #     return int(total_price) + (int(cornice_price * int(kwargs['quantity'])) - (size_price * int(kwargs['quantity'])))

    if control_price == 0:
        return total_price


    # total_price = int(
    #     (size_price * int(kwargs['quantity'])) + cornice_price + control_price
    # )


    return total_price


# def _convert_to_int(data):
#     if not data:
#         return 0
#     return int(''.join([i for i in data if i.isdigit()]))


def get_product_options(request):
    selected_width = request.POST.get('item-width', 0)
    selected_height = request.POST.get('item-length', 0)
    selected_control = request.POST.get('item-control')
    selected_cornice_type = request.POST.get('item-cornice-type')
    selected_control_type = request.POST.get('item-control-type')

    return {
        "product_selected_width": selected_width,
        "product_selected_height": selected_height,
        "product_selected_control": selected_control,
        "product_selected_cornice_type": selected_cornice_type,
        "product_selected_control_type": selected_control_type,
    }
