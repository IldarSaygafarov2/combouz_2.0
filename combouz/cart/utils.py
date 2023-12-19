from combouz import settings

from .models import Customer, Order, OrderProduct, Product


def _convert_to_int(data):
    if not data:
        return 0
    return int(''.join([i for i in data if i.isdigit()]))


class CartForAuthenticatedUser:
    def __init__(self, request, product_id=None, action=None):
        self.user = request.user
        self.request = request

        if action == "delete_product":
            self.delete_order_product(product_id)

        if product_id and action:
            self.add_or_delete(product_id, action)

    def _get_product_options(self):
        selected_width = self.request.POST.get('item-width')
        selected_height = self.request.POST.get('item-length')
        selected_control = self.request.POST.get('item-control')
        selected_cornice_type = self.request.POST.get('item-cornice-type')
        selected_control_type = self.request.POST.get('item-control-type')

        return {
            "product_selected_width": _convert_to_int(selected_width),
            "product_selected_height": _convert_to_int(selected_height),
            "product_selected_control": selected_control,
            "product_selected_cornice_type": selected_cornice_type,
            "product_selected_control_type": selected_control_type,
        }

    def get_cart_info(self):
        customer, created = Customer.objects.get_or_create(user=self.user)
        order, created = Order.objects.get_or_create(user=customer)
        order_products = order.orderproduct_set.all()
        cart_total_quantity = order.get_cart_total_quantity
        cart_total_price = order.get_cart_total_price
        cart_simple_total_price = order.get_simple_total_price

        return {
            "cart_total_quantity": cart_total_quantity,
            "cart_total_price": cart_total_price,
            "cart_simple_total_price": cart_simple_total_price,
            "order": order,
            "products": order_products,
        }

    def add_or_delete(self, product_id, action):
        order = self.get_cart_info()["order"]
        product = Product.objects.get(pk=product_id)
        options = self._get_product_options()
        qty = self.request.POST.get('item-count')

        print(options)

        order_product, created = OrderProduct.objects.get_or_create(
            order=order,
            product=product,
            **self._get_product_options()
        )

        if action == "add" and product.quantity > 0:
            order_product.product_selected_width = options.get('product_selected_width')
            order_product.product_selected_height = options.get('product_selected_height')
            if not qty:
                order_product.quantity += 1  # +1 в корзину
                product.quantity -= 1  # -1 со склада
            else:
                order_product.quantity += int(qty)  # +1 в корзину
                product.quantity -= int(qty)  # -1 со склада
        else:
            if not qty:
                order_product.quantity -= 1
                product.quantity += 1
            else:
                order_product.quantity -= int(qty)
                product.quantity += int(qty)
        product.save()
        order_product.save()

        if order_product.quantity <= 0:
            order_product.delete()

    def delete_order_product(self, product_id):
        order = self.get_cart_info()["order"]
        product = Product.objects.get(pk=product_id)

        order_product = OrderProduct.objects.get(order=order, product=product)

        # возвращаем продукту то количество, которое было удалено из корзины
        product.quantity = order_product.quantity
        product.save()

        order_product.delete()
        order.save()

    def clear(self):
        order = self.get_cart_info()["order"]
        order_products = order.orderproduct_set.all()
        for product in order_products:
            product.delete()
        order.save()


class CartForAnonymousUser:
    def __init__(self, request, product_id=None, action=None):
        self.session = request.session
        self.request = request
        self.cart = self.get_cart()

        if product_id and action:
            self.key = str(product_id)
            self.product = Product.objects.get(pk=product_id)
            self.cart_product = self.cart.get(self.key)

            if action == "add" and self.product.quantity > 0:
                self.add()
            elif action == "delete":
                self.delete()

            self.product.save()
            self.save()

    def get_cart(self):
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session["cart"] = {}
        return cart

    def save(self):
        self.session.modified = True

    def get_cart_info(self):
        products = []
        order = {
            "get_cart_total_price": 0,
            "get_cart_total_quantity": 0,
            "get_cart_simple_total_price": 0
        }
        cart_total_quantity = order["get_cart_total_quantity"]
        cart_total_price = order["get_cart_total_price"]
        cart_simple_total_price = order["get_cart_simple_total_price"]
        for key in self.cart:
            if self.cart[key]["quantity"] > 0:
                product_quantity = self.cart[key]["quantity"]
                cart_total_quantity += product_quantity
                product = Product.objects.get(pk=key)
                get_total_price = product.get_price(_format=False) * product_quantity

                cart_product = {
                    "pk": product.pk,
                    "product": {
                        "pk": product.pk,
                        "name": product.name,
                        "uzs_price": product.get_price(_format=False),
                        "get_price": product.get_price(_format=False),
                        "get_price_with_discount": product.get_price_with_discount(_format=False),
                        "get_first_photo": product.get_first_img(),
                        "quantity": product.quantity,
                        "get_absolute_url": product.get_absolute_url(),
                        "add_to_cart": product.add_to_cart(),
                        "remove_from_cart": product.remove_from_cart(),
                    },
                    "quantity": product_quantity,
                    "get_total_price": get_total_price,
                }
                products.append(cart_product)
                order["get_cart_total_price"] += cart_product["get_total_price"]
                order["get_cart_simple_total_price"] += cart_product["get_total_price"]
                order["get_cart_total_quantity"] += cart_product["quantity"]
                cart_total_price = order["get_cart_total_price"]
                cart_simple_total_price = order["get_cart_simple_total_price"]

        self.save()

        return {
            "cart_total_quantity": cart_total_quantity,
            "cart_total_price": cart_total_price,
            "cart_simple_total_price": cart_simple_total_price,
            "order": order,
            "products": products,
        }

    def add(self):
        print(self.request.POST)
        if self.cart_product:
            self.cart_product["quantity"] += 1
        else:
            self.cart[self.key] = {"quantity": 1}
        self.product.quantity -= 1

    def delete(self):
        self.cart_product["quantity"] -= 1
        self.product.quantity += 1

        if self.cart_product["quantity"] <= 0:
            del self.cart[self.key]

    # def remove_from_cart(self):
    #     del self.cart[self.key]

    def clear(self):
        self.cart = {}


def get_cart_data(request):
    if request.user.is_authenticated:
        user_cart = CartForAuthenticatedUser(request)
        cart_info = user_cart.get_cart_info()
    else:
        session_cart = CartForAnonymousUser(request)
        cart_info = session_cart.get_cart_info()

    return {
        "cart_total_quantity": cart_info["cart_total_quantity"],
        "cart_total_price": cart_info["cart_total_price"],
        "cart_simple_total_price": cart_info["cart_simple_total_price"],
        "order": cart_info["order"],
        "products": cart_info["products"],
    }
