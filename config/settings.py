"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import lesson.apps
from config import local_settings

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r3c3c0q+pv7_mz=%fjm(u191x^n9n8ow&_#48*ayynx&53vnni'

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

    # для работы с БД
    'django.contrib.postgres',

    # django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',



    # local
    'cards.apps.CardsConfig',
    'users.apps.UsersConfig',
    'lesson.apps.LessonConfig',

    # django-cleanup для удаления не используемых файлов
    'django_cleanup.apps.CleanupConfig',  # должен быть помещен последним

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pet_project',
        'USER': 'vlad',
        'PASSWORD': 'admin',
        # 'HOST': 'localhost',
        # 'PORT': 5432,
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Медиа файлы
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Настройка модели пользователя
AUTH_USER_MODEL = 'users.CustomUser'

# Настройка django-allauth
SITE_ID = 1
# TODO: Редирект пока не работает, создай в urls 'home'
LOGIN_REDIRECT_URL = 'dictionary:home'  # Перенаправление при входе
ACCOUNT_LOGOUT_REDIRECT = 'dictionary:home'  # Перенаправление при выходе
ACCOUNT_SESSION_REMEMBER = True  # Запоминать сессии пользователя
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True  # Использовать при регистрации две строки пароля
ACCOUNT_USERNAME_REQUIRED = False  # Требовать обязательного вода имени пользователя если True
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Какой метод использовать при входе на сайт
ACCOUNT_EMAIL_REQUIRED = True  # Обязательная передача адреса электронной почты
ACCOUNT_UNIQUE_EMAIL = True  # Обеспечение уникальности адресов электронной почты
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Почтовые отправления
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = local_settings.EMAIL_HOST  # хост SMTP-сервера
EMAIL_HOST_USER = local_settings.EMAIL_HOST_USER  # логин пользователя для SMTP-сервера
EMAIL_HOST_PASSWORD = local_settings.EMAIL_HOST_PASSWORD  # пароль пользователя для SMTP-сервера
EMAIL_PORT = 587  # порт SMTP-сервера
EMAIL_USE_TLS = True  # использовать ли защищенное TLS-подключение
DEFAULT_FROM_EMAIL = local_settings.DEFAULT_FROM_EMAIL  # От кого будут отправляться письма
