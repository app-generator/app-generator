Datta Able Flask
=====================================================================

Open-source `Django
Dashboard <https://appseed.us/admin-dashboards/django/>`__ provided by
``AppSeed`` on top of a modern design. `Datta
Able <https://appseed.us/product/datta-able/django/>`__ Bootstrap Lite
is the most stylized Bootstrap 4 Template, among all other Lite/Free
admin templates in the market. It comes with high feature-rich pages and
components with fully developer-centric code - design from
``CodedThemes``.

-  👉 `Datta Able
   Django <https://appseed.us/product/datta-able/django/>` -
   ``Product page``
-  👉 `Datta Able
   Django <https://django-datta-able.appseed-srv1.com/>`-
   ``LIVE demo``

Features
--------

   ``Have questions?`` Contact `Support <https://appseed.us/support/>`
   (Email & Discord) provided by **AppSeed**

+-----------------------+-----------------------+-----------------------+
| Free Version          | `PRO                  | `Custom               |
|                       | Version <https://app  | Development <         |
|                       | seed.us/product/datta | https://appseed.us/cu |
|                       | -able-pro/django/>`__ | stom-development/>`__ |
+=======================+=======================+=======================+
| ✓ **Django 4.2.9**    | **Everything in       | **Everything in       |
|                       | Free**, plus:         | PRO**, plus:          |
+-----------------------+-----------------------+-----------------------+
| ✓ Bootstrap 4 UI      | ✅ **PRO Bootstrap 5  | ✅ **1 Week**         |
|                       | UI**, ``Dark-Mode``   | `                     |
|                       |                       | `Custom Development`` |
+-----------------------+-----------------------+-----------------------+
| ✓ API Generator       | ✅ **OAuth**          | ✅ **Team**: PM,      |
|                       | ``GitHub``            | Developer, Tester     |
+-----------------------+-----------------------+-----------------------+
| ✓ DataTables          | ✅ ``API``,           | ✅ Weekly Sprints     |
|                       | `Charts <https:/      |                       |
|                       | /django-datta-pro.onr |                       |
|                       | ender.com/charts/>`__ |                       |
+-----------------------+-----------------------+-----------------------+
| ✓ ``Docker``          | ✅ `Enhanced          | ✅ Technical Specs    |
|                       | DataTables <https:/   |                       |
|                       | /django-datta-pro.onr |                       |
|                       | ender.com/tables/>`__ |                       |
+-----------------------+-----------------------+-----------------------+
| ✓ ``CI/CD`` Flow via  | ✅ **Celery**         | ✅ Documentation      |
| Render                | (``async tasks``)     |                       |
+-----------------------+-----------------------+-----------------------+
| ✓ ``Free Support``    | ✅ **Media Files      | ✅ **30 days Delivery |
| (GitHub Issues)       | Manager**             | Warranty**            |
+-----------------------+-----------------------+-----------------------+
| -                     | ✅ **Extended User    | ✅ `CI/CD for AWS,    |
|                       | Profiles**            | DO <h                 |
|                       |                       | ttps://appseed.us/ter |
|                       |                       | ms/#section-ci-cd>`__ |
|                       |                       | **(Extra)**           |
+-----------------------+-----------------------+-----------------------+
| -                     | ✅ **Automated e2e    | -                     |
|                       | Tests**               |                       |
+-----------------------+-----------------------+-----------------------+
| -                     | ✅                    | -                     |
|                       | ``                    |                       |
|                       | Private REPO Access`` |                       |
+-----------------------+-----------------------+-----------------------+
| -                     | ✅ `Premium           | -                     |
|                       | Support <https://ap   |                       |
|                       | pseed.us/support/>`__ |                       |
+-----------------------+-----------------------+-----------------------+
| ————————————          | ————————————          | ————————————          |
+-----------------------+-----------------------+-----------------------+
| ✓ `LIVE               | 🚀 `LIVE              | 🛒 ``Order``:         |
| Demo <https           | Demo <                | `$999 <https://app    |
| ://django-datta-able. | https://django-datta- | seed.gumroad.com/l/ro |
| appseed-srv1.com/>`__ | pro.onrender.com/>`__ | cket-package-week>`__ |
|                       |                       | (GUMROAD)             |
+-----------------------+-----------------------+-----------------------+

.. figure:: https://user-images.githubusercontent.com/51070104/176118649-7233ffbc-6118-4f56-8cda-baa81d256877.png
   :alt: Datta Able (enhanced with dark mode) - Open-Source Seed project
   generated by AppSeed.

   Datta Able (enhanced with dark mode) - Open-Source Seed project
   generated by AppSeed.

Start with ``Docker``
---------------------

   👉 **Step 1** - Download the code from the GH repository (using
   ``GIT``)

.. code:: bash

   $ git clone https://github.com/app-generator/django-datta-able.git
   $ cd django-datta-able

   👉 **Step 2** - Start the APP in ``Docker``

.. code:: bash

   $ docker-compose up --build 

Visit ``http://localhost:5085`` in your browser. The app should be up &
running.

Environment
-----------

Create a new ``.env`` file using sample ``env.sample``. The meaning of
each variable can be found below:

-  ``DEBUG``: if ``True`` the app runs in development mode

   -  For production value ``False`` should be used

-  For ``MySql`` persistence

   -  Install the DB Driver: ``pip install mysqlclient``
   -  Create DB and assign a new user (full rights)
   -  Edit ``.env`` to match the DB, user, and password

Manual Build
------------

   Download the code

.. code:: bash

   $ git clone https://github.com/app-generator/django-datta-able.git
   $ cd django-datta-able

👉 Set Up for ``Unix``, ``MacOS``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Install modules via ``VENV``

.. code:: bash

   $ virtualenv env
   $ source env/bin/activate
   $ pip3 install -r requirements.txt

   Set Up Database

