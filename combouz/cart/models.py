from django.db import models
from django.utils.translation import gettext as _

from accounts.models import CustomUser
from helpers.functions import format_price
from web_site.models import Product
from django.urls import reverse


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True
    )
    first_name = models.CharField(verbose_name=_("Имя"), max_length=150)
    last_name = models.CharField(verbose_name=_("Фамилия"), max_length=150)
    email = models.EmailField(verbose_name=_("Почта"))
    phone_number = models.CharField(verbose_name=_("Номер телефона"), max_length=15)
    mounting_type = models.CharField(verbose_name=_("Тип монтажа"), max_length=255)
    address = models.CharField(verbose_name=_("Адрес"), max_length=255)
    comment = models.CharField(
        verbose_name=_("Комментарий"), max_length=1000, default=""
    )
    delivery_type = models.CharField(verbose_name=_("Тип доставки"), max_length=150)
    delivery_option = models.CharField(
        verbose_name=_("Вариант доставки"),
        max_length=150,
        default="",
    )

    def __str__(self):
        return self.first_name


class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    @property
    def get_cart_total_price(self):
        order_products = self.orderproduct_set.all()
        total = sum([item.get_total_price(_format=False) for item in order_products])
        return format_price(total)

    @property
    def get_simple_total_price(self):
        order_products = self.orderproduct_set.all()
        total = sum([item.get_total_price(_format=False) for item in order_products])
        return total

    @property
    def get_cart_total_quantity(self):
        order_products = self.orderproduct_set.all()
        return sum([item.quantity for item in order_products])


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="order_products")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    product_selected_width = models.PositiveIntegerField(default=0, null=True)
    product_selected_height = models.PositiveIntegerField(default=0, null=True)
    product_selected_control = models.CharField(default='', blank=True, max_length=150, null=True)
    product_selected_cornice_type = models.CharField(default='', blank=True, max_length=150, null=True)
    product_selected_control_type = models.CharField(default='', blank=True, max_length=150, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def remove_from_cart(self):
        return reverse(
            'cart:remove',
            kwargs={'order_product_id': self.pk}
        )

    # @property
    def get_total_price(self, _format=True):

        width = self.product_selected_width
        height = self.product_selected_height

        decimal_size = (width / 100) * (height / 100)
        product_price = self.product.get_price(_format=False)

        size_price = product_price

        if decimal_size < 0.5:
            size_price = int(product_price) / 2
        elif 0.5 < decimal_size < 1.0:
            size_price = product_price
        elif decimal_size > 1.0:
            size_price = decimal_size * product_price

        control_price = self.product.get_electrical_price()
        cornice_price = self.product.get_cornice_type_price()

        if not self.product_selected_control_type:
            control_price = 0
        if not self.product_selected_cornice_type:
            cornice_price = 0

        total = int((size_price + control_price + cornice_price) * self.quantity)
        if not self.product.discount:
            return total
        if not _format:
            return total

        return format_price(total)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'
