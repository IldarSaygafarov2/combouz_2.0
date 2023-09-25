import requests as req
from accounts.forms import CustomUserAuthenticationForm, CustomUserCreationForm
from django.shortcuts import redirect, render
from web_site.models import Product

from combouz import settings

from .utils import CartForAnonymousUser, CartForAuthenticatedUser, get_cart_data

DELIVERY_TYPES = {
    "takeaway": "Доставка курьером",
    "pickup": "Самовывоз - 0 сум",
    "install,size,delivery": "Установка, размер, доставка",
    "install,delivery": "Доставка и установка",
    "delivery-tashkent": "Доставка по городу Ташкент",
}


def __make_basket_products_msg(basket_data):
    return f"""
Вариант Доставки: {DELIVERY_TYPES[basket_data['busket-delivery']]}
Фамилия: {basket_data['busket-surname']}
Имя: {basket_data['busket-name']}
Почта: {basket_data['busket-email']}
Номер телефона: {basket_data['busket-phone']}
Тип монтажа: {basket_data['busket-montage']}
Адрес: {basket_data['busket-address']}
Комментарий: {basket_data['busket-comment']}
Тип доставки: {DELIVERY_TYPES[basket_data['busket-delivery-type']]}
"""


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
        basket_msg = __make_basket_products_msg(request.POST)
        product_names = ""
        for product in cart_info["products"]:
            product_names += f"Продукт: {product.product.name}\n"

        product_names += basket_msg
        req.post(
            settings.CHANNEL_API_LINK.format(
                token=settings.BOT_TOKEN,
                channel_id=settings.CHANNEL_ID,
                text=product_names,
            )
        )
    if request.user.is_authenticated:
        category = cart_info["products"].last()
        category = category.product.category if category else None
        last_product = cart_info["products"].last().product if category else None
    else:
        product = Product.objects.get(pk=cart_info["products"][-1]["product"]["pk"])
        category = product.category
        last_product = product
    context = {
        "cart_total_quantity": cart_info["cart_total_quantity"],
        "cart_total_price": cart_info["cart_total_price"],
        "order": cart_info["order"],
        "products": cart_info["products"],
        "category": category,
        "last_product": last_product,
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
    }
    return render(request, "cart/basket.html", context)
