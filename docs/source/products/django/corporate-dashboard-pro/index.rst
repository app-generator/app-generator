:og:description: Django Corporate Dashboard PRO - Premium Starter built on top of Corporate Design
:og:image: https://github.com/user-attachments/assets/e2385055-3110-4842-b679-36c9a1060e48
:og:image:alt: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Corporate DesignMaterial Dashboard Design.

`Corporate PRO </product/corporate-dashboard-pro/django/>`__ 
============================================================

.. title:: Django Corporate Dashboard PRO - Premium Starter built on top of Corporate UI Dashboard     
.. meta::
    :description: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with `Corporate PRO </product/corporate-dashboard/>`__ Design.
    :keywords: django, django pro template, django pro starter, material-dashboard pro, material-dashboard django 

Premium Django starter built with Database, DB Tools, and `Corporate PRO </product/corporate-dashboard/>`__ Design (PRO Version) 
released by `Creative-Tim </agency/creative-tim/>`__ using Bootstrap 5 Framework.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 `Django Corporate Dashboard PRO </product/corporate-dashboard-pro/django/>`__ - Product Page (contains download link)
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- **Simple, Easy-to-Extend** Codebase
- **Corporate Dashboard Design**, the PRO version. Section covered:
    - **Admin section** (reserved for superusers)
    - **Authentication**: `Django.contrib.AUTH`, Registration
    - **All Pages** available in for ordinary users 
- **Docker**
- **Deployment-Ready** for Render 

.. image:: https://github.com/user-attachments/assets/e2385055-3110-4842-b679-36c9a1060e48
   :alt: Premium Django starter built on top of Bootstrap 5 and Corporate Dashboard PRO, a pixel-perfect design from Creative-Tim.


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/corporate-dashboard-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

    unzip django-corporate-dashboard-pro.zip
    cd django-corporate-dashboard-pro

Once the source code is unzipped, the next step is to start it and use provided features.     

Export `GITHUB_TOKEN` in the environment 
----------------------------------------

App-Generator provides the value during purchase. This is required because the project has a private REPO dependency: `github.com/app-generator/priv-django-admin-corporate-pro`

.. code-block:: shell
    :caption: GITHUB_TOKEN export for different operating systems

    $ export GITHUB_TOKEN='TOKEN_HERE'  # for Linux, Mac
    $ set GITHUB_TOKEN='TOKEN_HERE'     # Windows CMD
    $ $env:GITHUB_TOKEN = 'TOKEN_HERE'  # Windows powerShell 

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

.. image:: https://github.com/user-attachments/assets/e2385055-3110-4842-b679-36c9a1060e48
   :alt: Premium Django starter built on top of Bootstrap 5 and Corporate Dashboard PRO, a pixel-perfect design from Creative-Tim. 

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst
