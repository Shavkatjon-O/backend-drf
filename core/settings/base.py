import environ

from pathlib import Path
from django.utils.translation import gettext_lazy as _

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "apps.calendars",
    "apps.chats",
    "apps.common",
    "apps.employees",
    "apps.events",
    "apps.projects",
    "apps.users",
    "apps.vacations",
]

THIRD_PARTY_APPS = [
    "drf_yasg",
    "rest_framework",
    "rest_framework_simplejwt",
    "rosetta",
    "corsheaders",
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

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
    "core.middlewares.ErrorHandlerMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"

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

TIME_ZONE = "Asia/Tashkent"

USE_L10N = True
USE_I18N = True
USE_TZ = True

LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
    ("uz", _("Uzbek")),
)
LOCALE_PATHS = (BASE_DIR / "locales/",)

STATICFILES_DIRS = (BASE_DIR / "staticfiles",)

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

JAZZMIN_SETTINGS = {
    "site_title": "CRM Backend Demo",
    "site_header": "CRM Backend Demo",
    "site_brand": "CRM Backend Demo",
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# EMAIL_HOST = env.str("EMAIL_HOST")
# EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = env.int("EMAIL_PORT")
# EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
# EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL")
