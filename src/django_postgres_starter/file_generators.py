import os
from .utils import generate_secret_key
from .constants import GITIGNORE_CONTENT, BASE_HTML, NAVBAR_HTML, FOOTER_HTML, CSS_CONTENT, JS_CONTENT

def create_gitignore(project_path):
    with open(os.path.join(project_path, '.gitignore'), 'w') as f:
        f.write(GITIGNORE_CONTENT.strip())

def create_html_files(project_name, module_app_name):
    with open('templates/base.html', 'w') as f:
        f.write(BASE_HTML.format(project_name=project_name))

    with open('templates/navbar.html', 'w') as f:
        f.write(NAVBAR_HTML)

    with open('templates/footer.html', 'w') as f:
        f.write(FOOTER_HTML.format(project_name=project_name))

    module_templates_path = os.path.join(module_app_name, 'templates', module_app_name)
    os.makedirs(module_templates_path, exist_ok=True)
    with open(os.path.join(module_templates_path, 'index.html'), 'w') as f:
        f.write(f"""
{{% extends 'base.html' %}}

{{% block title %}}Home{{% endblock %}}

{{% block content %}}
    <h1>Welcome to {module_app_name}</h1>
    <p>This is a sample template for your module app.</p>
{{% endblock %}}
""")

def create_css_file():
    with open('static/css/styles.css', 'w') as f:
        f.write(CSS_CONTENT)

def create_js_file():
    with open('static/js/scripts.js', 'w') as f:
        f.write(JS_CONTENT)

def create_settings_file(main_app_name, module_app_name):
    settings_content = f"""
from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{module_app_name}',
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

ROOT_URLCONF = '{main_app_name}.urls'

TEMPLATES = [
    {{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {{
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }},
    }},
]

WSGI_APPLICATION = '{main_app_name}.wsgi.application'

# Database
DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }}
}}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',}},
    {{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',}},
    {{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',}},
    {{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',}},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
"""

    settings_path = os.path.join(main_app_name, 'settings.py')
    with open(settings_path, 'w') as f:
        f.write(settings_content)

def create_env_file(db_name, db_user, db_password):
    with open(".env", "w") as f:
        f.write(f"SECRET_KEY={generate_secret_key()}\n")
        f.write("DEBUG=True\n")
        f.write("ALLOWED_HOSTS=localhost,127.0.0.1\n")
        f.write(f"DB_NAME={db_name}\n")
        f.write(f"DB_USER={db_user}\n")
        f.write(f"DB_PASSWORD={db_password}\n")
        f.write("DB_HOST=localhost\n")
        f.write("DB_PORT=5432\n")

def create_urls_file(main_app_name, module_app_name):
    # Create main project urls.py
    main_urls_content = f"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('{module_app_name}.urls')),
]
"""
    with open(os.path.join(main_app_name, 'urls.py'), 'w') as f:
        f.write(main_urls_content)

    # Create module app urls.py
    module_urls_content = f"""from django.urls import path
from . import views

app_name = '{module_app_name}'

urlpatterns = [
    path('', views.home, name='home'),
]
"""
    with open(os.path.join(module_app_name, 'urls.py'), 'w') as f:
        f.write(module_urls_content)

def create_forms_file(file_path):
    with open(file_path, 'w') as f:
        f.write("""from django import forms

# Add your forms here
# class ExampleForm(forms.Form):
#     field_name = forms.CharField(max_length=100)
""")

def create_views_file(file_path, module_app_name):
    with open(file_path, 'w') as f:
        f.write(f"""from django.shortcuts import render

def home(request):
    return render(request, '{module_app_name}/index.html')
""")