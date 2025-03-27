:og:description: Flask Material Kit - Open-Source Flask Template
:og:image: https://github.com/user-attachments/assets/d83d18dd-b147-4fcb-ba3a-cc4926c6d536
:og:image:alt: Flask Material Kit - Open-Source Flask Template

`Material Kit </product/material-kit/flask/>`__
===================================================================

.. title:: Flask Material Kit - Open-Source Flask Template 
.. meta::
    :description: Open-Source Flask Template crafted on top of Material Kit Design
    :keywords: flask, starter, flask template, material design, material dashboard, bootstrap dark-design

Free starter built on Bootstrap and Flask with database, authentication, and Docker support. The Material Kit design is crafted by Creative-Tim using Bootstrap 5 Framework.

- 👉 `Flask Material Kit </product/material-kit/flask/>`__ - Product Page (contains download link)
- 👉 `Flask Material Kit <https://flask-material-kit.appseed-srv1.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `Material Kit </docs/templates/bootstrap/material-kit.html>`__ Full Integration 
- `Bootstrap </docs/templates/bootstrap.html>`__ CSS Styling 
- Session-based Authentication
- DB Persistence: SQLite/MySql/PostgreSQL
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/user-attachments/assets/d83d18dd-b147-4fcb-ba3a-cc4926c6d536
   :alt: Flask Material Kit - Open-source Starter styled with Material Kit design, crafted by Creative-Tim using Bootstrap 5 Framework. 

.. include::  /_templates/components/flask-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/material-kit/flask/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/flask-material-kit.git
    cd flask-material-kit

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

.. image:: https://github.com/user-attachments/assets/d83d18dd-b147-4fcb-ba3a-cc4926c6d536
   :alt: Flask Material Kit - Open-source Starter styled with Material Kit design, crafted by Creative-Tim using Bootstrap 5 Framework. 

.. include::  /_templates/components/flask-create-users.rst

.. include::  /_templates/components/generator-flask.rst
        
.. include::  /_templates/components/footer-links.rst
