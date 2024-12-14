"""
Django settings for marketplace project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4bq4ik+=sy0tc1lhpkk9(x(%45a0s0t$@&1d2ydn9xjm&q^wtm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'marketplace_api',
    'rest_framework',
    'corsheaders',
    'accounts',
    



]

CORS_ALLOW_ALL_ORIGINS = True
CSRF_COOKIE_SECURE = False
CORS_ORIGIN_WHITELIST = ['http://localhost:3000']

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Allow all methods
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    
]

ROOT_URLCONF = 'marketplace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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






WSGI_APPLICATION = 'marketplace.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


#database 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online_marketplace',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
         'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }, 
        
    }
}


# sent email 
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'kaveendahelitha@gmail.com'
#EMAIL_HOST_PASSWORD = 'vyvambgauqevkjex'
#EMAIL_USE_TLS = True


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#json web token part
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}

#SIMPLE_JWT = {
   #'AUTH_HEADER_TYPES': ('JWT',),
  # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
  # 'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
   # 'AUTH_TOKEN_CLASSES': (
    #    'rest_framework_simplejwt.tokens.AccessToken',
    #)
#}

#DJOSER = {
#    'LOGIN_FIELD': 'email',
#    'USER_CREATE_PASSWORD_RETYPE': True,
#    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
#    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
#    'SEND_CONFIRMATION_EMAIL': True,
#    'SET_USERNAME_RETYPE': True,
#    'SET_PASSWORD_RETYPE': True,
#    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
#    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
#    'ACTIVATION_URL': 'activate/{uid}/{token}',
#    'SEND_ACTIVATION_EMAIL': True,
#    #'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
#    #'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://localhost:8000/google', 'http://localhost:8000/facebook'],
#    'SERIALIZERS': {
#        'user_create': 'accounts.serializers.UserCreateSerializer',
#        'user': 'accounts.serializers.UserCreateSerializer',
#        'current_user': 'accounts.serializers.UserCreateSerializer',
#        'user_delete': 'djoser.serializers.UserDeleteSerializer',
#    }
#}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py


CORS_ALLOW_ALL_ORIGINS=True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL= '/media/'