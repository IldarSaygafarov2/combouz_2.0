import requests as req
from constance import config
from django.db.models import QuerySet
from django.shortcuts import redirect, render

from accounts.forms import CustomUserAuthenticationForm, CustomUserCreationForm
from combouz import settings
from web_site.models import Product
from .utils import CartForAnonymousUser, CartForAuthenticatedUser, get_cart_data
from .models import OrderProduct


DELIVERY_TYPES = {
    "takeaway": "Доставка курьером",
    "pickup": "Самовывоз - 0 сум",
    "install,size,delivery": "Установка, размер, доставка",
    "install,delivery": "Доставка и установка",
    "delivery-tashkent": "Доставка по городу Ташкент",
}


def __make_basket_products_msg(basket_data):
    return f"""

Дополнительные данные:

Фамилия: {basket_data['busket-surname']}
Имя: {basket_data['busket-name']}
Почта: {basket_data['busket-email']}
Номер телефона: {basket_data['busket-phone']}
Тип монтажа: {basket_data['busket-montage']}
Адрес: {basket_data['busket-address']}
Комментарий: {basket_data['busket-comment']}
Тип доставки: {DELIVERY_TYPES[basket_data['busket-delivery-type']]}
"""


def __make_basket_products_message(order_products: QuerySet[OrderProduct], basket_data):
    msg = ""
    for order_product in order_products:
        msg += f"""
Название продукта: {order_product.product.name}
Ширина: {order_product.product_selected_width}
Длина: {order_product.product_selected_height}
Управление: {order_product.product_selected_control}
Тип карниза: {order_product.product_selected_cornice_type}
Тип управления: {order_product.product_selected_control_type}
Количество: {order_product.quantity}
"""
    msg += __make_basket_products_msg(basket_data)
    return msg


# Create your views here.
def to_cart(request, product_id, action):
    if not request.user.is_authenticated:
        session_cart = CartForAnonymousUser(request, product_id, action)
    else:
        user_cart = CartForAuthenticatedUser(request, product_id, action)

    return redirect("cart:cart")


def basket_view(request):
    cart_info = get_cart_data(request)

    if request.method == "POST":
        basket_msg = __make_basket_products_message(cart_info['products'], request.POST)
        req.post(
            settings.CHANNEL_API_LINK.format(
                token=settings.BOT_TOKEN,
                channel_id=settings.CHANNEL_ID,
                text=basket_msg,
            )
        )
        cart_info["order"].delete()
        return redirect('cart')

    if request.user.is_authenticated:
        category = cart_info["products"].last()
        category = category.product.category if category else None
        last_product = cart_info["products"].last().product if category else None
    else:
        if cart_info["products"]:
            product = Product.objects.get(pk=cart_info["products"][-1]["product"]["pk"])
            category = product.category
            last_product = product
        else:
            category = ""
            last_product = ""

    context = {
        "cart_total_quantity": cart_info["cart_total_quantity"],
        "cart_total_price": cart_info["cart_total_price"],
        "cart_simple_total_price": cart_info["cart_simple_total_price"],
        "order": cart_info["order"],
        "products": cart_info["products"],
        "category": category,
        "last_product": last_product,
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "config": config
    }
    return render(request, "cart/basket.html", context)


def remove_from_cart(request, order_product_id):
    order_product = OrderProduct.objects.get(pk=order_product_id)
    order_product.product.quantity += order_product.quantity
    order_product.product.save()
    order_product.delete()

    return redirect('cart:cart')