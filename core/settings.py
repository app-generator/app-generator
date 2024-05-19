"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os, random, string
from pathlib import Path
from django.contrib import messages
from str2bool import str2bool 
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))

# Enable/Disable DEBUG Mode
DEBUG = str2bool(os.environ.get('DEBUG'))

# Hosts Settings
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com', '0.0.0.0']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://localhost:5085', 'http://127.0.0.1:8000', 'http://127.0.0.1:5085', 'https://core-django.onrender.com']

# Application definition

INSTALLED_APPS = [
    "webpack_loader",
    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # APPS
    "home",
    "apps.users",
    #"apps.auth",
    "apps.blog",
    #"apps.auth",
    #"apps.deploy",
    #"apps.docs",
    #"apps.generator",
    #"apps.pages",
    #"apps.products",
    #"apps.tasks",
    #"apps.tools",

    # Util
    "debug_toolbar",

    # allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

    'django_quill',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Util
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    # allauth 
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "core.urls"

UI_TEMPLATES = os.path.join(BASE_DIR, 'templates') 

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [UI_TEMPLATES],
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


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MESSAGE_TAGS = {
    messages.INFO: 'text-blue-800 border border-blue-300 bg-blue-50 dark:text-blue-400 dark:border-blue-800',
    messages.SUCCESS: 'text-green-800 border border-green-300 bg-green-50 dark:text-green-400 dark:border-green-800',
    messages.WARNING: 'text-yellow-800 border border-yellow-300 bg-yellow-50 dark:text-yellow-300 dark:border-yellow-800',
    messages.ERROR: 'text-red-800 border border-red-300 bg-red-50 dark:text-red-400 dark:border-red-800',
}

SITE_ID = 1
LOGIN_REDIRECT_URL = "/users/profile/"

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_SECRET_KEY = os.getenv("GOOGLE_SECRET_KEY", "")

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "")
GITHUB_SECRET_KEY = os.getenv("GITHUB_SECRET_KEY", "")


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        "APP": {
            "client_id": GOOGLE_CLIENT_ID,
            "secret": GOOGLE_SECRET_KEY,
        },
    },
    'github': {
        "APP": {
            "client_id": GITHUB_CLIENT_ID,
            "secret": GITHUB_SECRET_KEY,
        },
    },
}


QUILL_CONFIGS = {
    'default':{
      "theme": "snow",
      "modules": {
        "syntax": True,
        "toolbar": [
          [
            {"header": []},
            {"align": []},
            "bold",
            "italic",
            "underline",
            "strike",
            "blockquote",
          ],
          ["code-block", "link"],
        ],
        "imageCompressor": {
          "quality": 0.8,
          "maxWidth": 2000,
          "maxHeight": 2000,
          "imageType": "image/jpeg",
          "debug": False,
          "suppressErrorLogging": True
        },
        "resize": {
          "showSize": True,
          "locale": {}
        }
      },
      "formats": [
        "header",
        "bold",
        "italic",
        "underline",
        "strike",
        "blockquote",
        "code-block",
        "link",
        "indent",
        "list",
        "align",
      ],
      "sanitize": True,
    }
}