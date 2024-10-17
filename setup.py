from setuptools import setup, find_packages

# Optionally, read README.md for long description
# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name="django-postgres-starter",
    version="0.1.0",
    author="James Stephenson, PhD",
    author_email="jstephen@scc-i.com",
    description="A tool to quickly set up a Django project with PostgreSQL",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/yourusername/django-postgres-starter",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "Django>=4.2,<5.0",
        "psycopg2-binary>=2.9.6",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "django-postgres-starter=django_postgres_starter.main:main",
        ],
    },
)