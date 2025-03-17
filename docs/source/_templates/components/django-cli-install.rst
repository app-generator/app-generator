Import CLI Package
------------------

Download a starter that supports the Django CLI package: `Datta Able </product/datta-able/django/>`__ (Free) or `Dynamic Django </onboarding-kit/>`__ (Paid) via **Onboarding Kit** Bundle. 
Once the project is downloaded, unzip it and inspect the files.  

.. code-block:: shell

    unzip django-datta-able.zip
    cd django-datta-able
    pip install -r requirements.txt


The CLI helpers are located in the `cli` package, root of the codebase:

.. code-block:: bash
    :caption: Project Files

    < PROJECT_ROOT > 
       |
       |-- cli/                       # CLI Package   
            |-- __init__.py           # The entry point  
            |-- common.py             # Constants 
            |-- h_ai_claude.py        # Claude.AI Interface 
            |-- h_code_parser.py      # AST-based helpers 
            |-- h_django_common.py    # Manage Project dependencies 
            |-- h_django_deps.py      # Manage Project dependencies 
            |-- h_django_env.py       # Manage ENV
            |-- h_django_settings.py  # Manage Settings 
            |-- h_django_urls.py      # Manage Routing 
            |-- h_django.py           # DJANGO specific helpers
            |-- h_files.py            # Filesystem Helpers 
            |-- h_git.py              # GIT Interface
            |-- h_shell.py            # Shell Interface
            |-- h_util.py             # Misc Helpers


After installing the dependencies, we can start the Python shell and import the CLI package in the **Django** or **Python** Shell. 

.. code-block:: shell
    :caption: Import CLI helpers 

    # Usage via Django Shell 
    python manage.py shell
    >>> from cli import * 

    # OR using the Python Shell 
    python                 # Start Python Shell 
    >>> from cli import *  # Import CLI Helpers  
    >>> h_random()         # Test the import by calling a helper 
    >>> 'Py8v76'      

At this point, we can start using the CLI helpers. 
