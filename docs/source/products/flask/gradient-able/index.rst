:og:description: Flask Gradient Able - Open-Source Flask Template
:og:image: https://user-images.githubusercontent.com/51070104/171583187-c4ca1bef-b535-458e-9250-8d62ba1f5b30.png
:og:image:alt: Flask Gradient Able - Open-Source Flask Template

`Gradient Able </product/gradient-able/flask/>`__
=================================================

.. title:: Flask Gradient Able - Open-Source Flask Template 
.. meta::
    :description: Open-Source Flask Template crafted on top of Gradient Able Design
    :keywords: flask, starter, flask template, gradient able, bootstrap 4, flask template

**Open-Source Flask Template** built with a minimum set of features on top of **Gradient Able**, a modern dashboard design from CodedThemes. 
This template can be used to start a new project quickly by adding new features on top of the existing ones or simply for learning purposes.

- 👉 `Gradient Able Flask </product/gradient-able/flask/>`__ - Product Page (contains download link)
- 👉 `Gradient Able Flask <flask-gradient-able.appseed-srv1.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord  

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- Simple, Easy-to-Extend codebase, `Blueprint Pattern </blog/flask-blueprints-a-developers-guide/>`__
- Up-to-date Dependencies
- `Gradient Able </docs/templates/bootstrap/gradient-able.html>`__ Integration 
- `Bootstrap </docs/templates/bootstrap.html>`__ CSS Styling 
- Authentication: Session Based
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- `Dynamic DataTables <https://flask-gradient-demo.onrender.com/dynamic-dt/products>`__ - manage data without coding
- Docker 
- CI/CD integration for Render 

.. figure:: https://user-images.githubusercontent.com/51070104/171583187-c4ca1bef-b535-458e-9250-8d62ba1f5b30.png
   :alt: Gradient Able - Open-Source Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-prerequisites.rst


Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/gradient-able/flask/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/flask-gradient-able.git
    cd flask-gradient-able

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

- **Core**: holds the project settings 
- **Home**: the application that integrates the Gradient Able Design 
- **Api**: the generated API 

.. code-block:: bash   

    < PROJECT ROOT >
        |
        |-- apps/
        |    |
        |    |-- authentication/                 # Handles auth routes (login and register)
        |    |    |-- routes.py                  # Define authentication routes  
        |    |    |-- models.py                  # Defines models  
        |    |    |-- forms.py                   # Define auth forms (login and register) 
        |    |
        |    |-- home/                           # A simple app that serve HTML files
        |    |    |-- routes.py                  # Define app routes
        |    |
        |    |-- dyn_dt/                          # Dynamic Data Tables Module
        |    |    |-- routes.py                  # Define app routes
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

.. figure:: https://user-images.githubusercontent.com/51070104/171583187-c4ca1bef-b535-458e-9250-8d62ba1f5b30.png
   :alt: Flask Gradient Able - Open-Source Flask Template, actively supported by App Generator

.. include::  /_templates/components/flask-create-users.rst

.. include::  /_templates/components/generator-flask.rst

.. include::  /_templates/components/footer-links.rst