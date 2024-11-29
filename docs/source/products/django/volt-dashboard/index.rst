:og:description: Django Volt Dashboard - Free Starter with Volt Bootstrap 5 Design
:og:image: https://user-images.githubusercontent.com/51070104/168843604-b026fd94-5969-4be7-81ac-5887cf0958e5.png
:og:image:alt: Django Volt Dashboard - Free Starter with Volt Bootstrap 5 Design

`Volt Dashboard </product/volt-dashboard/django/>`__ 
====================================================

.. title:: Django Volt Dashboard - Free Starter with Soft UI Dashboard Design
.. meta::
    :description: Open-source Django starter built on top of Bootstrap 5 and Volt Dashboard, a pixel-perfect design from Themesberg.
    :keywords: soft dashboard, django soft dashboard template, django soft ui dashboard starter, django soft design  

**Django Volt Dashboard** is an open-source starter built with basic modules, authentication and Docker support on top of a pixel-perfect Bootstrap 5 design.

- 👉 `Django Volt Dashboard </product/volt-dashboard/django/>`__ - Product Page (contains download link)
- 👉 `Django Volt Dashboard <https://django-volt.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst

Features
--------

- Simple, Easy-to-Extend codebase
- `Volt Dashboard </docs/templates/bootstrap/volt-dashboard.html>`__ Full Integration 
- Bootstrap 4 Styling 
- Session-based Authentication
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/168843604-b026fd94-5969-4be7-81ac-5887cf0958e5.png
   :alt: Open-source Django starter built on top of Bootstrap 5 and Volt Dashboard, a pixel-perfect design from Themesberg.

.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/volt-dashboard/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-volt-dashboard.git
    cd django-volt-dashboard

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

.. image:: https://user-images.githubusercontent.com/51070104/168843604-b026fd94-5969-4be7-81ac-5887cf0958e5.png
   :alt: Open-source Django starter built on top of Bootstrap 5 and Volt Dashboard, a pixel-perfect design from Themesberg.

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst
