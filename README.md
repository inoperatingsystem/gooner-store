# gooner-store

**PBP ASSIGNMENT 2**

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


**PBP ASSIGNMENT 3**

**Why do we need data delivery in implementing a platform?**

Because a platform usually isn’t only accessed by one type of client (like a website), but also mobile apps or even third-party systems. By using data delivery (through JSON or XML), the backend can send structured data that is easy to process by the frontend or other services. This makes the architecture cleaner, more flexible, and easier to maintain in the long run.

**In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?**

In my opinion, JSON is better and more widely used today. The main reasons are:
- JSON is shorter and easier to read (while XML is more verbose with many tags).
- JSON works natively with JavaScript (JSON.parse(), JSON.stringify()), which makes it super convenient for web apps.
- Its format (objects, arrays, strings, numbers) matches what most programming languages already use.

XML still has its place, for example when working with complex document structures or older/legacy systems. But for modern web development, JSON is more popular because it’s simpler and more practical.

**What is the purpose of the is_valid() method in Django forms, and why do we need it?**

is_valid() checks whether the data submitted through the form meets all the field requirements and validations. If it’s valid, Django will prepare a cleaned_data dictionary that we can safely use to save into the database. If not, it gives back error messages that we can show to the user. Basically, it’s the safety gate to make sure the data is clean before we actually use it.

**Why do we need a csrf_token when making forms in Django? What can happen if we don't include a csrf_token in a Django form? How can this be exploited by an attacker?**

The CSRF token protects against Cross-Site Request Forgery (CSRF) attacks. Without it, a malicious website could trick a logged-in user into unknowingly sending a request to our site (for example, changing their account settings or transferring money). Because the browser automatically includes cookies, the request would look “real” unless we check the CSRF token.
If we don’t use it, attackers can exploit this by making hidden forms or scripts that auto-submit to our site on behalf of the victim. So, including {% csrf_token %} is necessary to ensure that the form really comes from our website.

**Explain how you implemented the checklist above step-by-step (not just following the tutorial).**
1.	Create the model. I defined the model fields (like name, price, stock) in models.py, then ran makemigrations and migrate.
2.	Make the form. I used ModelForm in forms.py so I didn’t need to manually define each field.
3.	Write the views. I made views for listing all objects, creating a new one, showing details, and also for returning JSON/XML (both for all objects and by ID).
4.	Set up URLs. I connected each view to a path in urls.py, including /json/, /xml/, /add_product/, and product detail page.
5.	Templates. I created templates:
    - A form page with {% csrf_token %} to submit add product.
    - A product detail page to show detailed information of a single product.
8.	Validation. In the add product view. I used form.is_valid() before saving the object. If it’s invalid, the same form is shown with error messages.
9.	Check JSON/XML endpoints. I tested the URLs with Postman to make sure they return the right format.

**Do you have any feedback for the teaching assistants for Tutorial 2?**
- Fix PWS

<img width="1470" height="956" alt="Screenshot 2025-09-17 at 11 40 05" src="https://github.com/user-attachments/assets/1e5adc98-cd44-490b-8c66-38bfcac32bc0" />

<img width="1470" height="956" alt="Screenshot 2025-09-17 at 11 40 11" src="https://github.com/user-attachments/assets/afdc932f-f0d2-48ac-b15c-4d6d34a671cb" />

<img width="1470" height="956" alt="Screenshot 2025-09-17 at 11 40 18" src="https://github.com/user-attachments/assets/a7cd1383-1e27-42ad-9465-418cdfbff63e" />

<img width="1470" height="956" alt="Screenshot 2025-09-17 at 11 40 24" src="https://github.com/user-attachments/assets/8955b615-4acf-4b40-a216-e29669dd83ae" />
