:og:description: Django AdminLTE - Open-source Starter styled with AdminLTE design
:og:image: https://app-generator.dev/static/product/adminlte/django/top.png
:og:image:alt: Django AdminLTE - Open-source Starter styled with AdminLTE design

`AdminLTE </product/adminlte/django/>`__ 
=========================================

.. title:: Django AdminLTE - Open-source Starter styled with AdminLTE design     
.. meta::
    :description: Open-source Django Template styled with AdminLTE design  
    :keywords: django, django template, django starter, adminlte, adminlte django 

**Django AdminLTE** is an open-source starter built with basic modules, authentication and Docker support on top of the AdminLTE Design.

- 👉 `Django AdminLTE </product/adminlte/django/>`__ - Product Page (contains download link)
- 👉 `Django AdminLTE <https://adminlte-django.appseed-srv1.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `AdminLTE </docs/templates/bootstrap/adminlte.html>`__ Full Integration 
- Bootstrap 4 Styling 
- Session-based Authentication
- DB Persistence: SQLite/MySql/PostgreSQL
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/app-generator/django-adminlte/assets/51070104/8f0c396d-2f33-46b9-9689-2982c987399d
   :alt: Django AdminLTE - Open-source Starter styled with AdminLTE design 

.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `product page </product/adminlte/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-adminlte.git
    cd django-adminlte

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


.. include::  /_templates/components/django-manual-build.rst

.. image:: https://github.com/user-attachments/assets/4d5f6b17-3b80-469b-ade7-2b8e318f829d
   :alt: Homepage Django AdminLTE - open-source starter built on top of AdminLTE 

.. include::  /_templates/components/django-create-users.rst

Contents
--------

.. toctree::
   :maxdepth: 1

   source-code 
   deployment
