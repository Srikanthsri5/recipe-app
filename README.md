# Recipe App

    Recipe App is a project using Django Rest Framework to manage and share recipes.

## Continuous Integration
    This project uses GitHub Actions for continuous integration. The workflow is configured to run pytest tests on each push and pull request to ensure code quality and functionality.

## Docker
    Recipe App is built using Docker for containerization, ensuring consistency across different environments.

## Features

- Create, read, update, and delete recipes
- User authentication and authorization
- Search and filter recipes
- API documentation with Django Rest Framework

## Installation

1. Clone the repository:
    git clone https://github.com/Srikanthsri5/recipe-app.git
    cd recipe-app

2. Create and activate a virtual environment:
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:
    pip install -r requirements.txt

4. Set up the database:
    python manage.py migrate

5. Create a superuser to access the admin interface:
    python manage.py createsuperuser

6. Start the development server:
    python manage.py runserver

7. Usage
    Access the application at http://127.0.0.1:8000/ in your web browser.
    Use the admin interface at http://127.0.0.1:8000/admin/ to manage users and recipes.

