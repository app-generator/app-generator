Installation 
============

.. title:: Installation -  Dynamic Django Starter      
.. meta::
    :description: Learn how to install Dynamic Django, a tool that helps to manage data with ease  
    :keywords: install dynamic django, install dynamic services, set up dynamic api, set up dynamic programming, install dynamic patterns

This page explains the installtion of `Dynamic Django <./index.html>`__, a tools that helps to manage large amount of information with ease: 

- CSV to model
- CSV loader 
- Dynamic API exposure for every model via configuration 
- Dynamic DataTables 
- Charts 

Here are the steps to get started and use the tool: 

Download Sources
****************

To get the product navigate to the `payment page <https://appseed.gumroad.com/l/devtool-dynamic-django>`__ and complete the purchase. 
Once the download is complete, unzip it and change the directory inside the unzipped folder:

.. code-block:: bash
    :caption: Unzip Dynamic Django

    unzip dynamic-django.zip
    cd dynamic-django 

As an alternative, the project sources can be cloned directly from GitHub by those that have access: 

.. code-block:: bash
    :caption: Git Clone from the private REPO

    git clone https://github.com/app-generator/priv-dynamic-django.git
    cd priv-dynamic-django

Install Modules 
***************

The best way when installing modules is to use a virtual environment to ensure isolation of the downloaded packages and zero side effect in the operating system. 

.. code-block:: bash

    virtualenv env
    # OR
    python -m venv env 

After creation, the next step is to activate the environment and install project dependencies 

.. code-block:: bash

    source env/bin/activate
    pip install -r requirements.txt

Migrate Database 
****************

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate

Running the project
*******************

You can run Dynamic Django locally or deploy it on Render. If you want to run the server locally, you'll need to run the following command:

.. code-block:: bash

    python manage.py createsuperuser # optional for SuperUSer creation
    python manage.py runserver       

**runserver** command starts Dynamic Django on the default address **http://localhost:8000**.

.. include::  /_templates/components/footer-links.rst
