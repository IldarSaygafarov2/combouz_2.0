from combouz import settings

from .models import Customer, Order, OrderProduct, Product


class CartForAuthenticatedUser:
    def __init__(self, request, product_id=None, action=None):
        self.user = request.user

        if action == "delete_product":
            self.delete_order_product(product_id)

        if product_id and action:
            self.add_or_delete(product_id, action)

    def get_cart_info(self):
        customer, created = Customer.objects.get_or_create(user=self.user)
        order, created = Order.objects.get_or_create(user=customer)
        order_products = order.orderproduct_set.all()
        cart_total_quantity = order.get_cart_total_quantity
        cart_total_price = order.get_cart_total_price
        print(cart_total_price)

        return {
            "cart_total_quantity": cart_total_quantity,
            "cart_total_price": cart_total_price,
            "order": order,
            "products": order_products,
        }

    def add_or_delete(self, product_id, action):
        order = self.get_cart_info()["order"]
        product = Product.objects.get(pk=product_id)
        order_product, created = OrderProduct.objects.get_or_create(
            order=order, product=product
        )

        if action == "add" and product.quantity > 0:
            order_product.quantity += 1  # +1 в корзину
            product.quantity -= 1  # -1 со склада
        else:
            order_product.quantity -= 1
            product.quantity += 1
        product.save()
        order_product.save()

        if order_product.quantity <= 0:
            order_product.delete()

    def delete_order_product(self, product_id):
        order = self.get_cart_info()["order"]
        product = Product.objects.get(pk=product_id)

        order_product = OrderProduct.objects.get(order=order, product=product)

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
        order = {"get_cart_total_price": 0, "get_cart_total_quantity": 0}
        cart_total_quantity = order["get_cart_total_quantity"]
        cart_total_price = order["get_cart_total_price"]
        for key in self.cart:
            if self.cart[key]["quantity"] > 0:
                product_quantity = self.cart[key]["quantity"]
                cart_total_quantity += product_quantity
                product = Product.objects.get(pk=key)
                get_total_price = product.price * product_quantity

                cart_product = {
                    "pk": product.pk,
                    "product": {
                        "pk": product.pk,
                        "name": product.name,
                        "price": product.price,
                        "get_first_photo": product.get_first_photo(),
                        "quantity": product.quantity,
                        "get_absolute_url": product.get_absolute_url(),
                    },
                    "quantity": product_quantity,
                    "get_total_price": get_total_price,
                }
                products.append(cart_product)
                order["get_cart_total_price"] += cart_product["get_total_price"]
                order["get_cart_total_quantity"] += cart_product["quantity"]
                cart_total_price = order["get_cart_total_price"]

        self.save()

        return {
            "cart_total_quantity": cart_total_quantity,
            "cart_total_price": cart_total_price,
            "order": order,
            "products": products,
        }

    def add(self):
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
        "order": cart_info["order"],
        "products": cart_info["products"],
    }
