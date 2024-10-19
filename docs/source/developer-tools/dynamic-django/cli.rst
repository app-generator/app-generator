CLI Tools
=========

.. title:: CLI Tools -  Dynamic Django Starter      
.. meta::
    :description: Powerfull CLI tools to mutate Python/Django codebase via Dynamic Django  
    :keywords: dynamic cli tools, dynamic services, dynamic django, dynamic programming, dynamic patterns

This page explains the **CLI Helpers** shipped by the `Dynamic Django <./index.html>`__ starter.  

.. include::  /_templates/components/banner-top.rst

Usage - Import CLI Package
--------------------------

The CLI helpers are located in the `cli` package, root of the codebase:

.. code-block:: bash
    :caption: Project Files

    < Dynamic Django > 
       |
       |-- core/                            
       |    |-- settings.py           # Project Configuration  
       |
       |-- cli/                       # CLI Package   
            |-- __init__.py           # The entry point  
            |-- common.py             # Constants 
            |-- h_code_parser.py      # AST-based helpers 
            |-- h_files.py            # Filesystem Helpers 
            |-- h_git.py              # GIT Interface
            |-- h_shell.py            # Shell Interface
            |-- h_django.py           # DJANGO specific helpers
            |-- h_django_deps.py      # Manage Project dependencies 
            |-- h_django_env.py       # Manage ENV
            |-- h_django_settings.py  # Manage Settings 
            |-- h_django_urls.py      # Manage Routing 

The `cli` package can be used in the Django Shell, but also outside Django in Python shell

.. code-block:: shell
    :caption: Import CLI helpers 

    # Usage via Django Shell 
    python manage.py shell
    >>> from cli import * 

    # Usage via Python Shell 
    python
    >>> from cli import * 

In both ways, the Django machinery is available. 

GIT CLI
-------

The **Git Interface** defined in `cli/h_git.py` aims to help beginners to interact with the GitHub platform using simplified commands. 

    git_changes()

Print current changes and modified files. Here is a sample output: 

.. code-block:: shell
    :caption: git_changes() output 

    >>> from cli import *
    >>> git_changes()
    .env
    core/settings.py
    db.sqlite3
    django_dyn_api/helpers.py
    home/models.py


    git_log()

Print the latest changes made on the codebase 

.. image:: https://github.com/user-attachments/assets/907ea5f2-a5ec-4774-a1fe-e377e4403f85
   :alt: Dynamic Django - Git CLI, the output of git_log() helper  


Shell Helpers 
-------------

Using the shell interface we can check the Django migration status, migrate the Database, create an ADMIN user or start the project using a custom PORT. 

    check_migrations()

Check migrations status 

    exec_migration()

Migrate the database 

    create_admin() 

Create a superuser using the input collected from the terminal 

Code Parser  
-----------

This helper allows to get Python classes using reflection and also we can inject code in existing classes and models 

    name_to_class(name: str)

This helper will return the a Python class instance if the input string identifies an imported class.

.. code-block:: python
    :caption: name_to_class() usage and output 

    >>> from cli import *
    >>> product = name_to_class('home.models.Product')
    >>> product.objects.all()
    <QuerySet [<Product: Nike / $99>, <Product: PUMA / $99>, <Product: Jordan 5 / $99>, <Product: Jordan 4 / $199>, <Product: Jordan 1 / $499>]>

    PythonFileClassManipulator - Interface to the AST code structure 

This class is heavily used to update the code via primitives like **add_model()**, **add_model_field()** ..etc. 


Django Helpers 
--------------

The **Django Interface** defined in `cli/h_django.py` aims to make easier the interaction with all Django internal structures and entities like applications, configuration.

    get_django()

Initiate Django in Python shell outside `manage.py shell` command. This is important when we need to interact with Django core from a bash shell. 

    check_db_conn()

Check if the DB credentials are correct and the codebase can work as expected. 

    get_apps()

List all registered application in **settings.INSTALLED_APPS** section 

    get_models(aApp) - returs objects 

List all models defined in an application  

    get_models_name(aApp) - returs strings 

List the models names  defined in an application  

    get_model_fields(aModelClass) 

Returns all class fields 

    get_model_fk(aModelClass)

Returns all fields that are Foreign Keys 

    add_model(aAppName, aModelName)

Adds a new model to axisting application

    add_model_field(aAppName, aModelName, aFieldName, aFieldType, `**kwargs`)

Added a specific field to a model 

    del_model_field(aAppName, aModelName, aFieldName)

Delete field from an existing model     

.. include::  /_templates/components/footer-links.rst
