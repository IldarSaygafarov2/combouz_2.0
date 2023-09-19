import requests as req
from accounts.forms import CustomUserAuthenticationForm, CustomUserCreationForm
from django.shortcuts import HttpResponse, redirect, render

from combouz import settings

from .models import Category, Client, Feedback, HeroGallery, Product, ProjectsGallery

# Create your views here.


def home_view(request):
    slides = HeroGallery.objects.all()
    projects = enumerate(ProjectsGallery.objects.all(), start=1)
    home_categories = Category.objects.filter(show_on_homepage=True)
    bestsellers = Category.objects.filter(make_bestseller=True).first()
    reviews = Feedback.objects.all()
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "slides": slides,
        "projects": projects,
        "reviews": reviews,
        "home_categories": home_categories,
        "bestsellers": bestsellers,
    }
    return render(request, "web_site/index.html", context)


def about_view(request):
    projects = ProjectsGallery.objects.all()
    clients = Client.objects.all()
    context = {
        "projects": projects,
        "clients": clients,
    }
    return render(request, "web_site/about.html", context)


def contacts_view(request):
    return render(request, "web_site/contacts.html")


def portfolio_view(request):
    projects = enumerate(ProjectsGallery.objects.all(), start=1)
    context = {
        "projects": projects,
    }
    return render(request, "web_site/portfolio.html", context)


def category_products(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = category.products.all()
    context = {
        "products": products,
        "category": category,
    }
    return render(request, "web_site/categories.html", context)


def subcategory_products(request, subcategory_slug):
    return render(request, "web_site/categories.html")


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        "product": product,
    }
    return render(request, "web_site/product_detail.html", context)


def send_phone_number_to_telegram(request):
    phone_number = request.POST.get("phone_number")
    msg = f"Оставленный номер телефона: {phone_number}"
    req.post(
        settings.CHANNEL_API_LINK.format(
            token=settings.BOT_TOKEN, channel_id=settings.CHANNEL_ID, text=msg
        )
    )

    return redirect("home")
