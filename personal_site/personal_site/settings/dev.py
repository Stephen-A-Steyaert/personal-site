from .base import *
from dotenv import load_dotenv
from personal_site.settings import get_secret
from personal_site.settings.types import Databases
from typing import Optional

load_dotenv(BASE_DIR / "personal_site" / "settings" / ".env")

DEBUG: bool = True
ALLOWED_HOSTS: list[str] = ["*"]
SECRET_KEY: Optional[str] = get_secret("SECRET_KEY", "")

DATABASES: Databases = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "USER": None,
        "PASSWORD": None,
        "HOST": None,
        "PORT": None,
    }
}


STATIC_URL: str = "/static/"
MEDIA_URL: str = "/media/"
