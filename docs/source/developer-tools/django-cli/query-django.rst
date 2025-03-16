Query Django 
============

.. title:: Query Django Internals - Django CLI Package      
.. meta::
    :description: Interact with Django internals via the Django CLI Package     
    :keywords: django cli, list models, list apps, list models, update models 

This page explains the Django Internals helpers  shipped by the `Django CLI Package <./index.html>`__. With a few lines of code we will be able to get Django Instance, check database conenction, 
list registered applications and models, inspect models and create new ones.  

.. include::  /_templates/components/banner-top.rst

.. include::  /_templates/components/django-cli-install.rst

Get Django Instance 
-------------------

Using this helper, we can retrieve in the CLi an instance of Django. 

.. code-block:: python
    :caption: get_django()

    >>> from cli import * 
    >>> get_django()
    <django.apps.registry.Apps object at 0x000001BB8DE27A00> 


Check DB Connection 
-------------------

.. code-block:: python
    :caption: check_db_conn()

    >>> from cli import * 
    >>> check_db_conn()


Get Applications   
----------------

.. code-block:: python
    :caption: get_apps()

    >>> from cli import * 
    >>> get_apps()


Get App Models    
--------------

.. code-block:: python
    :caption: get_models(aApp)

    >>> from cli import * 
    >>> get_models(aApp)


Get Models Name
---------------

.. code-block:: python
    :caption: get_models_name(aApp)

    >>> from cli import * 
    >>> get_models_name(aApp)


Get Model by Name
-----------------

.. code-block:: python
    :caption: get_model_by_name(aApp, aModelname)

    >>> from cli import * 
    >>> get_model_by_name(aApp, aModelname)


Get Model Fields 
----------------

.. code-block:: python
    :caption: get_model_fields(aModelClass)

    >>> from cli import * 
    >>> get_model_fields(aModelClass)

Get Model FKs
----------------

.. code-block:: python
    :caption: get_model_fk(aModelClass)

    >>> from cli import * 
    >>> get_model_fk(aModelClass)


Check Model Migration
---------------------

.. code-block:: python
    :caption: check_model_migration(aModelClass)

    >>> from cli import * 
    >>> check_model_migration(aModelClass)


Extract Class Code
------------------

.. code-block:: python
    :caption: extract_class_code(aFilePath, aClassName)

    >>> from cli import * 
    >>> extract_class_code(aFilePath, aClassName)


Add Model to App 
----------------

.. code-block:: python
    :caption: add_model(aAppName, aModelName)

    >>> from cli import * 
    >>> add_model(aAppName, aModelName)

.. include::  /_templates/components/footer-links.rst
