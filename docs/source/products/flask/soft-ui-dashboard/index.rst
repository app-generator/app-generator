:og:description: Flask Soft UI Dashboard - Open-Source Flask Template
:og:image: https://github.com/user-attachments/assets/9510c443-4615-4856-b9c4-f00875134f7d
:og:image:alt: Flask Soft UI Dashboard - Open-Source Flask Template

`Soft UI Dashboard </product/soft-ui-dashboard/flask/>`__
=========================================================

.. title:: Flask Soft UI Dashboard - Open-Source Flask Template 
.. meta::
    :description: Open-Source Flask Template crafted on top of Soft UI Dashboard Design
    :keywords: flask, starter, flask template, datta able, bootstrap 4, flask template

**Open-Source Flask Template** built with a minimum set of features on top of `Soft UI Dashboard </product/soft-ui-dashboard/>`__, a modern dashboard design from Creative-Tm. 
This template can be used to start a new project quickly by adding new features on top of the existing ones or simply for learning purposes.

- 👉 `Soft UI Dashboard Flask </product/soft-ui-dashboard/flask/>`__ - Product Page (contains download link)
- 👉 `Soft UI Dashboard Flask <https://flask-datta-demo.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord  

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- Simple, Easy-to-Extend codebase, `Blueprint Pattern </blog/flask-blueprints-a-developers-guide/>`__
- Up-to-date Dependencies
- `Soft UI Dashboard </product/soft-ui-dashboard/>`__ Design Integration
- `Bootstrap </docs/templates/bootstrap.html>`__ CSS Styling 
- Authentication: Session Based, GitHub OAuth
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Dynamic DataTables - manage data without coding
- Docker 
- CI/CD integration for Render 

.. figure:: https://github.com/user-attachments/assets/9510c443-4615-4856-b9c4-f00875134f7d
   :alt: Soft UI Dashboard - Open-Source Seed project powered by Flask - actively supported by App Generator

.. include::  /_templates/components/flask-prerequisites.rst


Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/soft-ui-dashboard/flask/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/flask-soft-ui-dashboard.git
    cd flask-soft-ui-dashboard

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

- **Core**: holds the project settings 
- **Home**: the application that integrates the Soft UI Dashboard Design 
- **Api**: the generated API 

.. code-block:: bash   

    < PROJECT ROOT >
        |
        |-- apps/
        |    |
        |    |-- authentication/                 # Handles auth routes (login and register)
        |    |    |-- routes.py                  # Define authentication routes  
        |    |    |-- models.py                  # Defines models  
        |    |    |-- forms.py                   # Define auth forms (login and register) 
        |    |
        |    |-- home/                           # A simple app that serve HTML files
        |    |    |-- routes.py                  # Define app routes
        |    |
        |    |-- dyn_dt/                          # Dynamic Data Tables Module
        |    |    |-- routes.py                  # Define app routes
        |    |
        |    |-- static/
        |    |    |-- <css, JS, images>          # CSS files, Javascripts files
        |    |
        |    |-- templates/                      # Templates used to render pages
        |    |    |-- includes/                  # HTML chunks and components
        |    |    |    |-- navigation.html       # Top menu component
        |    |    |    |-- sidebar.html          # Sidebar component
        |    |    |    |-- footer.html           # App Footer
        |    |    |    |-- scripts.html          # Scripts common to all pages
        |    |    |
        |    |    |-- layouts/                   # Master pages
        |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
        |    |    |    |-- base.html             # Used by common pages
        |    |    |
        |    |    |-- accounts/                  # Authentication pages
        |    |    |    |-- login.html            # Login page
        |    |    |    |-- register.html         # Register page
        |    |    |
        |    |    |-- home/                      # UI Kit Pages
        |    |         |-- index.html            # Index page
        |    |         |-- 404-page.html         # 404 page
        |    |         |-- .html                 # All other pages
        |    |    
        |  config.py                             # Set up the app
        |    __init__.py                         # Initialize the app
        |
        |-- requirements.txt                     # App Dependencies
        |
        |-- .env                                 # Inject Configuration via Environment
        |-- run.py                               # Start the app - WSGI gateway

.. include::  /_templates/components/flask-manual-build.rst

.. figure:: https://github.com/user-attachments/assets/9510c443-4615-4856-b9c4-f00875134f7d
   :alt: Soft UI Dashboard - Open-Source Seed project powered by Flask - actively supported by App Generator 

.. include::  /_templates/components/flask-create-users.rst

Dynamic DataTables  
------------------

This pattern allows to manage the information saved in any model without coding effort. Here is how it works:

- Define a new model or update an existing one 
- Migrate your database using Flask-Migrate Module
    - `$ flask db migrate` - generate the SQL 
    - `$ flask db upgrade` - apply changes in DB
- Update Configuration to activate the dynamic table view
    - `apps.config.DYNAMIC_DATATB` section
- Access the `dynamic datatable <https://flask-datta-demo.onrender.com/dynamic-dt>`__ route in the browser and access the model 
        
Configuration 
*************

The dynamic datatable module loads the configuration from **DYNAMIC_DATATB** variable, saved in the Configuration class, where the dictionary structure is used to:

- key: datatable URI path 
- value: the import path for the Model to be managed

Below set up will expose the URI **/dynamic-dt/products** for the model **apps.models.Product**

.. code-block:: python

    class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))   

    ...(tuncated output)

    DYNAMIC_DATATB = {
        "products": "apps.models.Product"
    }

UI View 
*******

Once the configuration is saved, the application automatically build the dataTable view for the speficied model with a set of common helpers like:

- pagination 
- filters 
- search 
- number of items per page 

.. figure:: https://github.com/user-attachments/assets/ab46a909-0076-4be5-83d0-2b773377f103
   :alt: Dynamic DataTable view - Manage data without coding in Flask 

.. include::  /_templates/components/generator-flask.rst

.. include::  /_templates/components/footer-links.rst
