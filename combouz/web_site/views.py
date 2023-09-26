import requests as req
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from accounts.forms import CustomUserAuthenticationForm, CustomUserCreationForm
from combouz import settings
from .models import (
    Category,
    Client,
    Feedback,
    HeroGallery,
    Product,
    ProjectsGallery,
    Subcategory,
    Comment,
    CommentItem,
    Question,
    ProductColorItem,
)


def __create_paginated_products(request, qs):
    paginator = Paginator(qs, 3)
    page = request.GET.get("page")
    qs = paginator.get_page(page)
    return qs


def home_view(request):
    slides = HeroGallery.objects.all()
    projects = enumerate(ProjectsGallery.objects.all(), start=1)
    home_categories = Category.objects.filter(show_on_homepage=True)
    bestsellers = Category.objects.filter(make_bestseller=True).first()
    reviews = Feedback.objects.all()
    videos = Question.objects.all()
    correct_videos = [
        video.video_link.replace("youtu.be", "www.youtube.com/embed")
        for video in videos
    ]
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "slides": slides,
        "projects": projects,
        "reviews": reviews,
        "home_categories": home_categories,
        "bestsellers": bestsellers,
        "videos": correct_videos,
    }
    return render(request, "web_site/index.html", context)


def about_view(request):
    projects = ProjectsGallery.objects.all()
    clients = Client.objects.all()
    context = {
        "projects": projects,
        "clients": clients,
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
    }
    return render(request, "web_site/about.html", context)


def contacts_view(request):
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
    }
    return render(request, "web_site/contacts.html", context)


def portfolio_view(request):
    projects = enumerate(ProjectsGallery.objects.all(), start=1)
    context = {
        "projects": projects,
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
    }
    return render(request, "web_site/portfolio.html", context)


def category_products(request, category_slug):
    category = Category.objects.filter(slug=category_slug).first()
    sort = request.GET.get("sort")

    if category is None:
        products = Product.objects.all()
    else:
        products = category.products.all()

    if sort:
        qs = __create_paginated_products(request, products.order_by(sort))
    else:
        qs = __create_paginated_products(request, products)

    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "products": qs,
        "category": category,
    }
    return render(request, "web_site/categories.html", context)


def subcategory_products(request, subcategory_slug):
    subcategory = Subcategory.objects.get(slug=subcategory_slug)
    products = subcategory.products.all()
    qs = __create_paginated_products(request, products)
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "products": qs,
        "category": subcategory.category,
    }
    return render(request, "web_site/categories.html", context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    next_num = request.GET.get('next')
    comments_total = product.comments.count()
    comments = product.comments.all()[0:2]

    if next_num:
        next_num = int(next_num)
        comments = product.comments.all()[:next_num + next_num]

    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist("img")

        comment = Comment.objects.create(
            author=request.user,
            product=product,
            body=data["user-comment"],
        )
        comment.save()

        for image in images:
            comment_item = CommentItem.objects.create(comment=comment, img=image)
            comment_item.save()
        return redirect("product_detail", product_slug=product_slug)
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "comments": comments,
        "product": product,
        "comments_total": comments_total
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


def sort_products_by_color(request, color):
    color_obj = ProductColorItem.objects.get(color=color)
    products = Product.objects.filter(color=color_obj)

    qs = __create_paginated_products(request, products)

    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "products": qs,
    }
    return render(request, "web_site/categories.html", context)


def sort_products_by_dimming(request, dimming):
    products = Product.objects.filter(dimming=dimming)
    qs = __create_paginated_products(request, products)
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "products": qs,
    }
    return render(request, "web_site/categories.html", context)


def sort_products_by_country(request, country):
    products = Product.objects.filter(manufacturer_country=country)
    qs = __create_paginated_products(request, products)
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "products": qs,
    }
    return render(request, "web_site/categories.html", context)
