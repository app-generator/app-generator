:og:description: Django Pixel UI - Open-Source Django Template
:og:image: https://user-images.githubusercontent.com/51070104/168753915-d61b2f97-57b2-4d14-a774-d217d120ff62.png
:og:image:alt: Django Pixel UI - Open-Source Django Template

`Pixel UI </product/pixel-bootstrap/django/>`__
===============================================

.. title:: Django Pixel UI - Open-Source Django Template 
.. meta::
    :description: Open-Source Django Template crafted on top of Pixel UI Design
    :keywords: django, starter, django template, material design, material dashboard, bootstrap dark-design

Free starter built on Bootstrap and Django with database, authentication, and Docker support. The Pixel UI design is crafted by Themesberg using Bootstrap 5 Framework.

- 👉 `Django Pixel UI </product/pixel-bootstrap/django/>`__ - Product Page (contains download link)
- 👉 `Django Pixel UI <https://django-pixel-lite.appseed-srv1.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `Pixel UI </docs/templates/bootstrap/pixel-bootstrap.html>`__ Full Integration 
- Bootstrap 4 Styling 
- Session-based Authentication
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/168753915-d61b2f97-57b2-4d14-a774-d217d120ff62.png
   :alt: Django Pixel UI - Open-source Starter styled with Pixel UI design, crafted by Themesberg using Bootstrap 5 Framework. 


.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/pixel-bootstrap/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-pixel.git
    cd django-pixel

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

.. image:: https://user-images.githubusercontent.com/51070104/168753915-d61b2f97-57b2-4d14-a774-d217d120ff62.png
   :alt: Django Pixel UI - Open-source Starter styled with Pixel UI design, crafted by Themesberg using Bootstrap 5 Framework. 

.. include::  /_templates/components/django-create-users.rst

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
