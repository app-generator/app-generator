:og:description: Django Soft Design - Free Starter with Soft UI Design Design
:og:image: https://user-images.githubusercontent.com/51070104/168812602-e35bad42-823f-4d3e-9d13-87a6c06c5a63.png
:og:image:alt: Django Soft Design - Free Starter with Soft UI Design Design

`Soft Design </product/soft-ui-design/django/>`__ 
==================================================

.. title:: Django Soft Design - Free Starter with Soft UI Design Design
.. meta::
    :description: Open-source Django starter built on top of Bootstrap 5 and Soft Design, a pixel-perfect design from Creative-Tim.
    :keywords: soft app, django soft app template, django soft ui app starter, django soft design  

Open-source Django starter built on top of Bootstrap 5 and Soft Design, a pixel-perfect design from Creative-Tim. 
The starter provides a simple, intuitive codebase, authentication and Docker Support.

- 👉 `Django Soft Design </product/soft-ui-design/django/>`__ - Product Page (contains download link)
- 👉 `Django Soft Design <https://django-soft-ui-free.appseed-srv1.com/>`__ - LIVE Demo
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
   :alt: Open-source Django starter built on top of Bootstrap 5 and Soft Design, a pixel-perfect design from Creative-Tim.

.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `product page </product/soft-ui-app/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-soft-ui-design.git
    cd django-soft-ui-design

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

.. image:: https://user-images.githubusercontent.com/51070104/168812602-e35bad42-823f-4d3e-9d13-87a6c06c5a63.png
   :alt: Open-source Django starter built on top of Bootstrap 5 and Soft Design, a pixel-perfect design from Creative-Tim.

.. include::  /_templates/components/django-create-users.rst

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
