from rest_framework.decorators import api_view
from rest_framework.response import Response
from helpers.functions import calculate_price
from web_site.models import Product


@api_view(['POST'])
def get_price_by_options(request):

    data = request.data

    total_price = calculate_price(
        Product,
        product_id=data['product_id'],
        cornice_type=data['cornice_type'],
        control_type=data['control_type'],
        width=data['width'],
        height=data['height'],
        quantity=data['quantity']
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
