from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import CustomUserAuthenticationForm, CustomUserCreationForm


# Create your views here.
def user_login(request):
    form = CustomUserAuthenticationForm(data=request.POST)
    if form.is_valid():
        email = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    else:
        print(form.errors)
    return redirect("home")


def user_registration(request):
    form = CustomUserCreationForm(data=request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = form.cleaned_data["email"].split("@")[0]
        user.save()
        return redirect("home")
    return redirect("home")


def user_logout(request):
    logout(request)
    return redirect("home")
