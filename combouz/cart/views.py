from django.shortcuts import render, redirect
from web_site.models import Product
from .utils import CartForAnonymousUser, CartForAuthenticatedUser, get_cart_data


# Create your views here.
def to_cart(request, product_id, action):
    if not request.user.is_authenticated:
        session_cart = CartForAnonymousUser(request, product_id, action)
    else:
        user_cart = CartForAuthenticatedUser(request, product_id, action)

    return redirect("cart:cart")


def basket_view(request):
    cart_info = get_cart_data(request)
    context = {
        "cart_total_quantity": cart_info["cart_total_quantity"],
        "cart_total_price": cart_info["cart_total_price"],
        "order": cart_info["order"],
        "products": cart_info["products"],
        # "category": category,
        # "last_product": last_product,
    }
    return render(request, "cart/basket.html", context)
