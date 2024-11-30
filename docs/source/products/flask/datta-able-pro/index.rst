:og:description: Flask Datta Able PRO - Premium Flask Template
:og:image: https://user-images.githubusercontent.com/51070104/170474361-a58da82b-fff9-4a59-81a8-7ab99f478f48.png
:og:image:alt: Flask Datta Able PRO - Premium Flask Template

`Datta Able PRO </product/datta-able/flask/>`__
===============================================

.. title:: Flask Datta Able PRO - Premium Flask Template 
.. meta::
    :description: Premium Flask Template crafted on top of Datta Able Design
    :keywords: flask, starter, flask template, datta able, bootstrap 4, flask template

**Premium Flask Template** built with a minimum set of features on top of **Datta Able**, a modern dashboard design from CodedThemes. 
This template can be used to start a new project quickly by adding new features on top of the existing ones or simply for learning purposes.

- 👉 `Datta Able Flask </product/datta-able-pro/flask/>`__ - Product Page (contains download link)
- 👉 `Datta Able Flask <https://flask-datta-pro.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord  

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- `Up-to-date dependencies`
- Apps
  - DataTables
  - API
  - Charts
  - Media Files Manager
- DB Persistence: SQLite (default), can be used with MySql, PgSql
  - Silent fallback to `SQLite`  
- `DB Tools`: SQLAlchemy ORM, `Flask-Migrate`
- `Authentication`, Session Based
- `Docker`, Page Compression via `Flask-Minify`
- `CI/CD` flow via `Render`

.. figure:: https://user-images.githubusercontent.com/51070104/170474361-a58da82b-fff9-4a59-81a8-7ab99f478f48.png
   :alt: Datta Able - Premium Seed project powered by Flask - actively supported by App Generator


.. include::  /_templates/components/flask-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/datta-able-pro/flask/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow thhe installation steps:

.. code-block:: shell

    unzip flask-datta-able-pro.zip
    cd flask-datta-able-pro

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

- **Core**: holds the project settings 
- **Home**: the application that integrates the Datta Able Design 
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

.. figure:: https://user-images.githubusercontent.com/51070104/170474361-a58da82b-fff9-4a59-81a8-7ab99f478f48.png
   :alt: Datta Able - Premium Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-create-users.rst