.. code:: bash

   $ python manage.py makemigrations
   $ python manage.py migrate

   Generate API

.. code:: bash

   $ python manage.py generate-api -f

   Start the APP

.. code:: bash

   $ python manage.py createsuperuser # create the admin
   $ python manage.py runserver       # start the project

At this point, the app runs at ``http://127.0.0.1:8000/``.

👉 Set Up for ``Windows``
~~~~~~~~~~~~~~~~~~~~~~~~~

   Install modules via ``VENV`` (windows)

::

   $ virtualenv env
   $ .\env\Scripts\activate
   $ pip3 install -r requirements.txt

   Set Up Database

.. code:: bash

   $ python manage.py makemigrations
   $ python manage.py migrate

   Start the APP

.. code:: bash

   $ python manage.py createsuperuser # create the admin
   $ python manage.py runserver       # start the project

At this point, the app runs at ``http://127.0.0.1:8000/``.

Codebase Structure
------------------

The project is coded using a simple and intuitive structure presented
below:

.. code:: bash

   < PROJECT ROOT >
      |
      |-- core/                            
      |    |-- settings.py                   # Project Configuration  
      |    |-- urls.py                       # Project Routing
      |
      |-- home/
      |    |-- views.py                      # APP Views 
      |    |-- urls.py                       # APP Routing
      |    |-- models.py                     # APP Models 
      |    |-- tests.py                      # Tests  
      |    |-- templates/                    # Theme Customisation 
      |         |-- pages                    # 
      |              |-- custom-index.py     # Custom Dashboard      
      |
      |-- requirements.txt                   # Project Dependencies
      |
      |-- env.sample                         # ENV Configuration (default values)
      |-- manage.py                          # Start the app - Django default start script
      |
      |-- ************************************************************************

How to Customize
----------------

When a template file is loaded in the controller, ``Django`` scans all
template directories starting from the ones defined by the user, and
returns the first match or an error in case the template is not found.
The theme used to style this starter provides the following files:

.. code:: bash

   # This exists in ENV: LIB/admin_datta
   < UI_LIBRARY_ROOT >                      
      |
      |-- templates/                     # Root Templates Folder 
      |    |          
      |    |-- accounts/       
      |    |    |-- auth-signin.html     # Sign IN Page
      |    |    |-- auth-signup.html     # Sign UP Page
      |    |
      |    |-- includes/       
      |    |    |-- footer.html          # Footer component
      |    |    |-- sidebar.html         # Sidebar component
      |    |    |-- navigation.html      # Navigation Bar
      |    |    |-- scripts.html         # Scripts Component
      |    |
      |    |-- layouts/       
      |    |    |-- base.html            # Masterpage
      |    |    |-- base-auth.html       # Masterpage for Auth Pages
      |    |
      |    |-- pages/       
      |         |-- index.html           # Dashboard Page
      |         |-- profile.html         # Profile Page
      |         |-- *.html               # All other pages
      |    
      |-- ************************************************************************

When the project requires customization, we need to copy the original
file that needs an update (from the virtual environment) and place it in
the template folder using the same path.

   For instance, if we want to **customize the index.html** these are
   the steps:

-  ✅ ``Step 1``: create the ``templates`` DIRECTORY inside the ``home``
   app
-  ✅ ``Step 2``: configure the project to use this new template
   directory

   -  ``core/settings.py`` TEMPLATES section

-  ✅ ``Step 3``: copy the ``index.html`` from the original location
   (inside your ENV) and save it to the ``home/templates`` DIR

   -  Source PATH: ``<YOUR_ENV>/LIB/admin_black_pro/pages/index.html``
   -  Destination PATH:
      ``<PROJECT_ROOT>home/templates/pages/index.html``

..

   To speed up all these steps, the **codebase is already configured**
   (``Steps 1, and 2``) and a ``custom dashboard`` can be found at this
   location:

``home/templates/pages/custom-index.html``

By default, this file is unused because the ``theme`` expects
``index.html`` (without the ``custom-`` prefix).

In order to use it, simply rename it to ``index.html``. Like this, the
default version shipped in the library is ignored by Django.

In a similar way, all other files and components can be customized
easily.

Deploy on `Render <https://render.com/>`__
------------------------------------------

-  Create a Blueprint instance

   -  Go to https://dashboard.render.com/blueprints this link.

-  Click ``New Blueprint Instance`` button.
-  Connect your ``repo`` which you want to deploy.
-  Fill the ``Service Group Name`` and click on the
   ``Update Existing Resources`` button.
-  After that, your deployment will start automatically.

At this point, the product should be LIVE.

`Datta Able Django <https://appseed.us/product/datta-able-pro/django/>`__ ``PRO Version``
-----------------------------------------------------------------------------------------

   For more components, pages, and priority on support, feel free to
   take a look at this amazing starter:

Designed for those who like bold elements and beautiful websites,
**Datta Able** is the most stylish Bootstrap 4 Admin Template compare to
all other Bootstrap admin templates. It comes with high feature-rich
pages and components with fully developer-centric code.

-  👉 `Django Datta
   PRO <https://appseed.us/product/datta-able-pro/django/>`__ - product
   page

   -  ✅ ``Enhanced UI`` - more pages and components
   -  ✅ ``Priority`` on support

.. figure:: https://user-images.githubusercontent.com/51070104/170474361-a58da82b-fff9-4a59-81a8-7ab99f478f48.png
   :alt: Datta Able PRO - Full-Stack Starter generated by AppSeed.

   Datta Able PRO - Full-Stack Starter generated by AppSeed.

--------------

`Datta Able Django <https://appseed.us/product/datta-able/django/>`__ -
Open-source starter provided by `AppSeed <https://appseed.us/>`__.
