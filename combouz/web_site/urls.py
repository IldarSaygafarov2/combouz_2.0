from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("contacts/", views.contacts_view, name="contacts"),
    path("portfolio/", views.portfolio_view, name="portfolio"),
    path("portfolio/<slug:slug>/", views.portfolio_detail_view, name="portfolio_detail"),
    path(
        "categories/<slug:subcategory_slug>/",
        views.subcategory_products,
        name="subcategory_detail",
    ),
    path("products/<slug:product_slug>/", views.product_detail, name="product_detail"),
    path("send_email/", views.send_phone_number_to_telegram, name="send_email"),
    path('reviews/', views.reviews_view, name="reviews"),

    path('sizes/', views.get_sizes, name='sizes')
]
