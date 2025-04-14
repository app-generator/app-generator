:og:description: Django Pixel UI PRO - Premium Starter built on top of Pixel Design (pro version)
:og:image: https://user-images.githubusercontent.com/51070104/168812715-52e036b7-582d-4851-9657-6b1f99727619.png
:og:image:alt: Premium Django Starter enhanced with OAuth Github, Extended User Profiles, Self-Deletion option and Docker Support - Pixel PRO Design

`Pixel UI PRO </product/datta-pixel-bootstrap-pro/django/>`__
==============================================================

.. title:: Django Pixel UI PRO - OAuth Github, Extended User Profiles, Self-Deletion option, and Docker Support
.. meta::
    :description: Premium Django Starter enhanced with OAuth Github, Extended User Profiles, Self-Deletion option and Docker Support - Pixel PRO Design
    :keywords: pixel ui kit, pixel bootstrap 5, django pixel starter, django template with pixel ui, premium django starter

Premium Django Starter enhanced with OAuth Github, Extended User Profiles, Self-Deletion option, and Docker Support.
`Themesberg </agency/themesberg/>`__ provides the - `Pixel UI PRO </product/pixel-bootstrap/django/>`__ Design (PRO version).

- 👉 `Django Pixel UI PRO </product/pixel-bootstrap-pro/django/>`__ - Product Page (contains download link)
- 👉 `Django Pixel UI PRO <https://django-pixel-enh.appseed-srv1.com/>`__ - LIVE Demo 
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `Pixel UI PRO </product/pixel-bootstrap/django/>`__ Design Integration 
- `Bootstrap </docs/templates/bootstrap.html>`__ CSS Styling
- Session-based Authentication
- OAuth for Github
- Extended User Profiles
- DB Persistence: SQLite/MySql/PostgreSQL
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/168760719-f0e45406-2b2a-43e0-badf-fa953edb62b8.png
   :alt: Django Pixel PRO - Premium Starter built on top of Pixel


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/pixel-bootstrap-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow thhe installation steps:

.. code-block:: shell

    unzip django-pixel-pro.zip
    cd django-pixel-pro

Once the source code is unzipped, the next step is to start it and use provided features.     


Export `GITHUB_TOKEN` in the environment 
----------------------------------------

App-Generator provides the value during purchase. This is required because the project has a private REPO dependency: `github.com/app-generator/priv-django-theme-pixel-pro`

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

    <  ROOT  >
        |
        |-- core/                 # Project Settings 
        |    |-- settings.py 
        |    |-- wsgi.py     
        |    |-- urls.py     
        |
        |-- home/                 # Presentation app 
        |    |-- views.py         # serve the HOMEpage  
        |    |-- urls.py     
        |    |-- models.py
        |
        |
        |-- templates/            # UI templates 
        |-- static/               # Tailwind/Flowbite 
        |    |-- src/             # 
        |         |-- input.css   # CSS Styling
        |
        |-- Dockerfile            # Docker
        |-- docker-compose.yml    # Docker 
        |
        |-- render.yml            # CI/CD for Render
        |-- build.sh              # CI/CD for Render 
        |
        |-- manage.py             # Django Entry-Point
        |-- requirements.txt      # dependencies
        |-- .env                  # ENV File


.. include::  /_templates/components/django-manual-build.rst

.. image:: https://user-images.githubusercontent.com/51070104/168760719-f0e45406-2b2a-43e0-badf-fa953edb62b8.png
   :alt: Django Pixel PRO - Premium Starter built on top of Pixel

.. include::  /_templates/components/django-create-users.rst
    
Contents
--------

.. toctree::
   :maxdepth: 1

   customization
