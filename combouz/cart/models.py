from accounts.models import CustomUser
from django.db import models
from helpers.functions import format_price
from web_site.models import Product


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True
    )
    first_name = models.CharField(verbose_name="Имя", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150)
    email = models.EmailField(verbose_name="Почта")
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15)
    mounting_type = models.CharField(verbose_name="Тип монтажа", max_length=255)
    address = models.CharField(verbose_name="Адрес", max_length=255)
    comment = models.CharField(verbose_name="Комментарий", max_length=1000, default="")
    delivery_type = models.CharField(verbose_name="Тип доставки", max_length=150)
    delivery_option = models.CharField(
        verbose_name="Вариант доставки",
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
        total = sum([item.get_total_price for item in order_products])
        return format_price(total)
        # return total

    @property
    def get_cart_total_quantity(self):
        order_products = self.orderproduct_set.all()
        return sum([item.quantity for item in order_products])


class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="order_products"
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        return int(self.product.uzs_price) * self.quantity