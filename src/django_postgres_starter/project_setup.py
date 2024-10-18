import os
import venv
import sys
from .utils import run_command
from .file_generators import (
    create_gitignore, create_html_files, create_css_file, create_js_file,
    create_settings_file, create_env_file, create_urls_file, create_forms_file,
    create_views_file
)

def create_django_project(args):
    project_name = args.project_name
    main_app_name = args.main_app_name
    module_app_name = args.module_app_name
    db_name = args.db_name
    db_user = args.db_user
    db_password = args.db_password
    target_dir = os.path.abspath(args.target_dir)

    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Set up project structure
    project_path = os.path.join(target_dir, project_name)
    os.makedirs(project_path, exist_ok=True)
    os.chdir(project_path)

    # Create virtual environment
    venv.create("venv", with_pip=True)

    # Determine the path to the Python executable in the virtual environment
    if sys.platform == "win32":
        python_executable = os.path.join("venv", "Scripts", "python.exe")
    else:
        python_executable = os.path.join("venv", "bin", "python")

    # Install Django and other required packages
    run_command(f'"{python_executable}" -m pip install django psycopg2-binary python-dotenv')

    # Create Django project
    run_command(f'"{python_executable}" -m django startproject {main_app_name} .')

    # Create module app
    run_command(f'"{python_executable}" manage.py startapp {module_app_name}')

    # Create additional directories
    os.makedirs('media', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    os.makedirs(os.path.join('static', 'css'), exist_ok=True)
    os.makedirs(os.path.join('static', 'js'), exist_ok=True)
    os.makedirs(os.path.join('static', 'images'), exist_ok=True)

    # Create files
    create_html_files(project_name, module_app_name)
    create_css_file()
    create_js_file()
    create_settings_file(main_app_name, module_app_name)
    create_env_file(db_name, db_user, db_password)
    create_urls_file(main_app_name, module_app_name)
    create_forms_file(os.path.join(module_app_name, 'forms.py'))
    create_views_file(os.path.join(module_app_name, 'views.py'), module_app_name)
    create_gitignore(os.getcwd())

    print(f"{project_name} Django project setup complete!")
    print(f"Project created in: {project_path}")
    print("To activate the virtual environment, run:")
    if sys.platform == "win32":
        print(rf"{project_path}\venv\Scripts\activate")
    else:
        print(f"source {project_path}/venv/bin/activate")
    print("\nBefore running migrations, make sure to:")
    print(f"1. Create a PostgreSQL database named '{db_name}'")
    print("2. Ensure your PostgreSQL user has the necessary permissions")
    print("\nThen, run the following commands:")
    print("python manage.py makemigrations")
    print("python manage.py migrate")
    print("python manage.py runserver")