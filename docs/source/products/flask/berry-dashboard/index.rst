:og:description: Flask Berry Dashboard - Open-Source Flask Template
:og:image: https://github.com/user-attachments/assets/71c3fed0-58cb-41e6-aa97-8686a10ede45
:og:image:alt: Flask Berry Dashboard - Open-Source Flask Template

`Berry </product/berry-dashboard/flask/>`__
============================================

.. title:: Flask Berry Dashboard - Open-Source Flask Template 
.. meta::
    :description: Open-Source Flask Template crafted on top of Berry Dashboard Design
    :keywords: flask, starter, flask template, datta able, bootstrap 4, flask template

**Open-Source Flask Template** built with a minimum set of features on top of `Berry </product/berry-dashboard/>`__, a modern dashboard design from `CodedThemes </agency/codedthemes/>`__. 
This template can be used to start a new project quickly by adding new features on top of the existing ones or simply for learning purposes.

- 👉 `Berry Dashboard Flask </product/berry-dashboard/flask/>`__ - Product Page (contains download link)
- 👉 `Berry Dashboard Flask <https://flask-berry.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord  

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- Simple, Easy-to-Extend codebase, `Blueprint Pattern </blog/flask-blueprints-a-developers-guide/>`__
- Up-to-date Dependencies
- `Berry Dashboard </product/berry-dashboard/>`__ Design Integration 
- `Bootstrap </docs/templates/bootstrap.html>`__ CSS Styling 
- Authentication: Session Based, GitHub OAuth
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. figure:: https://github.com/user-attachments/assets/71c3fed0-58cb-41e6-aa97-8686a10ede45
   :alt: Berry Dashboard - Open-Source Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-prerequisites.rst


Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/berry-dashboard/flask/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/flask-berry-dashboard.git
    cd flask-berry-dashboard

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

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

.. figure:: https://github.com/user-attachments/assets/71c3fed0-58cb-41e6-aa97-8686a10ede45
   :alt: Berry Dashboard - Open-Source Seed project powered by Flask - actively supported by App Generator 

.. include::  /_templates/components/flask-create-users.rst

.. include::  /_templates/components/generator-flask.rst

.. include::  /_templates/components/footer-links.rst
