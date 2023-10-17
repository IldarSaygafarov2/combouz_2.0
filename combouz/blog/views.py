from django.shortcuts import render, HttpResponse

from .models import Article


def blog_articles(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "blog/index.html", context)


def blog_article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        "article": article
    }
    return render(request, "blog/article_detail.html", context)

