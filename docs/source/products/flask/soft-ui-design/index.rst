:og:description: Flask Soft Design - Free Starter with Soft UI Design Design
:og:image: https://user-images.githubusercontent.com/51070104/168812602-e35bad42-823f-4d3e-9d13-87a6c06c5a63.png
:og:image:alt: Flask Soft Design - Free Starter with Soft UI Design Design

`Soft Design </product/soft-ui-design/flask/>`__ 
==================================================

.. title:: Flask Soft Design - Free Starter with Soft UI Design Design
.. meta::
    :description: Open-source Flask starter built on top of Bootstrap 5 and Soft Design, a pixel-perfect design from Creative-Tim.
    :keywords: soft app, flask soft app template, flask soft ui app starter, flask soft design  

Open-source Flask starter built on top of Bootstrap 5 and Soft Design, a pixel-perfect design from Creative-Tim. 
The starter provides a simple, intuitive codebase, authentication and Docker Support.

- 👉 `Flask Soft Design </product/soft-ui-design/flask/>`__ - Product Page (contains download link)
- 👉 `Flask Soft Design <https://flask-soft-ui-free.appseed-srv1.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `Soft Design </docs/templates/bootstrap/soft-ui-design.html>`__ Full Integration 
- `Bootstrap </docs/templates/bootstrap.html>`__ CSS Styling 
- Session-based Authentication
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/168812602-e35bad42-823f-4d3e-9d13-87a6c06c5a63.png
   :alt: Open-source Flask starter built on top of Bootstrap 5 and Soft Design, a pixel-perfect design from Creative-Tim.

.. include::  /_templates/components/flask-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `product page </product/soft-ui-app/flask/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/flask-soft-ui-design.git
    cd flask-soft-ui-design

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

.. code-block:: bash
    :caption: Project Files

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
            |    |         |-- *.html                # All other pages
            |    |    
            |  config.py                             # Set up the app
            |    __init__.py                         # Initialize the app
            |
            |-- requirements.txt                     # App Dependencies
            |
            |-- .env                                 # Inject Configuration via Environment
            |-- run.py                               # Start the app - WSGI gateway


.. include::  /_templates/components/flask-manual-build.rst

.. image:: https://user-images.githubusercontent.com/51070104/168812602-e35bad42-823f-4d3e-9d13-87a6c06c5a63.png
   :alt: Open-source Flask starter built on top of Bootstrap 5 and Soft Design, a pixel-perfect design from Creative-Tim.

.. include::  /_templates/components/flask-create-users.rst

.. include::  /_templates/components/generator-flask.rst
        
.. include::  /_templates/components/footer-links.rst
