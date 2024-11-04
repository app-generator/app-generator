Templates System
================

This page explains how to override templates from third-party applications in `Django <./index.html>`__, including multiple approaches and best practices. 
Here are the key points to remember when overriding templates:

**Template loading order is crucial**

`Django <./index.html>`__ checks your project templates first, then app templates in the order specified in **INSTALLED_APPS**.

**You have multiple override methods**

- Project-level overrides in your main templates directory
- App-level overrides in your app's templates directory
- Partial overrides using template inheritance

Always match the exact template path structure of the third-party app. Use template inheritance to keep original content while adding your own.

.. include::  /_templates/components/banner-top.rst

Understanding Template Loading Order
------------------------------------

**Django** looks for templates in the following order:

- Directories listed in **DIRS** within **TEMPLATES** setting
- **templates** directories inside each app, based on app order in **INSTALLED_APPS**

.. code-block:: python 

    # settings.py
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                BASE_DIR / 'templates',  # Project-level templates
            ],
            'APP_DIRS': True,  # Enable app template directories
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    INSTALLED_APPS = [
        'myapp',              # Your app (first to check)
        'third_party_app',    # Third-party app (checked after)
        'django.contrib.admin',
        # ...
    ]

Project Structure for Template Overrides
----------------------------------------

.. code-block:: bash 

    myproject/
        ├── myproject/
        │   ├── settings.py
        │   └── urls.py
        ├── templates/          # Project-level templates
        │   └── third_party_app/  # Match the app's template structure
        │       └── template_to_override.html
        ├── myapp/
        │   └── templates/     # App-level templates
        │       └── third_party_app/  # Match the app's template structure
        │           └── template_to_override.html
        └── venv/
            └── lib/
                └── python3.x/
                    └── site-packages/
                        └── third_party_app/
                            └── templates/
                                └── third_party_app/
                                    └── original_template.html


Methods to Override Templates
-----------------------------

Method 1: Project-Level Override
********************************

.. code-block:: html

    <!-- templates/third_party_app/template_to_override.html -->
    {% extends "third_party_app/template_to_override.html" %}

    {% block content %}
        <!-- Your custom content -->
    {% endblock %}


Method 2: App-Level Override
****************************

.. code-block:: html

    <!-- myapp/templates/third_party_app/template_to_override.html -->
    {% extends "third_party_app/base.html" %}

    {% block title %}Custom Title{% endblock %}

    {% block content %}
        <!-- Your custom content -->
    {% endblock %}

Method 3: Partial Override Using includes
*****************************************

.. code-block:: html

    <!-- templates/third_party_app/template_to_override.html -->
    {% extends "third_party_app/base.html" %}

    {% block sidebar %}
        {% include "myapp/custom_sidebar.html" %}
    {% endblock %}    


Finding Templates to Override
-----------------------------

Locating Original Templates

.. code-block:: python 

    # management/commands/find_template.py
    from django.core.management.base import BaseCommand
    from django.template.loader import get_template
    from django.template.loaders.app_directories import get_app_template_dirs

    class Command(BaseCommand):
        def add_arguments(self, parser):
            parser.add_argument('template_name', type=str)

        def handle(self, *args, **options):
            template_name = options['template_name']
            try:
                template = get_template(template_name)
                self.stdout.write(f'Template found at: {template.origin.name}')
            except Exception as e:
                self.stdout.write(f'Error finding template: {e}')    


Advanced Override Techniques
----------------------------

Using Template Inheritance
**************************

.. code-block:: html

    <!-- templates/third_party_app/base.html -->
    {% extends "third_party_app/original_base.html" %}

    {% block extra_css %}
        {{ block.super }}  <!-- Keep original CSS -->
        <link rel="stylesheet" href="{% static 'css/custom.css' %}">
    {% endblock %}

    {% block content %}
        <div class="custom-wrapper">
            {{ block.super }}  <!-- Keep original content -->
            {% include "myapp/additional_content.html" %}
        </div>
    {% endblock %}


Context Modification
********************

.. code-block:: python

    # views.py
    from third_party_app.views import OriginalView

    class CustomView(OriginalView):
        template_name = 'third_party_app/template_to_override.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['custom_data'] = self.get_custom_data()
            return context    


Best Practices
--------------

Template Discovery
******************

.. code-block:: python

    # settings.py
    # Add debug toolbar for template source inspection
    if DEBUG:
        INSTALLED_APPS += ['debug_toolbar']
        MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']    


Template Discovery
******************

.. code-block:: html 

    <!-- Document template versions -->
    {% comment %}
    Original template version: 2.1.0
    Last override update: 2024-01-15
    Changes:
    - Modified header layout
    - Added custom sidebar
    {% endcomment %}    


Fallback Templates
******************

.. code-block:: html 

    {% extends parent_template|default:"third_party_app/base.html" %}

    {% block content %}
        {% include custom_sidebar|default:"third_party_app/default_sidebar.html" %}
        {{ block.super }}
    {% endblock %}


Template Fragment Caching
*************************

.. code-block:: html 

    {% load cache %}

    {% cache 500 sidebar request.user.id %}
        {% include "custom_sidebar.html" %}
    {% endcache %}


Troubleshooting
---------------

When the templates output is not the one we expect, we can inspect the templating system and search for the cause. 


Check Template Resolution Order
*******************************

.. code-block:: python 

    # settings.py
    DEBUG = True
    TEMPLATES[0]['OPTIONS']['debug'] = True  # Enable template debug info

Using Django Debug Toolbar
**************************

Add to **INSTALLED_APPS** and check the Templates panel for:

- Template inheritance chain
- Context variables
- Template source

Common Issues
*************

- Template Not Found: Check path matches exactly
- Blocks Not Overridden: Verify block names match
- Inheritance Issues: Check circular dependencies

.. include::  /_templates/components/footer-links.rst
