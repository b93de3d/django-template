from pathlib import Path
import json
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


with open("/etc/{{ project_name }}_config.json") as f:
    CONFIG = json.loads(f.read())

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = CONFIG["SECRET_KEY"]

ENV = CONFIG.get("ENV", "DEV")

if ENV == "DEV":
    DEBUG = True
    HOST = "4e8000.ngrok.io"
    FRONTEND_HOST = "4e3000.ngrok.io"
    ALLOWED_HOSTS = ["*"]
    CORS_ALLOW_ALL_ORIGINS = True
else:
    DEBUG = False
    HOST = CONFIG["HOST"]
    FRONTEND_HOST = HOST
    ALLOWED_HOSTS = [HOST]
    CORS_ALLOWED_ORIGINS = [f"https://{FRONTEND_HOST}"]
    STATIC_ROOT = "/home/rowan/src/static"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "dynamic_rest",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{{ project_name }}.urls"

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

WSGI_APPLICATION = "{{ project_name }}.wsgi.application"

if ENV == "DEV":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": CONFIG["DB_NAME"],
            "USER": CONFIG["DB_USER"],
            "PASSWORD": CONFIG["DB_PASSWORD"],
            "HOST": CONFIG["DB_HOST"],
            "PORT": CONFIG["DB_PORT"],
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAdminUser"],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.zoho.com"
EMAIL_PORT = "465"
EMAIL_USE_SSL = True
EMAIL_HOST_USER = CONFIG["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = CONFIG["EMAIL_HOST_PASSWORD"]

STRIPE_SK = CONFIG["STRIPE_SK"]
STRIPE_WH = CONFIG["STRIPE_WH"]

if ENV != "DEV":
    sentry_sdk.init(
        dsn=CONFIG["SENTRY_DSN"],
        integrations=[DjangoIntegration()],
        traces_sample_rate=0.01,
        send_default_pii=True
    )
