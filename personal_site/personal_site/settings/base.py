from pathlib import Path
from personal_site.settings import get_secret
from .types import TemplateConfig, PasswordValidator

# --- Paths ---
BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

# --- Installed apps ---
INSTALLED_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_hosts",
]

# --- Middleware ---
middleware: list[str] = [
    "django_hosts.middleware.HostsRequestMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_hosts.middleware.HostsResponseMiddleware",
]

# --- URLs ---
ROOT_URLCONF: str = "personal_site.urls"

# --- Templates ---
TEMPLATES: list[TemplateConfig] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# --- WSGI ---
WSGI_APPLICATION: str = "personal_site.wsgi.application"

# --- Password validation ---
AUTH_PASSWORD_VALIDATORS: list[PasswordValidator] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Time & Locale ---
TIME_ZONE: str = "America/New_York"
USE_TZ: bool = True

# --- Defaults ---
DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"
DEFAULT_HOST: str = "resume"
PARENT_HOST: str = "basedomain"  # or example.com


# --- Helpers ---
def get_bool(secret_id: str) -> bool:
    val = get_secret(secret_id, "")
    return val.lower() in {"1", "true", "yes"} if val else False


# --- Sphinx override ---
if get_bool("SPHINX_BUILD"):
    middleware: list[str] = [
        mw
        for mw in middleware
        if "django_hosts.middleware.HostsRequestMiddleware" not in mw
        and "django_hosts.middleware.HostsResponseMiddleware" not in mw
    ]

MIDDLEWARE: list[str] = middleware
