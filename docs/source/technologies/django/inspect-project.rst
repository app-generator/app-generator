Inspect Project
===============

Inheriting a legacy `Django <https://www.djangoproject.com/>`__ project can be challenging. 
This tutorial will guide you through the process of inspecting and understanding an existing Django project, helping you gain insights into its structure, dependencies, and functionality.

.. include::  /_templates/components/banner-top.rst

If we are new to the project, a good idea migth be to inspect the project footprint using `tree` command. 

.. code-block:: bash

    tree -L 2 -d
    # The simplified output for App-Generator.dev project is below: 

    ├── apps
    │   ├── ai_processor
    │   ├── api
    │   ├── authentication
    │   ├── blog
    │   ├── common
    │   ├── dashboard
    │   ├── deploy
    │   ├── generator
    │   ├── helpers
    │   ├── pages
    │   ├── products
    │   ├── tasks
    │   ├── ticket
    │   └── tools
    ├── cli
    │   ├── management
    │   └── migrations
    ├── core
    ├── docs
    │   ├── build
    │   └── source
    ├── static
    │   ├── assets
    │   ├── common
    │   ├── dist
    │   └── product
    ├── staticfiles
    ├── templates
    │   ├── authentication
    │   ├── dashboard
    │   ├── docs
    │   ├── generator
    │   ├── includes
    │   ├── layouts
    │   └── pages
    └── util
        ├── generator
        └── logger

Print Configuration
-------------------

.. code-block:: python 

    from django.core.management.base import BaseCommand
    from django.utils import timezone

    from django.conf import settings

    class Command(BaseCommand):
        help = 'Displays project config'

        def handle(self, *args, **kwargs):
            
            # Iterate over apps
            for key in settings.__dict__.keys():

                self.stdout.write(" Cfg Key: " + key + " -> %s" % settings.__dict__[ key ] )

The sample output of the above is below: 

.. code-block:: bash

    python.exe manage.py help_print_cfg
    # The output 
    Cfg Key: _wrapped -> <Settings "core.settings">
    Cfg Key: INSTALLED_APPS -> ['webpack_loader', 'django.contrib.admin', ...]        
    Cfg Key: LOGGING_CONFIG -> logging.config.dictConfig
    Cfg Key: LOGGING -> {}
    Cfg Key: DEFAULT_EXCEPTION_REPORTER -> django.views.debug.ExceptionReporter
    Cfg Key: FORCE_SCRIPT_NAME -> None

Print Models 
-------------

.. code-block:: python 

    from django.core.management.base import BaseCommand
    from django.utils import timezone

    from django.apps import apps

    class Command(BaseCommand):
        help = 'Displays registered apps and models'

        def handle(self, *args, **kwargs):
            
            # Iterate over apps
            for app in apps.get_app_configs():
                self.stdout.write(" APP -> %s" % app.verbose_name)

                # Iterate over models
                for model in app.get_models():

                    prefix = str(model.__module__ + '.' + model.__name__)
                    self.stdout.write("\t |--> %s" % prefix )
                    prefix = prefix.replace('.models', '')
                    fields = model._meta.fields
                    for f in fields:
                        f_type = str( type(f).__qualname__ )
                        f_name = str( f ).replace(prefix + '.', '')
                        f_info = f_name + ': ' + f_type
                        self.stdout.write("\t   |--> %s " % f_info ) 
            
The sample output of the above is below: 

.. code-block:: bash

    python.exe manage.py help_print_models
    # The output 

    APP -> Webpack Loader
    APP -> Administration
            |--> django.contrib.admin.models.LogEntry
            |--> admin.LogEntry.id: AutoField
            |--> admin.LogEntry.action_time: DateTimeField
            |--> admin.LogEntry.user: ForeignKey
            |--> admin.LogEntry.content_type: ForeignKey
            |--> admin.LogEntry.object_id: TextField
            |--> admin.LogEntry.object_repr: CharField
            |--> admin.LogEntry.action_flag: PositiveSmallIntegerField
            |--> admin.LogEntry.change_message: TextField    

.. include::  /_templates/components/footer-links.rst
