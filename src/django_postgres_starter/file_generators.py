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
    # Implementation for creating settings.py
    pass

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

def create_urls_file(module_app_name):
    # Implementation for creating urls.py
    pass

def create_forms_file(file_path):
    with open(file_path, 'w') as f:
        f.write("""from django import forms

# Add your forms here
# class ExampleForm(forms.Form):
#     field_name = forms.CharField(max_length=100)
""")

def create_views_file(file_path, module_app_name):
    with open(file_path, 'a') as f:
        f.write(f"""
from django.shortcuts import render

def home(request):
    return render(request, '{module_app_name}/index.html')
""")