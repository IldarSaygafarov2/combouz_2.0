from django.urls import path

from . import views


app_name = "blog"

urlpatterns = [
    path('', views.blog_articles, name="blog"),
    path('<slug:slug>/', views.blog_article_detail, name="article_detail")
]
