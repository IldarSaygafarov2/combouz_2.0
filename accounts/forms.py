from accounts.models import CustomUser
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label="Почта",
        widget=forms.EmailInput(
            attrs={
                "class": "modal__form-input",
                "placeholder": "Your email",
                "name": "user-email",
                "autocomplete": "email",
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "modal__form-input modal__form-password",
                "placeholder": "password",
                "name": "user-password",
            }
        ),
    )

    class Meta:
        model = CustomUser
        # fields = ("email", "password")


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Почта",
        widget=forms.EmailInput(
            attrs={
                "class": "modal__form-input",
                "placeholder": "Your email",
                "name": "user-email",
                "autocomplete": "email",
            }
        ),
    )
    phone_number = forms.CharField(
        label="Номер телефона",
        widget=forms.NumberInput(
            attrs={
                "class": "modal__form-input",
                "placeholder": "Your phone number",
                "name": "user-phone",
            }
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "modal__form-input modal__form-password",
                "placeholder": "password",
                "name": "user-password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "modal__form-input modal__form-password-rep",
                "placeholder": "Repeat password",
                "name": "user-password-repeat",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("email", "phone_number", "password1", "password2")
