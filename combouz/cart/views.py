from django.shortcuts import render, redirect
from web_site.models import Product
from .utils import CartForAnonymousUser, CartForAuthenticatedUser, get_cart_data


# Create your views here.
def to_cart(request, product_id, action):
    product = Product.objects.get(pk=product_id)
    # product_msg = __make_product_variant_msg(request.POST)

    # obj = MessageTelegram.objects.create(product=product, product_msg=product_msg)
    # obj.save()

    if not request.user.is_authenticated:
        session_cart = CartForAnonymousUser(request, product_id, action)
    else:
        user_cart = CartForAuthenticatedUser(request, product_id, action)

    return redirect("cart")


def basket_view(request):
    cart_info = get_cart_data(request)

    # if request.method == "POST":
    #     basket_msg = __make_basket_products_msg(request.POST)

    #     for product in cart_info["products"]:
    #         if request.user.is_authenticated:
    #             message_tg = MessageTelegram.objects.filter(
    #                 product_id=product.product.pk
    #             )
    #         else:
    #             message_tg = MessageTelegram.objects.filter(product_id=product["pk"])

    #         basket_msg += "".join(
    #             [
    #                 message_tg_obj.product_msg
    #                 for message_tg_obj in message_tg
    #                 if message_tg_obj.product_msg
    #             ]
    #         )

    #         basket_msg += f"Продукт: {product.product.name}"
    #         req.post(
    #             settings.CHANNEL_API_LINK.format(
    #                 token=settings.BOT_TOKEN,
    #                 channel_id=settings.CHANNEL_ID,
    #                 text=basket_msg,
    #             )
    #         )

    # category = cart_info["products"].last()
    # category = category.product.category if category else None
    # last_product = cart_info["products"].last().product if category else None
    context = {
        "cart_total_quantity": cart_info["cart_total_quantity"],
        "cart_total_price": cart_info["cart_total_price"],
        "order": cart_info["order"],
        "products": cart_info["products"],
        # "category": category,
        # "last_product": last_product,
    }
    return render(request, "cart/basket.html", context)
