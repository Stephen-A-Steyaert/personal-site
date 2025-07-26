from .base import *
from personal_site.settings import get_secret

SECRET_KEY = get_secret("SECRET_KEY", "")

DEBUG = False
raw_hosts = get_secret("ALLOWED_HOSTS", "")
ALLOWED_HOSTS = [host.strip() for host in raw_hosts.split(",") if host.strip()]



DATABASES = {
    "default": {
        'ENGINE': f"django.db.backends.{get_secret("DATABASE_ENGINE", "sqlite3")}",
        'NAME': get_secret("DATABASE_NAME", "personalsite"),
        'USER':get_secret("DATABASE_USERNAME", 'ss'),
        'PASSWORD':get_secret('DATABASE_PASSWORD', "ss"),
        'HOST':get_secret('DATABASE_HOST', 'db'),
        'PORT':get_secret("DATABASE_PORT", 5432)
    }
}


SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


# Static Files URL
STATIC_URL = "cdn.basedomain/static/"

# Media Files URL
MEDIA_URL = "cdn.basedomain/media/"
