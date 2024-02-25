import os
from collections import OrderedDict
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-3ne8dybq!dxbz3da9=4ss9##z=h0n!i=a51fdt$0@+vd$66l&^"

DEBUG = True

ALLOWED_HOSTS = [
    "combouz.pythonanywhere.com",
    "127.0.0.1"
]

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "jazzmin",
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'rest_framework',

    "django_dump_load_utf8",
    "django.contrib.sites",

    "accounts.apps.AccountsConfig",
    "web_site.apps.WebSiteConfig",
    "cart.apps.CartConfig",
    "blog.apps.BlogConfig",
    "api.apps.ApiConfig",


    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",

    "ckeditor",
    "ckeditor_uploader",
    "constance",
    "debug_toolbar",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "combouz.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "combouz.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

BOT_TOKEN = "6651100598:AAE0CSIZJ4D9JX-DRnGk_qTYdJ2WX-bzrb8"
CHANNEL_ID = -1001965630465
CHANNEL_API_LINK = (
    "https://api.telegram.org/bot{token}/sendMessage?chat_id={channel_id}&text={text}"
)
CART_SESSION_ID = "cart"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 28
ACCOUNT_UNIQUE_EMAIL = False
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = "/"
SITE_ID = 1
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

JAZZMIN_SETTINGS = {
    "site_title": "Combouz Admin",
    "site_header": "Combouz",
    "site_brand": "Combouz",
    "site_logo": None,
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome",
    "copyright": "Creitive Agency",
    "search_model": ["auth.User", "auth.Group"],
    "user_avatar": None,

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {
            "name": "Support",
            "url": "https://github.com/farridav/django-jazzmin/issues",
            "new_window": True,
        },
        {"model": "auth.User"},
        {"app": "app"},
    ],

    "usermenu_links": [
        {
            "name": "Support",
            "url": "https://github.com/farridav/django-jazzmin/issues",
            "new_window": True,
        },
        {"model": "auth.user"},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth"],
    "custom_links": {},
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,

    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": True,
}

gettext = lambda s: s
LANGUAGES = (
    ("ru", gettext("Russia")),
    ("uz", gettext("Uzbek")),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_DATABASE_PREFIX = "constance:core:"

CONSTANCE_CONFIG = OrderedDict([
    ("EMAIL", ("info@combo.uz", "Почта для связи")),
    ("PHONE_NUMBER", ("+998 (95) 142 - 33 - 13", "Номер для связи")),
    ("OFFICE_ADDRESS", ("г.Ташкент, Алмазарский район, ул.Сагбан 37/1", "Локация офиса")),
    ("WORKING_TIME", ("с 9:00 до 19:00", "Режим работы")),
    ("CALLING_TIME", ("с 8:00 до 20:00", "Режим звонков")),
    ("ADVANTAGE_1", ("", "Первое преимущество")),
    ("ADVANTAGE_2", ("", "Второе преимущество")),
    ("ADVANTAGE_3", ("", "Третье преимущество")),
    ("ABOUT_PAGE_TITLE", ("", "Заголовок страницы 'О компании'")),
    ("ABOUT_PAGE_DESCRIPTION", ("", "Описание страницы 'О компании'")),
    ("PRODUCTS_ON_PAGE", (3, "Количество продуктов на странице")),
    ("SHOW_SLIDER", (True, "Скрыть/показать слайдер на главной странице")),
    ("CONTACTS_PAGE_DESCRIPTION", ("", "Описание страницы 'Контакты'")),
    ("PICKUP_DISCOUNT", (0, "Размер скидки для самовывоза"))
])

CONSTANCE_CONFIG_FIELDSETS = {
    "Общие данные": (
        "EMAIL",
        "PHONE_NUMBER",
        "OFFICE_ADDRESS",
        "WORKING_TIME",
        "CALLING_TIME",
        "PRODUCTS_ON_PAGE",
        "SHOW_SLIDER",
        "PICKUP_DISCOUNT"
    ),
    "Страница 'О компании'": ("ABOUT_PAGE_TITLE", "ABOUT_PAGE_DESCRIPTION", "ADVANTAGE_1", "ADVANTAGE_2", "ADVANTAGE_3"),
    "Страница 'Контакты'": ("CONTACTS_PAGE_DESCRIPTION",)
}

CKEDITOR_UPLOAD_PATH = "uploads/"


# FACEBOOK LOGIN SETTINGS
ACCOUNT_EMAIL_VERIFICATION = 'none'
CORS_ALLOW_ALL_ORIGINS = True

SMS_API_KEY = os.getenv('SMS_API_KEY')
SMS_SENDER = 'Combouz'
SMS_HOST = 'qyypgm.api.infobip.com'

