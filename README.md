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


**PBP ASSIGNMENT 4**

**What is Django's AuthenticationForm? Explain its advantages and disadvantages.**

It’s a built-in form for login with username and password.
- Advantages: ready-made, already validates credentials, integrates with Django’s authentication system, safe for basic login.
- Disadvantages: only works with username+password by default, no extra features (2FA, captcha), needs customization for modern use cases.

**What is the difference between authentication and authorization? How does Django implement the two concepts?**

Authentication = verifying identity (who you are). Example: logging in with username & password.
Authorization = checking permissions (what you can do). Example: only admins can delete posts.
In Django:
- Authentication handled by authenticate(), login(), AuthenticationMiddleware.
- Authorization handled by permissions, groups, decorators like @login_required, @permission_required.


**What are the benefits and drawbacks of using sessions and cookies in storing the state of a web application?**

Cookies: stored in the browser, small size (~4KB), simple but can be tampered with, sent with every request.
Sessions: stored on the server, cookie only keeps the session ID. More secure, can hold larger data, but requires server storage and management.
Django default: server-side sessions for security, with cookies just storing the session key.

**In web development, is the usage of cookies secure by default, or is there any potential risk that we should be aware of? How does Django handle this problem?**

Not fully. Risks include:
- XSS: attacker steals cookies through injected JavaScript.
- CSRF: cookies auto-send across sites, attacker can exploit this.
- Sniffing: cookies stolen if not encrypted via HTTPS.
- Tampering: if cookies store raw data.

Django’s protections:
- HttpOnly (not readable by JavaScript).
- Secure (only sent over HTTPS).
- SameSite (reduces CSRF).
- CSRF middleware with {% csrf_token %}.
- Session data stored on the server, not in cookies.

**Explain how you implemented the checklist above step-by-step (not just following the tutorial).**
1. Create a new Django project and an accounts app to keep authentication code organized.
2. Add your accounts app to INSTALLED_APPS and keep Django’s auth and sessions apps enabled so you have User and session support.
3. Ensure SecurityMiddleware, SessionMiddleware, CsrfViewMiddleware, and AuthenticationMiddleware are present in MIDDLEWARE so sessions, CSRF protection, and request.user work.
4. Make a login template that posts via POST, renders the form fields, and includes {% csrf_token %} to protect from CSRF.
5. Use Django’s AuthenticationForm or LoginView to validate credentials with authenticate() and avoid reimplementing basic checks.
6. In your login view call login(request, user) after validation to create the server-side session and rotate the session key.
7. Add an optional “remember me” checkbox and call request.session.set_expiry(0) for non-remembered sessions or set_expiry(seconds) for custom expiry.
8. Secure cookies in settings.py by setting SESSION_COOKIE_SECURE=True, SESSION_COOKIE_HTTPONLY=True, and SESSION_COOKIE_SAMESITE='Lax' (and CSRF_COOKIE_SECURE=True).
9. Protect pages with @login_required and use @permission_required or user.has_perm() for fine-grained authorization checks.
10. Add brute-force protections (rate limiting or packages like django-axes) to prevent repeated login attempts.
11. Write tests for login success/failure, protected-view redirects, and session expiry to catch regressions early.
12. Deploy with DEBUG=False, ALLOWED_HOSTS configured, HTTPS enabled, and a secure SECRET_KEY to ensure production safety.

**PBP ASSIGNMENT 5**

**Urutan Prioritas CSS Selector**
CSS memilih aturan berdasarkan urutan prioritas (specificity):
- !important selalu menang, meskipun biasanya dihindari.
- Inline style (atribut style langsung di elemen) memiliki prioritas tinggi.
- ID selector lebih kuat dibanding class.
- Class, attribute, pseudo-class lebih kuat dibanding elemen biasa.
- Element dan pseudo-element paling rendah prioritasnya.
- Universal selector dan default browser berada di urutan terakhir.

Jika ada aturan dengan prioritas yang sama, aturan yang ditulis paling akhir akan dipakai.

**Pentingnya Responsive Design**
Responsive design penting karena pengguna mengakses web dari berbagai perangkat dengan ukuran layar berbeda. Dengan desain responsif, tampilan dapat menyesuaikan sehingga lebih mudah digunakan dan nyaman di semua perangkat. Hal ini meningkatkan pengalaman pengguna, membantu optimasi SEO, serta mempermudah pengelolaan karena hanya satu basis kode yang dipelihara.
Contoh aplikasi yang sudah menerapkan responsive design adalah GitHub dan Tokopedia, di mana tampilan otomatis menyesuaikan saat layar diperkecil. Sebaliknya, banyak sistem akademik atau aplikasi internal lama masih menggunakan layout fixed-width, sehingga tidak nyaman diakses melalui ponsel.

**Perbedaan Margin, Border, dan Padding**
- Content adalah isi dari elemen seperti teks atau gambar.
- Padding adalah ruang antara content dan border.
- Border adalah garis yang mengelilingi padding.
- Margin adalah ruang di luar border yang memisahkan elemen dengan elemen lain.

Secara sederhana: content berada di tengah, kemudian dikelilingi padding, lalu border, dan di luar semuanya ada margin.

**Flexbox dan Grid Layout**
- Flexbox digunakan untuk mengatur tata letak satu dimensi, baik secara baris maupun kolom. Flexbox sangat berguna untuk menyusun elemen yang berderet seperti navbar, card, atau tombol.
- Grid digunakan untuk tata letak dua dimensi yang melibatkan baris dan kolom sekaligus. Grid cocok untuk membuat struktur halaman utama, galeri gambar, atau layout kompleks dengan pembagian ruang yang jelas.

**Step-by-Step Implementasi**	
1. Menyusun struktur HTML dasar sesuai kebutuhan konten.
2. Menambahkan gaya dasar CSS seperti warna, ukuran teks, dan jarak.
3. Menerapkan box model dengan margin, border, dan padding agar elemen memiliki ruang yang rapi.
4. Mengatur layout menggunakan Flexbox atau Grid sesuai kebutuhan (misalnya Flexbox untuk navbar, Grid untuk layout halaman).
5. Menambahkan media query agar tampilan menyesuaikan di layar kecil maupun besar.
6. Menguji tampilan pada berbagai ukuran layar untuk memastikan desain responsif.
7. Merefaktor kode agar lebih konsisten dan mudah dipelihara.
