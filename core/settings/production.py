from core.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    "crm-backend-demo.falconsoft.uz",
]

CSRF_TRUSTED_ORIGINS = [
    "crm-backend-demo.falconsoft.uz",
]
CSRF_COOKIE_SECURE = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASS"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}

LOGGER_BOT_TOKEN = env.str("LOGGER_BOT_TOKEN")
LOGGER_CHAT_ID = env.str("LOGGER_CHAT_ID")

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]
