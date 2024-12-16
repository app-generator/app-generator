Customize UI
============

This page explains how to customize the UI of **Django Tabler**.   

.. include::  /_templates/components/signin-invite.rst

The Concept 
-----------

Django Tabler UI is provided by `Tabler UI Library </docs/products/django-libs/theme-tabler.html>`__ that can be installed and used in any Django project (new or legacy). 

Django template system will search for a template file starting from current app location:

- Templates directory provided by the current application 
- Global templates directories specified in the configuration 
- Virtual Environment directories

By default, Django Tabler loads the SignIn and SignUp pages from the `templates` directory located in the root of the project, and the rest os the pages from virtual environment, where `Tabler UI Library` is installed 

In order to customize any page provided by the library, we need to copy the page from the virtual environment to the local templates directory. 

- The `source templates <https://github.com/app-generator/django-admin-tabler/tree/main/admin_tabler/templates>`__, provided by the **Tabler UI Library** 
- The `destination templates <https://github.com/app-generator/django-tabler/tree/master/templates>`__, configured in **Django Tabler** 

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
