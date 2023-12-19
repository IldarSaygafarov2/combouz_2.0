from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from web_site.models import Product


@api_view(['POST'])
def get_price_by_options(request):
    data = request.data
    product = Product.objects.filter(pk=data['product_id'])
    if not product.exists():
        return Response(status=status.HTTP_404_NOT_FOUND, data={
            'description': 'Product with id={} not found'.format(data['product_id'])
        })
    product = product.first()
    product_price = product.get_price(_format=False)

    cornice_price = product.uzs_cornice_type_price if data['cornice_type'] == 'aluminium' else product_price
    control_price = product.uzs_electrical_price if data['control_type'] == 'electro' else product_price

    width = int(''.join([i for i in data['width'] if i.isdigit()]))
    height = int(''.join([i for i in data['height'] if i.isdigit()]))
    decimal_size = (width / 100) * (height / 100)

    size_price = product_price
    if decimal_size < 0.5:
        size_price = int(product_price) / 2
    elif 0.5 < decimal_size < 1.0:
        size_price = product_price
    elif decimal_size > 1.0:
        size_price = decimal_size * product_price

    total_price = int(
        (size_price + (cornice_price - product_price) + (control_price - product_price)) * int(data['quantity'])
    )

    return Response(
        {
            'price': total_price
        }
    )

# 1 527 956
# 271 089
# {
#     "product_id": 4,
#     "width": "105см",
#     "height": "105см",
#     "quantity": 2,
#     "cornice_type": "plastic",
#     "control_type": "manual"
# }
