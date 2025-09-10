# pbp-assignment-2

**How I implemented the checklist for the assignment**
1. Initiate local directory and GitHub repository named pbp-assignment-2
    - git init
    - add .gitignore and list files not to be pushed
    - git remote add origin https://github.com/inoperatingsystem/pbp-assignment-2.git
    - git branch -M master
    - git add, commit, push
2. Create and isolate environment
    - python3 -m venv env
    - source env/bin/activate
3. Install dependencies and start django project
    - write django and needed dependencies in requirements.txt
    - pip install -r requirements.txt
    - django-admin startproject gooner_store
4. Configure environment variables
    - create .env file in root directory
    - write 'PRODUCTION=False' in .env
    - create .env.prod
    - write DB configuration in .env.prod with 'PRODUCTION=True' and 'SCHEMA=tugas_individu'
5. Configure settings.py
    - import and add 'load_dotenv()' to use environment variables
    - add 'ALLOWED_HOSTS = ["localhost", "127.0.0.1"]' to list hosts allowed to access the web app
    - write above DEBUG: 'PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true''
    - Change database configuration to use PostgreSQL with credentials from environment variables
6. Create main app in the project
    - python3 manage.py startapp main
    - add 'main' to INSTALLED_APPS in settings.py
7. Create models
    - Product model with attributes: id, name, price, description, thumbnail, category, is_featured,stock
8. Make and apply migrations
    - python3 manage.py makemigrations
    - python3 managepy migrate
9. Create views and template
    - import render in views.py
    - make show_main function, create context containing data to be sent to view, and return render
    - create templates directory in main and main.html inside
    - display data and create template variables to display the variable values in context
10. Configure URL Routing
    - open urls.py in main and modify the urlpatterns
    - open urls.py in gooner_store project directory
    - add 'include' import
    - add 'path('', include('main.urls')),' to urlpatterns
11. Unit testing
    - create tests.py in main
    - import TestCase, Client, News
    - add test functions
    - run python manage.py test
12. Deploy with PWS
    - create a new project in pws
    - add PWS deployment url to ALLOWED_HOSTS in settings.py
    - git add, commit, push
    - run commands listed in PWS Project Command
    - git push pws master
    - view the site in PWS deployment URL

**Django Diagram**
<img width="1320" height="840" alt="Flowchart" src="https://github.com/user-attachments/assets/f10a73c2-0511-4397-8940-72ccd17d0ae0" />

**How migration works in Django**

In Django, database migration is the process of keeping your database schema in sync with your models. It allows you to evolve the database structure without losing data. 
1. Models define the schema or how your database tables should look like.
2. makemigrationa
    Django compares current models.py with the last migration state. 
    It then generate migration files which describe changes to apply.
3. migrate
    Django looks at unapplied migration files and executes the SQL statements needed to alter the database schema.
    It also updates a special table called django_migrations, which records which migrations have been applied.

**Opinion on why Django is chosen as starting point on learning software development**
- It already comes prepackaged with a lot of common features you need for web development (database handling, URL routing, etc.), so we don't have to set up a lot manually.
- Django uses clear structure (Model-View-Template) that makes it easier to understand how web apps work. Easily transferable knowledge to many other frameworks (Rails, Laravel, Sprint, etc.) which follows similar MVC-like patterns. (Model-View-Controller)
- Thorough and easy to understand documentation and a large, global community which means there is a lot of tutorials and public projects to learn from.
- Teaches good programming practices. Built-in protection against attacks (SQL injection, XSS, CRSF, etc.), encourages DRY (Don't Repeat Yourself), and introduces migrations, testing, modular apps, deployment, which are widely-used concepts in software development.

**Feedback for the TA for tutorial 1**
- Easy to approach and responsive to questions.
- List different commands for Windows ("python ...") and Unix-like ("python3 ..."). Some people may not realize these differences and might be confused on why running only "python ..." doesn't work on their system.
