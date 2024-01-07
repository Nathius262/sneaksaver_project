import os
from decouple import config
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config("SECRET_KEY")

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [config("END_POINT"),]

ROOT_URLCONF = f'{config("PROJECT_NAME")}.urls'

WSGI_APPLICATION = f'{config("PROJECT_NAME")}.wsgi.application'


#ASGI_APPLICATION = f'{config("PROJECT_NAME")}.routing.application'

# Application definition

INSTALLED_APPS = [
    
    'jazzmin',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #installed apps
    #'cloudinary_storage',
    #'cloudinary',


    'authentication',
    'user',
    'sneaksaver',

    #django alllauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #'dj_rest_auth',
    #'dj_rest_auth.registration',
    'rest_framework_simplejwt',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'notifications',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = config("LANGUAGE_CODE")

TIME_ZONE = config("TIME_ZONE")

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'authentication.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django allauth configuration
SITE_ID = 1

#ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_LOGOUT_REDIRECT_URL = "/account/login/"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_USERNAME_REQUIRED =True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_FORMS = {'signup': 'authentication.forms.RegistrationForm'}
#ACCOUNT_USERNAME_MIN_LENGTH = 10

ACCOUNT_EMAIL_REQUIRED = True

# REST_AUTH_SERIALIZERS ={
#     "LOGIN_SERIALIZER": 'user.serializers.LoginSerializer'
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'DEFAULT_PREMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

REST_AUTH_REGISTER_SERIALIZERS ={
    'REGISTER_SERIALIZER': 'authentication.serializers.CustomRegisterSerializer'
}

REST_AUTH = {

    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY':True,
    'JWT_AUTH_COOKIE': 'access',
    #'JWT_AUTH_REFRESH_COOKIE': "refresh",
}


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ["BEARER"],
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=40),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(hours=72),
}

###############
###############
#####
##### DJANGO CORES HEADER CONFIGURATION
#####
###############
###############
CORS_URLS_REGEX = r"^/api/.*$"

CORS_ALLOWED_ORIGINS = [
    f'https://{config("END_POINT")}',
    f'http://{config("END_POINT")}',
]


#APPEND_SLASH=False

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_HEADERS = [
    "Content-Type",
    "Authorization",
    'access-control-allow-headers',
    'access-control-allow-origin',
]


STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    #os.path.join(BASE_DIR, MEDIA_URL)
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn/')


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
        }
    }
    
    

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config("DB_NAME"),
            'USER': config("DB_USER"),
            'PASSWORD': config("DB_PASSWORD"),
            'HOST': config("DB_HOST"),
            'PORT': '3306',
        }
    }

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')


    #BASE_URL = "Sneaksaver.pythonanywhere.com"

    # settings.py

    """LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': '/var/log/django_logs/error.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }"""

#Jazzmin configuration
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Sneaksaver Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Sneaksaver",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Sneaksaver",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "favicon.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "favicon.png",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "favicon.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "favicon.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Sneaksaver",

    # Copyright on the footer
    "copyright": "Sneaksaver",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    "search_model": ["authentication.CustomUser", ],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,


    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "authentication.CustomUser": "fas fa-user",
        "sites.Site": "fa fa-solid fa-sitemap",

    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "style.css",
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    "changeform_format_overrides": {"user": "collapsible", "allauth.account": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
}