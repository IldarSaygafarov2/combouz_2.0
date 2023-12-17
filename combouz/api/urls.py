from django.urls import path

from . import views

urlpatterns = [
    path('get_something/', views.get_something)
]
