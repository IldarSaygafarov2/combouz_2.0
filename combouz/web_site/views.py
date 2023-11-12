import requests as req
from constance import config
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from accounts.forms import CustomUserAuthenticationForm, CustomUserCreationForm
from blog.models import Article
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
    ProductDimming,
    ImagesOnAboutPage,
    SocialItem,
    Collection,
    ProductManufacturerCountry
)


def __create_paginated_products(request, qs):
    paginator = Paginator(qs, config.PRODUCTS_ON_PAGE)
    page = request.GET.get("page")
    qs = paginator.get_page(page)
    return qs


def home_view(request):
    slides = HeroGallery.objects.all()
    projects = enumerate(ProjectsGallery.objects.all(), start=1)
    home_categories = Category.objects.all()
    reviews = Feedback.objects.all()
    videos = Question.objects.all()
    articles = Article.objects.all()
    social_items = SocialItem.objects.all()
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
        "videos": correct_videos,
        "articles": articles,
        "social_items": social_items
    }
    return render(request, "web_site/index.html", context)


def about_view(request):
    clients = Client.objects.all()
    about_images = ImagesOnAboutPage.objects.all()

    context = {
        "about_images": about_images,
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
    projects = ProjectsGallery.objects.all()
    context = {
        "projects": projects,
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
    }
    return render(request, "web_site/portfolio.html", context)


def portfolio_detail_view(request, slug):
    project = ProjectsGallery.objects.get(slug=slug)
    context = {
        "project": project,
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
    }
    return render(request, "web_site/portfolio_detail.html", context)


def subcategory_products(request, subcategory_slug):
    subcategory = Subcategory.objects.get(slug=subcategory_slug)

    query = request.GET

    if "color" in query:
        color_obj = ProductColorItem.objects.get(color=query.get("color"))
        products = Product.objects.filter(color=color_obj)
    elif "dimming" in query:
        dimming_obj = ProductDimming.objects.get(dimming=query.get("dimming"))
        products = Product.objects.filter(dimming=dimming_obj)
    elif "country" in query:
        country_obj = ProductManufacturerCountry.objects.get(name=query.get("country"))
        products = Product.objects.filter(manufacturer_country=country_obj)
    elif "collection" in query:
        collection = Collection.objects.get(name=query.get("collection"))
        products = collection.products.all()
    else:
        products = subcategory.products.all()

    if "sort" in query:
        products = products.order_by(query.get("sort"))

    qs = __create_paginated_products(request, products)
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "products": qs,
        "subcategory": subcategory
    }
    return render(request, "web_site/categories.html", context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    category = product.category

    next_num = request.GET.get("next")
    comments_total = product.comments.count()
    comments = product.comments.all()[0:2]

    if next_num:
        next_num = int(next_num)
        comments = product.comments.all()[: next_num + next_num]

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
        "comments_total": comments_total,
        "category": category,
        "subcategory": product.subcategory
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
    dimming_obj = ProductDimming.objects.get(dimming=dimming)
    products = Product.objects.filter(dimming=dimming_obj)
    qs = __create_paginated_products(request, products)
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "products": qs,
    }
    return render(request, "web_site/categories.html", context)


def sort_products_by_country(request, country_id):
    products = Product.objects.filter(manufacturer_country=country_id)
    qs = __create_paginated_products(request, products)
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "products": qs,
    }
    return render(request, "web_site/categories.html", context)


def reviews_view(request):
    reviews = Feedback.objects.all()
    context = {
        "reviews": reviews,
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
    }
    return render(request, "web_site/reviews.html", context)
