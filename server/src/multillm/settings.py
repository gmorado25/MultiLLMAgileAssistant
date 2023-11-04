from distutils.util import strtobool
import json, os
from pathlib import Path

# =============================================================================
#   General Application Settings - module definitions. These will rarely need
#   to change.
#
#   For more information on this file, see
#   https://docs.djangoproject.com/en/4.2/topics/settings/
#
#   For the full list of settings and their values, see
#   https://docs.djangoproject.com/en/4.2/ref/settings/
#
#   For deploying project, see 
#   https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
#
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent   # Build paths inside project like this: BASE_DIR / 'subdir'.
CONFIG_DIR = BASE_DIR.parent / 'config'

ROOT_URLCONF = 'multillm.urls'                      # module that contains root project url mapping
WSGI_APPLICATION = 'multillm.wsgi.application'      # module that contains application deployment code

# Application definition - What modules should be loaded when starting the server.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_nextjs',
    'app'
]

# Middleware definition - What middleware features should be loaded when starting the server.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

NEXTJS_ADDRESS = os.environ['NEXTJS_ADDR']               # What address the NextJS front end is running on.

# =============================================================================
#   Database Settings - database engine and ORM definitions.
#   See - https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# =============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'    # What type auto-generated primary keys are

# =============================================================================
#   Localization Settings - date, time, language, etc.
#   See - https://docs.djangoproject.com/en/4.2/topics/i18n/
# =============================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =============================================================================
#   !!!IMPORTANT!!! SECURITY SETTINGS
#
#   See - https://docs.djangoproject.com/en/4.2/topics/security/
#         https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# =============================================================================

# Never deploy with debug = true in production
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'

# Keep your authentication and project keys a secret - DO NOT commit to source control
# The file 'keys-dev.json' is a dummy file provided for test and development configurations
if (DEBUG is True):
    auth_config = CONFIG_DIR / 'keys-dev.json' 
else: 
    auth_config = CONFIG_DIR / 'keys-prod.json'

with open(auth_config) as auth:
    keys = json.load(auth)
    SECRET_KEY = keys['MULTI_LLM_SECRET_KEY'] # Secret used by django server

# What address(es) django is allowed to serve. Required outside of debug mode.
ALLOWED_HOSTS = [NEXTJS_ADDRESS]

# CORS Settings - see https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = False                                   
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [NEXTJS_ADDRESS]

# =============================================================================
#   Miscellaneous django settings
#
#   See - https://docs.djangoproject.com/en/4.2/topics/security/
#         https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# =============================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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