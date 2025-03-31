:og:description: Flask Atlantis Dark PRO - Premium Starter built on top of Atlantis Dark
:og:image: https://user-images.githubusercontent.com/51070104/212669274-3eef24b4-7c19-4557-99c5-e24ae5b14a5b.png
:og:image:alt: Premium Flask starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Atlantis Dark Design.

`Atlantis Dark PRO </product/atlantis-dark-pro/flask/>`__ 
==========================================================

.. title:: Flask Atlantis Dark PRO - Premium Starter built on top of Atlantis Dark     
.. meta::
    :description: Premium Flask starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Atlantis Dark Design.
    :keywords: flask, flask pro template, flask pro starter, argon-dashboard pro, argon-dashboard flask 

Premium Flask starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Atlantis Dark Design.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 `Flask Atlantis Dark PRO </product/atlantis-dark-pro/flask/>`__ - Product Page (contains download link)
- 👉 `Flask Atlantis Dark PRO <https://flask-atlantis-dark-pro.appseed-srv1.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
---------

- Simple, Easy-to-Extend codebase
- **Atlantis Design - PRO Version**
- Bootstrap 4 Styling 
- Session-based Authentication
- DB Persistence: SQLite/MySql/PostgreSQL
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/212669274-3eef24b4-7c19-4557-99c5-e24ae5b14a5b.png
   :alt: Flask Atlantis Dark PRO - Premium Starter built on top of Atlantis Dark


Download Source Code 
--------------------

Access the `product page </product/atlantis-dark-pro/flask/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

    unzip flask-atlantis-dark-pro.zip
    cd flask-atlantis-dark-pro

Once the source code is unzipped, the next step is to start it and use provided features. 

.. code-block:: bash
    :caption: Project Files

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
