:og:description: Django Material Dashboard - Open-Source Django Template
:og:image: https://github.com/user-attachments/assets/dba1a100-3309-400c-99bc-6ba707697509
:og:image:alt: Django Material Dashboard - Open-Source Django Template

`Material Dashboard </product/material-dashboard/django/>`__
===================================================================

.. title:: Django Material Dashboard - Open-Source Django Template 
.. meta::
    :description: Open-Source Django Template crafted on top of Material Dashboard Design
    :keywords: django, starter, django template, material design, material dashboard, bootstrap dark-design

Free starter built on Bootstrap and Django with database, authentication, and Docker support. The Material Dashboard design is crafted by Creative-Tim using Bootstrap 5 Framework.

- 👉 `Django Material Dashboard </product/material-dashboard/django/>`__ - Product Page (contains download link)
- 👉 `Django Material Dashboard <https://django-material-dash2.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `Material Dashboard </docs/templates/bootstrap/material-dashboard.html>`__ Full Integration 
- Bootstrap 4 Styling 
- Session-based Authentication
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/user-attachments/assets/dba1a100-3309-400c-99bc-6ba707697509
   :alt: Django Material Dashboard - Open-source Starter styled with Material Dashboard design 


.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/material-dashboard/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-material-dashboard.git
    cd django-material-dashboard

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


.. image:: https://github.com/user-attachments/assets/dba1a100-3309-400c-99bc-6ba707697509
   :alt: Django Material Dashboard - Open-source Starter styled with Material Dashboard design 

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst
