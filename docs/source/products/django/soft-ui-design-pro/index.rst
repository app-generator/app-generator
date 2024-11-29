:og:description: Django Soft Design PRO - Premium Starter built on top of Soft UI Design
:og:image: https://user-images.githubusercontent.com/51070104/168812715-52e036b7-582d-4851-9657-6b1f99727619.png
:og:image:alt: Premium Django Starter enhanced with OAuth Github, Extended User Profiles, Self-Deletion option and Docker Support - Soft Design PRO

`Soft Design PRO </product/soft-ui-design-pro/django/>`__ 
=========================================================

.. title:: Django Soft Design PRO - Premium Starter built on top of Soft Design     
.. meta::
    :description: Premium Django Starter enhanced with OAuth Github, Extended User Profiles, Self-Deletion option and Docker Support - Soft Design PRO
    :keywords: soft ui design, django soft template, django pro template, django pro starter, soft ui design pro, soft design django 

Premium Django Starter enhanced with OAuth Github, Extended User Profiles, Self-Deletion option, and Docker Support.
Creative-Tim provides the **Soft UI Design**, the premium version

- 👉 `Django Soft Design PRO </product/soft-ui-design-pro/django/>`__ - Product Page (contains download link)
- 👉 `Django Soft Design PRO <https://django-soft-design-enh.appseed-srv1.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- Soft Design UI PRO Integration
- Bootstrap 5 Styling
- Session-based Authentication
- OAuth for Github
- Extended User Profiles
- DB Persistence: SQLite/MySql/PostgreSQL
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/168812715-52e036b7-582d-4851-9657-6b1f99727619.png
   :alt: Premium Django starter built on top of Bootstrap 5 and Soft Design PRO, a pixel-perfect design from Creative-Tim.


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/soft-ui-design-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

    unzip django-soft-ui-design-pro.zip
    cd django-soft-ui-design-pro

Once the source code is unzipped, the next step is to start it and use provided features.     


Export `GITHUB_TOKEN` in the environment 
----------------------------------------

App-Generator provides the value during purchase. This is required because the project has a private REPO dependency: `github.com/app-generator/priv-django-theme-soft-pro`

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

.. image:: https://user-images.githubusercontent.com/51070104/168812715-52e036b7-582d-4851-9657-6b1f99727619.png
   :alt: Premium Django starter built on top of Bootstrap 5 and Soft Design PRO, a pixel-perfect design from Creative-Tim.

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst