import requests as req
from accounts.forms import CustomUserAuthenticationForm, CustomUserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse, redirect, render

from combouz import settings

from .models import (
    Category,
    Client,
    Comment,
    Feedback,
    HeroGallery,
    Product,
    ProjectsGallery,
    Subcategory,
    Comment,
    CommentItem,
    Question,
)

# Create your views here.


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
    if category is None:
        products = Product.objects.all()
    else:
        products = category.products.all()

    paginator = Paginator(products, 1)
    page = request.GET.get("page")
    qs = paginator.get_page(page)

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
    context = {
        "registration_form": CustomUserCreationForm(),
        "login_form": CustomUserAuthenticationForm(),
        "products": products,
        "category": subcategory.category,
    }
    return render(request, "web_site/categories.html", context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    comments = product.comments.all()[0:2]
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
