:og:description: Flask Berry Dashboard PRO - Premium Flask Template
:og:image: https://github.com/user-attachments/assets/a8225bbd-86cb-4fd8-b8c4-8ac87197e4ba
:og:image:alt: Flask Berry Dashboard PRO - Premium Flask Template

`Berry PRO </product/berry-dashboard/flask/>`__
===============================================

.. title:: Flask Berry Dashboard PRO - Premium Flask Template 
.. meta::
    :description: Premium Flask Template crafted on top of Berry Dashboard Design
    :keywords: flask, starter, flask template, datta able, bootstrap 5, flask template

**Premium Flask Template** built with a minimum set of features on top of **Berry Dashboard PRO**, a premium dashboard design from CodedThemes. 
This template can be used to start a new project quickly by adding new features on top of the existing ones or simply for learning purposes.

- 👉 `Berry Dashboard Flask </product/berry-dashboard-pro/flask/>`__ - Product Page (contains download link)
- 👉 `Berry Dashboard Flask <https://flask-berry-pro.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord  

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- `Up-to-date dependencies`
- DB Persistence: SQLite (default), can be used with MySql, PgSql
    - Silent fallback to `SQLite`  
- DB Tools: SQLAlchemy ORM, `Flask-Migrate`
- Authentication, Session Based
- Docker, Page Compression via `Flask-Minify`
- CI/CD flow via `Render`


.. figure:: https://github.com/user-attachments/assets/a8225bbd-86cb-4fd8-b8c4-8ac87197e4ba
   :alt: Berry Dashboard - Premium Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/berry-dashboard-pro/flask/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow thhe installation steps:

.. code-block:: shell

    unzip flask-berry-dashboard-pro.zip
    cd flask-berry-dashboard-pro

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

- **Core**: holds the project settings 
- **Home**: the application that integrates the Berry Dashboard Design 
- **Api**: the generated API 

.. code-block:: bash   

    < PROJECT ROOT >
        |
        |-- apps/
        |    |
        |    |-- home/                           # A simple app that serve HTML files
        |    |    |-- routes.py                  # Define app routes
        |    |
        |    |-- authentication/                 # Handles auth routes (login and register)
        |    |    |-- routes.py                  # Define authentication routes  
        |    |    |-- models.py                  # Defines models  
        |    |    |-- forms.py                   # Define auth forms (login and register) 
        |    |
        |    |-- static/
        |    |    |-- <css, JS, images>          # CSS files, Javascripts files
        |    |
        |    |-- templates/                      # Templates used to render pages
        |    |    |-- includes/                  # HTML chunks and components
        |    |    |    |-- navigation.html       # Top menu component
        |    |    |    |-- sidebar.html          # Sidebar component
        |    |    |    |-- footer.html           # App Footer
        |    |    |    |-- scripts.html          # Scripts common to all pages
        |    |    |
        |    |    |-- layouts/                   # Master pages
        |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
        |    |    |    |-- base.html             # Used by common pages
        |    |    |
        |    |    |-- accounts/                  # Authentication pages
        |    |    |    |-- login.html            # Login page
        |    |    |    |-- register.html         # Register page
        |    |    |
        |    |    |-- home/                      # UI Kit Pages
        |    |         |-- index.html            # Index page
        |    |         |-- 404-page.html         # 404 page
        |    |         |-- .html                 # All other pages
        |    |    
        |  config.py                             # Set up the app
        |    __init__.py                         # Initialize the app
        |
        |-- requirements.txt                     # App Dependencies
        |
        |-- .env                                 # Inject Configuration via Environment
        |-- run.py                               # Start the app - WSGI gateway

.. include::  /_templates/components/flask-manual-build.rst

.. figure:: https://github.com/user-attachments/assets/a8225bbd-86cb-4fd8-b8c4-8ac87197e4ba
   :alt: Berry Dashboard - Premium Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-create-users.rst
