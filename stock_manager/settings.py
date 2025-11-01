import os
from pathlib import Path
import dj_database_url
from decouple import Config, Csv

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Utiliser Config et spécifier explicitement le chemin vers .env
config = Config(search_path=BASE_DIR)  

# Security settings
SECRET_KEY = config('SECRET_KEY', default='your-default-secret-key')  # Utilise une clé secrète à partir de la variable d'environnement
DEBUG = config('DEBUG', default=False, cast=bool)  # Passer à False en production
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())  # Liste des hôtes autorisés (à configurer dans Render)

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stock_app',  # Ton app ici
    'whitenoise.runserver_nostatic',  # Pour la gestion des fichiers statiques
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Pour gérer les fichiers statiques en production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs
ROOT_URLCONF = 'stock_manager.urls'

# WSGI application
WSGI_APPLICATION = 'stock_manager.wsgi.application'

# Database settings
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),  # Utilise l'URL de la base de données PostgreSQL fournie par Render
        conn_max_age=600,
        ssl_require=True
    )
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Dossier pour les fichiers statiques collectés
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Dossier pour les fichiers média uploadés

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production
SECURE_SSL_REDIRECT = True  # Redirige HTTP vers HTTPS
CSRF_COOKIE_SECURE = True  # Sécurise les cookies CSRF en production
SESSION_COOKIE_SECURE = True  # Assure que les cookies de session sont sécurisés
X_FRAME_OPTIONS = 'DENY'  # Empêche l'inclusion de ton site dans un iframe

# Django settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
