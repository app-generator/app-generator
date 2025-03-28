:og:description: Django Material Kit - Open-Source Django Template
:og:image: https://github.com/user-attachments/assets/d83d18dd-b147-4fcb-ba3a-cc4926c6d536
:og:image:alt: Django Material Kit - Open-Source Django Template

`Material Kit </product/material-kit/django/>`__
================================================

.. title:: Django Material Kit - Open-Source Django Template 
.. meta::
    :description: Open-Source Django Template crafted on top of Material Kit Design
    :keywords: django, starter, django template, material design, material dashboard, bootstrap dark-design

Free starter built on Bootstrap and Django with database, authentication, and Docker support. The Material Kit design is crafted by Creative-Tim using Bootstrap 5 Framework.

- 👉 `Django Material Kit </product/material-kit/django/>`__ - Product Page (contains download link)
- 👉 `Django Material Kit <https://django-mkit.onrender.com>`__ - LIVE Demo
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
   :alt: Django Material Kit - Open-source Starter styled with Material Kit design, crafted by Creative-Tim using Bootstrap 5 Framework. 

.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/material-kit/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-material-kit.git
    cd django-material-kit

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
        |         |-- includes                # UI Components 
        |     
        |-- requirements.txt                  # Project Dependencies
        |
        |-- env.sample                        # ENV Configuration (default values)
        |-- manage.py                         # Start the app - Django default start script


.. include::  /_templates/components/django-manual-build.rst

.. image:: https://github.com/user-attachments/assets/d83d18dd-b147-4fcb-ba3a-cc4926c6d536
   :alt: Django Material Kit - Open-source Starter styled with Material Kit design, crafted by Creative-Tim using Bootstrap 5 Framework. 

.. include::  /_templates/components/django-create-users.rst

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
