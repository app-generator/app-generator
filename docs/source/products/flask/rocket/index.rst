:og:description: Flask Rocket - Open-source Starter styled with Rocket design
:og:image: https://github.com/user-attachments/assets/d7527d5e-046c-4679-8f72-525290a5edd5
:og:image:alt: Flask Rocket - Open-source Starter styled with Rocket design

`Rocket </product/rocket/flask/>`__ 
=========================================

.. title:: Flask Rocket - Open-source Starter styled with Tailwind/Flowbite
.. meta::
    :description: Open-source Flask Template styled with Tailwind/Flowbite
    :keywords: rocket starter, flask rocket starter, rocket flask template, flask tailwind, flask flowbite  

**Flask Rocket** is an open-source starter built with basic modules, authentication, data tables, charts, API and Docker support.
The product UI is styled with **Flowbite**, an open source collection of UI components built with the utility classes from Tailwind CSS. 

- 👉 `Flask Rocket </product/rocket/flask/>`__ - Product Page (contains download link)
- 👉 `Flask Rocket <https://rocket-flask.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- Styling: Flowbite/Tailwind
- Extended User Model
- ApexJS Charts
- DataTables 
- API
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/user-attachments/assets/d7527d5e-046c-4679-8f72-525290a5edd5
   :alt: Flask Rocket - Open-source Starter styled with Flowbite/Tailwind 


.. include::  /_templates/components/flask-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `product page </product/rocket/flask/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/rocket-flask.git
    cd rocket-flask

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

.. image:: https://github.com/user-attachments/assets/d7527d5e-046c-4679-8f72-525290a5edd5
   :alt: Homepage Flask Rocket - open-source starter built on top of Flowbite/Tailwind

.. include::  /_templates/components/flask-create-users.rst

.. include::  /_templates/components/generator-flask.rst
        
.. include::  /_templates/components/footer-links.rst
