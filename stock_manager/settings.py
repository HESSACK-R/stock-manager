import os
from pathlib import Path
import dj_database_url

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')  # Use a secret key from env variable in production
DEBUG = os.environ.get('DEBUG', 'True') == 'True'  # Change to 'False' in production
ALLOWED_HOSTS = ['*']  # Or specify your domain name in production

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stock_app',  # Your app here
    'whitenoise.runserver_nostatic',  # For static file management
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # To handle static files in production
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
        default='postgres://USER:PASSWORD@HOST:PORT/NAME',  # Use Render's PostgreSQL credentials
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
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory for collected static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Directory for uploaded media files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
CSRF_COOKIE_SECURE = True  # Set CSRF cookie to be secure in production
SESSION_COOKIE_SECURE = True  # Ensure session cookies are secure
X_FRAME_OPTIONS = 'DENY'

# Django settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
