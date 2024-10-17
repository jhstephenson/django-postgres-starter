import argparse
import getpass
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='Set up a new Django project with PostgreSQL.')
    parser.add_argument('--project-name', help='Name of the Django project')
    parser.add_argument('--main-app-name', help='Name of the main Django app')
    parser.add_argument('--module-app-name', help='Name of the first module app')
    parser.add_argument('--db-name', help='PostgreSQL database name')
    parser.add_argument('--db-user', help='PostgreSQL database user')
    parser.add_argument('--db-password', help='PostgreSQL database password')
    parser.add_argument('--target-dir', help='Target directory for project creation')
    
    args = parser.parse_args()
    
    # Prompt for missing arguments
    if not args.project_name:
        args.project_name = input("Enter project name: ")
    if not args.main_app_name:
        args.main_app_name = input("Enter main app name: ")
    if not args.module_app_name:
        args.module_app_name = input("Enter module app name: ")
    if not args.db_name:
        args.db_name = input("Enter database name: ")
    if not args.db_user:
        args.db_user = input("Enter database user: ")
    if not args.db_password:
        args.db_password = getpass.getpass("Enter database password: ")
    if not args.target_dir:
        args.target_dir = input("Enter target directory for project creation (or press Enter for current directory): ")
        if not args.target_dir:
            args.target_dir = os.getcwd()
    
    return args