from constance import config
from django.shortcuts import render

from .models import Article


def blog_articles(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
        "config": config
    }
    return render(request, "blog/index.html", context)


def blog_article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        "article": article,
        "config": config
    }
    return render(request, "blog/article_detail.html", context)

