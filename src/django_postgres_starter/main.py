from .argument_parser import parse_arguments
from .project_setup import create_django_project

def main():
    args = parse_arguments()
    create_django_project(args)

if __name__ == "__main__":
    main()