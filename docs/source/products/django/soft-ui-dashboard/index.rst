:og:description: Django Soft Dashboard - Free Starter with Soft UI Dashboard Design
:og:image: https://github.com/user-attachments/assets/2dd7adf3-bf5f-4894-b585-3696e7a8606f
:og:image:alt: Django Soft Dashboard - Free Starter with Soft UI Dashboard Design

`Soft Dashboard </product/soft-ui-dashboard/django/>`__ 
=======================================================

.. title:: Django Soft Dashboard - Free Starter with Soft UI Dashboard Design
.. meta::
    :description: Open-source Django starter built on top of Bootstrap 5 and Soft Dashboard, a pixel-perfect design from Creative-Tim.
    :keywords: soft dashboard, django soft dashboard template, django soft ui dashboard starter, django soft design  

Open-source Django starter built on top of Bootstrap 5 and Soft Dashboard, a pixel-perfect design from Creative-Tim. 
The starter provides a simple, intuitive codebase, authentication and Docker Support.

- 👉 `Django Soft Dashboard </product/soft-ui-dashboard/django/>`__ - Product Page (contains download link)
- 👉 `Django Soft Dashboard <https://django-soft-dash.onrender.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `Soft Dashboard </docs/templates/bootstrap/soft-ui-dashboard.html>`__ Full Integration 
- `Bootstrap </docs/templates/bootstrap.html>`__ CSS Styling 
- Session-based Authentication
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/user-attachments/assets/2dd7adf3-bf5f-4894-b585-3696e7a8606f
   :alt: Open-source Django starter built on top of Bootstrap 5 and Soft Dashboard, a pixel-perfect design from Creative-Tim.

.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `product page </product/soft-ui-dashboard/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-soft-ui-dashboard.git
    cd django-soft-ui-dashboard

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

.. image:: https://github.com/user-attachments/assets/2dd7adf3-bf5f-4894-b585-3696e7a8606f
   :alt: Open-source Django starter built on top of Bootstrap 5 and Soft Dashboard, a pixel-perfect design from Creative-Tim.

.. include::  /_templates/components/django-create-users.rst

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
