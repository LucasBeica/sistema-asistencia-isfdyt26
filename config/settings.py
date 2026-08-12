"""
Django settings for config project.
"""

import os
from pathlib import Path

import dj_database_url


# ==================================================
# RUTAS
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
# SEGURIDAD
# ==================================================

# En Render se cargará desde una variable de entorno.
# En tu PC se usa esta clave solamente para desarrollo.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-clave-local-desarrollo-2026"
)


# ==================================================
# DEBUG
# ==================================================

# Local = True
# Render = False
DEBUG = not bool(os.environ.get("RENDER"))


# ==================================================
# HOSTS PERMITIDOS
# ==================================================

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

# Render proporciona automáticamente el nombre del dominio.
if os.environ.get("RENDER_EXTERNAL_HOSTNAME"):
    ALLOWED_HOSTS.append(
        os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    )


# ==================================================
# APLICACIONES
# ==================================================

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "Asistencia",
]


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise sirve CSS, imágenes y demás archivos estáticos
    # en producción.
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==================================================
# URLS
# ==================================================

ROOT_URLCONF = "config.urls"


# ==================================================
# TEMPLATES
# ==================================================

TEMPLATES = [

    {
        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

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


# ==================================================
# WSGI
# ==================================================

WSGI_APPLICATION = "config.wsgi.application"


# ==================================================
# BASE DE DATOS
# ==================================================

# En Render:
# DATABASE_URL = PostgreSQL
#
# En tu PC:
# SQLite (db.sqlite3)

if os.environ.get("DATABASE_URL"):

    DATABASES = {
        "default": dj_database_url.parse(
            os.environ.get("DATABASE_URL"),
            conn_max_age=600,
        )
    }

else:

    DATABASES = {

        "default": {

            "ENGINE":
                "django.db.backends.sqlite3",

            "NAME":
                BASE_DIR / "db.sqlite3",
        }
    }


# ==================================================
# VALIDACIÓN DE CONTRASEÑAS
# ==================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ==================================================
# IDIOMA Y ZONA HORARIA
# ==================================================

LANGUAGE_CODE = "es-ar"

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_I18N = True

USE_TZ = True


# ==================================================
# ARCHIVOS ESTÁTICOS
# ==================================================

STATIC_URL = "/static/"


# Carpeta donde Django juntará todos los archivos
# estáticos al ejecutar collectstatic.
STATIC_ROOT = BASE_DIR / "staticfiles"


# Carpeta donde actualmente tenés:
#
# Asistencia/
#     static/
#         css/
#         img/
#
STATICFILES_DIRS = [

    BASE_DIR / "Asistencia" / "static",

]


# WhiteNoise permite servir los archivos estáticos
# directamente desde Django en producción.
STORAGES = {

    "default": {
        "BACKEND":
            "django.core.files.storage.FileSystemStorage",
    },

    "staticfiles": {
        "BACKEND":
            "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# ==================================================
# CONFIGURACIÓN DE PRODUCCIÓN
# ==================================================

if not DEBUG:

    # Render utiliza HTTPS.
    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https",
    )

    # Las cookies se envían solamente mediante HTTPS.
    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True


# ==================================================
# CONFIGURACIÓN DE DJANGO
# ==================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
