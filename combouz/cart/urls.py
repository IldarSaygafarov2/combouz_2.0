from django.urls import path

from . import views

app_name = "cart"

urlpatterns = [
    path("", views.basket_view, name="cart"),
    path("to_cart/<int:product_id>/<str:action>/", views.to_cart, name="to_cart"),
]
