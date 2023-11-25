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

# Does nothing - Not Yet Implemented
DJANGO_HOST_ADDRESS = os.getenv('SERVER_ADDRESS', '127.0.0.1')
DJANGO_HOST_PORT = os.getenv('SERVER_PORT', '8000')    
NEXTJS_HOST_ADDRESS = os.getenv('NEXTJS_ADDRESS', 'localhost')
NEXT_JS_PORT = os.getenv('NEXTJS_PORT', '3000') 

# Build paths inside project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_DIR = BASE_DIR / 'server/config'

AUTH_KEYS = os.getenv('AUTH_KEYS_FILE', (CONFIG_DIR / 'keys-dev.json').resolve().__str__()).strip("\"")

MODELS_CONFIG = os.getenv('LLM_MODELS_FILE', (CONFIG_DIR / 'models.json').resolve().__str__())

ROOT_URLCONF = 'app.urls'                      # module that contains root project url mapping
WSGI_APPLICATION = 'app.wsgi.application'      # module that contains application deployment code

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
    'prompt_library',
    'multi_llm',
    'jira'
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

# =============================================================================
#   Database Settings - database engine and ORM definitions.
#   See - https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# =============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'server/db.sqlite3',
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
#
#   Never deploy with debug = true in production.
#   Keep your authentication and project keys a secret 
#       - DO NOT commit to source control.
#   The file 'keys-dev.json' is a dummy file provided for test and development 
#   configurations.
# =============================================================================

DEBUG = os.getenv('SERVER_DEBUG', 'False').lower() == 'true'

with open(AUTH_KEYS) as auth:
    entry: dict[str, str]
    auth_keys = json.load(auth)
    for entry in auth_keys['llm_auth_keys']:
        for key, value in entry.items():
            os.environ[key] = value

    SECRET_KEY = os.environ['MULTI_LLM_SECRET_KEY']

ALLOWED_HOSTS = [DJANGO_HOST_ADDRESS]

# CORS Settings - see https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = False                                   
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = ['http://' + NEXTJS_HOST_ADDRESS + ':' + NEXT_JS_PORT]

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

# Static files (CSS, JavaScript, Images), point to NextJS build folder
# See - https://docs.djangoproject.com/en/4.2/howto/static-files/
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