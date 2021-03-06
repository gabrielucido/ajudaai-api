import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'wi(c88*#)r*)c7#bgscj=b$pa$s8+7e*w9jdfcf=ti(bf-19k-'

ALLOWED_HOSTS = ['*']

if os.environ.get('MODE') == 'production':
    DEBUG = False
else:
    DEBUG = True

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APPS = [
    'autoslug',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'watson',
    'djoser',
]

LOCAL_APPS = [
    'core',
    'issues',
    'comments',
    'users',
]

REQUIRED_LAST_APPS = [
    'django_cleanup.apps.CleanupConfig',
]

INSTALLED_APPS = LOCAL_APPS + DEFAULT_APPS + EXTERNAL_APPS + REQUIRED_LAST_APPS

PRE_COMMOM_MIDDLEWARES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

DJANGO_MIDDLEWARES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

OTHERS_MIDDLEWARES = [
    'watson.middleware.SearchContextMiddleware',
]
WATSON_BACKEND = "watson.backends.AdaptiveSearchBackend"

MIDDLEWARE = PRE_COMMOM_MIDDLEWARES + DJANGO_MIDDLEWARES + OTHERS_MIDDLEWARES

ROOT_URLCONF = 'project.urls'

CONTEXT_PROCESSORS = [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': CONTEXT_PROCESSORS
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}
# Covers regular testing and django-coverage preventing errors
if 'test' in sys.argv or 'test/_coverage' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    DATABASES['default']['NAME'] = ':memory:'

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

AUTH_USER_MODEL = 'users.User'

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'project/static_files')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'project/media_files')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Django Rest Config
if DEBUG:
    DEFAULT_RENDERER_CLASSES = (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
else:
    DEFAULT_RENDERER_CLASSES = (
        'rest_framework.renderers.JSONRenderer',
    )

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 6,
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES,
    'DATETIME_FORMAT': '%d/%m/%Y %H:%M:%S',
    'DATE_FORMAT': '%d/%m/%Y',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

CORS_ALLOW_ALL_ORIGINS = True

LOGIN_URL = "/admin"
LOGIN_REDIRECT_URL = "/ajudaai/v1/"
