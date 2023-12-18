from django.urls import path

from . import views

urlpatterns = [
    # path('get_something/', views.get_something),
    path('get_price/', views.get_price_by_options)
]
