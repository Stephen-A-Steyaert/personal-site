from .base import *
from personal_site.settings import get_secret
from personal_site.settings.types import Databases
from typing import Optional

SECRET_KEY: Optional[str] = get_secret("SECRET_KEY", "")

DEBUG: bool = False

raw_hosts: Optional[str] = get_secret("ALLOWED_HOSTS", "")
ALLOWED_HOSTS: list[str] = [host.strip() for host in (raw_hosts or "").split(",") if host.strip()]

port_str = get_secret("DATABASE_PORT", "5432")

if port_str:
    port = int(port_str)
else:
    port = 5432

DATABASES: Databases = {
    "default": {
        "ENGINE": f"django.db.backends.{get_secret('DATABASE_ENGINE', 'sqlite3')}",
        "NAME": get_secret("DATABASE_NAME", "personalsite"),
        "USER": get_secret("DATABASE_USERNAME", "ss"),
        "PASSWORD": get_secret("DATABASE_PASSWORD", "ss"),
        "HOST": get_secret("DATABASE_HOST", "db"),
        "PORT": port,
    }
}


SECURE_SSL_REDIRECT: bool = True
CSRF_COOKIE_SECURE: bool = True
SESSION_COOKIE_SECURE: bool = True

# Static Files URL
STATIC_URL: str = "cdn.basedomain/static/"

# Media Files URL
MEDIA_URL: str = "cdn.basedomain/media/"
