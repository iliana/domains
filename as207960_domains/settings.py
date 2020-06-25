"""
Django settings for as207960_domains project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import logging


logging.basicConfig(level=logging.INFO)

sentry_sdk.init(
    dsn="https://da23a217b5584ccaa296aea526e3fc2c@o222429.ingest.sentry.io/5247893",
    integrations=[DjangoIntegration()],
    send_default_pii=True
)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.getenv("HOST", "domains.as207960.net")]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django_keycloak_auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.postgres',
    'phonenumber_field',
    'crispy_forms',
    'django_countries',
    'django_grpc',
    'rest_framework',
    'domains'
]

MIDDLEWARE = [
    'xff.middleware.XForwardedForMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django_keycloak_auth.middleware.OIDCMiddleware",
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'domains.exception_logging_middleware.ExceptionLoggingMiddleware'
]

ROOT_URLCONF = 'as207960_domains.urls'

AUTHENTICATION_BACKENDS = ["django_keycloak_auth.auth.KeycloakAuthorization"]

LOGIN_URL = "oidc_login"
LOGOUT_REDIRECT_URL = "oidc_login"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'as207960_domains.wsgi.application'

GRPCSERVER = {
    'servicers': ['domains.whois.grpc_hook'],
    'maximum_concurrent_rpcs': None,
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DB_HOST", "localhost"),
        "NAME": os.getenv("DB_NAME", "domains"),
        "USER": os.getenv("DB_USER", "domains"),
        "PASSWORD": os.getenv("DB_PASS"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

EXTERNAL_URL_BASE = os.getenv("EXTERNAL_URL", f"https://{ALLOWED_HOSTS[0]}")

STATIC_URL = f"{EXTERNAL_URL_BASE}/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = f"{EXTERNAL_URL_BASE}/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

KEYCLOAK_SERVER_URL = os.getenv("KEYCLOAK_SERVER_URL")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM")
OIDC_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
OIDC_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")
OIDC_SCOPES = os.getenv("KEYCLOAK_SCOPES")

PHONENUMBER_DEFAULT_REGION = "GB"
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_FAIL_SILENTLY = not DEBUG

XFF_TRUSTED_PROXY_DEPTH = 2
XFF_STRICT = True

REGISTRATION_ENABLED = True
EPP_PROXY_ADDR = os.getenv("EPP_PROXY_ADDR")
EPP_PROXY_CA = os.getenv("EPP_PROXY_CA")

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 25))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", False)
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", False)
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_FROM", "AS207960 Domains <domains@as207960.net>")

GCHAT_SERVICE_ACCOUNT = os.getenv("GCHAT_SERVICE_ACCOUNT_FILE")
GCHAT_PROJECT_ID = os.getenv("GCHAT_PROJECT_ID")

BILLING_URL = os.getenv("BILLING_URL")

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'domains.api.auth.BearerAuthentication',
        'domains.api.auth.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'EXCEPTION_HANDLER': 'domains.api.exceptions.exception_handler',
    'PAGE_SIZE': 25
}
