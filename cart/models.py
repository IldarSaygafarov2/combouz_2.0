from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import CustomUser
from helpers.functions import format_price, calculate_price
from web_site.models import Product


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
        total_price = calculate_price(
            obj=Product,
            product_id=self.product.pk,
            cornice_type=self.product_selected_cornice_type,
            control_type=self.product_selected_control_type,
            width=self.product_selected_width,
            height=self.product_selected_height,
            quantity=self.quantity
        )
        return total_price

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'

# 1 239 946
# 2 975 870
