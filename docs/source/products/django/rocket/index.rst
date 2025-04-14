:og:description: Django Rocket - Open-source Starter styled with Rocket design
:og:image: https://github.com/user-attachments/assets/d7527d5e-046c-4679-8f72-525290a5edd5
:og:image:alt: Django Rocket - Open-source Starter styled with Rocket design

`Rocket </product/rocket/django/>`__ 
====================================

.. title:: Django Rocket - Open-source Starter styled with Tailwind/Flowbite
.. meta::
    :description: Open-source Django Template styled with Tailwind/Flowbite
    :keywords: rocket starter, django rocket starter, rocket django template, django tailwind, django flowbite  

Django `Rocket </product/rocket/>`__ is an open-source starter built with basic modules, authentication, data tables, charts, API and Docker support.
The product UI is styled with **Flowbite**, an open source collection of UI components built with the utility classes from Tailwind CSS. 

- 👉 `Django Rocket </product/rocket/django/>`__ - Product Page (contains download link)
- 👉 `Django Rocket <https://rocket-django.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `Rocket </product/rocket/>`__ Design Integration 
- Styling: Flowbite/Tailwind
- Extended User Model
- ApexJS Charts
- DataTables 
- API
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/user-attachments/assets/d7527d5e-046c-4679-8f72-525290a5edd5
   :alt: Django Rocket - Open-source Starter styled with Flowbite/Tailwind 


.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `product page </product/rocket/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/rocket-django.git
    cd rocket-django

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

.. code-block:: bash
    :caption: Project Files

    < Project ROOT > 
        |
        |
        |-- core/                            
        |    |-- settings.py                  # Project Configuration  
        |    |-- urls.py                      # Project Routing
        |
        |-- home/
        |    |-- views.py                     # APP Views 
        |    |-- urls.py                      # APP Routing
        |    |-- models.py                    # APP Models 
        |    |-- tests.py                     # Tests  
        |    |-- templates/                   # Theme Customisation 
        |         |-- includes                # 
        |              |-- custom-footer.py   # Custom Footer      
        |     
        |-- requirements.txt                  # Project Dependencies
        |
        |-- env.sample                        # ENV Configuration (default values)
        |-- manage.py                         # Start the app - Django default start script


Install Tailwind/Flowbite
-------------------------

Tested with **Node** `v18.20.0` (use at least this version or above)

.. code-block:: bash

    $ npm install
    $ npm run dev
    $ npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css --watch # DEVELOPMENT (LIVE reload)
    $ npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css         # PRODUCTION    

.. include::  /_templates/components/django-manual-build.rst

.. image:: https://github.com/user-attachments/assets/d7527d5e-046c-4679-8f72-525290a5edd5
   :alt: Homepage Django Rocket - open-source starter built on top of Flowbite/Tailwind

.. include::  /_templates/components/django-create-users.rst

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
