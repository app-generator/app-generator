:og:description: Flask Volt Dashboard - Open-Source Flask Template
:og:image: https://user-images.githubusercontent.com/51070104/168842202-9b80a957-a375-4e6d-8247-2cc459267a86.png
:og:image:alt: Flask Volt Dashboard - Open-Source Flask Template

`Volt Dashboard </product/volt-dashboard/flask/>`__
====================================================

.. title:: Flask Volt Dashboard - Open-Source Flask Template 
.. meta::
    :description: Open-Source Flask Template crafted on top of Volt Dashboard Design
    :keywords: flask, starter, flask template, volt dashboard, bootstrap 5, flask template

**Open-Source Flask Template** built with a minimum set of features on top of **Volt Dashboard** Bootstrap Design. 
This template can be used to start a new project quickly by adding new features on top of the existing ones or simply for learning purposes.

- 👉 `Volt Dashboard Flask </product/volt-dashboard/flask/>`__ - Product Page (contains download link)
- 👉 `Volt Dashboard Flask <https://flask-volt-dashboard.appseed-srv1.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord  

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- Simple, Easy-to-Extend codebase, `Blueprint Pattern </blog/flask-blueprints-a-developers-guide/>`__
- Up-to-date Dependencies
- `Volt Dashboard </docs/templates/bootstrap/volt-dashboard.html>`__ Full Integration 
- `Bootstrap </docs/templates/bootstrap.html>`__ CSS Styling 
- Authentication: Session Based
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- `Dynamic DataTables <https://flask-volt.onrender.com/dynamic-dt/products>`__ - manage data without coding
- Docker 
- CI/CD integration for Render 

.. figure:: https://github.com/user-attachments/assets/2c84a3fa-347b-4fb7-9dc6-e5d3459f582e
   :alt: Volt Dashboard - Open-Source Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-prerequisites.rst


Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/volt-dashboard/flask/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/flask-volt-dashboard.git
    cd flask-volt-dashboard

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

- **Core**: holds the project settings 
- **Home**: the application that integrates the Volt Dashboard Design 
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

.. figure:: https://github.com/user-attachments/assets/2c84a3fa-347b-4fb7-9dc6-e5d3459f582e
   :alt: Volt Dashboard - Open-Source Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-create-users.rst

.. include::  /_templates/components/generator-flask.rst

.. include::  /_templates/components/footer-links.rst
