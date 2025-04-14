:og:description: Flask Rocket PRO - Premium Starter built on top of Flowbite/Tailwind
:og:image: https://github.com/user-attachments/assets/d60069f3-be43-460f-ba03-0da92276f87c
:og:image:alt: Premium Flask starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Flowbite/Tailwind Design.

`Rocket PRO </product/rocket-pro/flask/>`__ 
============================================

.. title:: Flask Rocket PRO - Premium Starter built on top of Rocket     
.. meta::
    :description: Premium Flask starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Rocket Design.
    :keywords: flask, flask pro template, flask pro starter, rocket pro, rocket flask 

Premium Flask starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Flowbite/Tailwind Design.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 `Flask Rocket PRO </product/rocket-pro/flask/>`__ - Product Page (contains download link)
- 👉 `Flask Rocket PRO <https://rocket-flask-pro.onrender.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
---------

- Simple, Easy-to-Extend codebase
- `Rocket </product/rocket/>`__ Design Integration 
- Styling: Flowbite/Tailwind
- Extended User Model
- ApexJS Charts
- DataTables 
- API
- Media Files Manager
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/user-attachments/assets/d60069f3-be43-460f-ba03-0da92276f87c
   :alt: Flask Rocket PRO - Premium Starter built on top of Flowbite/Tailwind


.. include::  /_templates/components/flask-prerequisites.rst

Download Source Code 
--------------------

Access the `product page </product/rocket-pro/flask/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow thhe installation steps:

.. code-block:: shell

    unzip rocket-flask-pro.zip
    cd rocket-flask-pro

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


Install Tailwind/Flowbite
-------------------------

Tested with **Node** `v18.20.0` (use at least this version or above)

.. code-block:: bash

    $ npm install
    $ npm run dev # DEVELOPMENT (LIVE reload)
    $ npm run dev # Production 

.. include::  /_templates/components/flask-manual-build.rst

.. image:: https://github.com/user-attachments/assets/d60069f3-be43-460f-ba03-0da92276f87c
   :alt: Flask Rocket PRO - Premium Starter built on top of Flowbite/Tailwind


.. include::  /_templates/components/flask-create-users.rst

