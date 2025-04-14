:og:description: Flask Atlantis Dark - Open-Source Flask Template
:og:image: https://user-images.githubusercontent.com/51070104/172799909-4cbc8eed-fdde-4408-ab61-123f235212d0.png
:og:image:alt: Flask Atlantis Dark - Open-Source Flask Template

`Atlantis Dark </product/atlantis-dark/flask/>`__
=================================================

.. title:: Flask Atlantis Dark - Open-Source Flask Template 
.. meta::
    :description: Open-Source Flask Template crafted on top of Atlantis Dark Design
    :keywords: flask, starter, flask template, atlantis-dark, bootstrap 4, flask template

**Open-Source Flask Template** built with a minimum set of features on top of `Atlantis Dark </product/atlantis-dark/>`__ Bootstrap Design. 
This template can be used to start a new project quickly by adding new features on top of the existing ones or simply for learning purposes.

- 👉 `Atlantis Dark Flask </product/atlantis-dark/flask/>`__ - Product Page (contains download link)
- 👉 `Atlantis Dark Flask <https://flask-atlantis-dark.appseed-srv1.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord  

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- Simple, Easy-to-Extend codebase, `Blueprint Pattern </blog/flask-blueprints-a-developers-guide/>`__
- Up-to-date Dependencies
- `Atlantis Dark </product/atlantis-dark/>`__ Design Integration 
- `Bootstrap </docs/templates/bootstrap.html>`__ CSS Styling 
- Authentication: Session Based
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. figure:: https://user-images.githubusercontent.com/51070104/172799909-4cbc8eed-fdde-4408-ab61-123f235212d0.png
   :alt: Atlantis Dark - Open-Source Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-prerequisites.rst


Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/atlantis-dark/flask/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/flask-atlantis-dark.git
    cd flask-atlantis-dark

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

.. figure:: https://user-images.githubusercontent.com/51070104/172799909-4cbc8eed-fdde-4408-ab61-123f235212d0.png
   :alt: Atlantis Dark - Open-Source Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-create-users.rst

.. include::  /_templates/components/generator-flask.rst

.. include::  /_templates/components/footer-links.rst
