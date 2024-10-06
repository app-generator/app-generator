Deployment
==========

.. title:: Deploy on Render -  Dynamic Django Starter      
.. meta::
    :description: Deploy Dynamic Django on Render, a popular service for developers  
    :keywords: Dynamic Django deployment, Django and Render, Deploy on Render 

This page explains how to deploy `Dynamic Django Tool <./index.html>`__ on **Render**, a popular service for developers.   

.. include::  /_templates/components/signin-invite.rst

Configuration
-------------

 The files that handles this step are: 

- **render.yaml**: the deployment descriptor 
- **build.sh**: bash script that executes the compialtion steps in the remote server 

.. code-block:: yaml
    :caption: render.yaml

    services:
    - type: web
        name: appseed-v2
        plan: starter
        env: python
        region: frankfurt  # region should be same as your database region.
        buildCommand: "./build.sh"
        startCommand: "gunicorn core.wsgi:application"
        envVars:
        - key: DEBUG
            value: True
        - key: SECRET_KEY
            generateValue: true
        - key: WEB_CONCURRENCY
            value: 4

.. code-block:: bash
    :caption: build.sh 

    python -m pip install --upgrade pip
    pip install -r requirements.txt

    # Collect Static
    python manage.py collectstatic --no-input

    # Migrate DB 
    python manage.py makemigrations
    python manage.py migrate

Steps to Follow
---------------

* You'll need to create a Blueprint instance on Render by going to this `link`_.
* Connect the repository that you want to deploy.
* Fill in the Service Group Name and click on the Update Existing Resources button.
* Click on Environment and add key called ``PYTHON_VERSION`` and set it equal to ``3.12.0``.
* After you make this change, the deployment will start automatically.

.. _link: https://dashboard.render.com/blueprints

In the end you should have a LIVE deployment identical to the official `Dynamic Django DEMO <https://dynamic-django.onrender.com/dynamic-dt/sales/>`__. 

.. image:: https://github.com/user-attachments/assets/7abec2c4-220f-4ac5-9de6-e96f8fc17c3e
   :alt: Dynamic Django - Dynamic DataTables view: minimal configuration, fully-fleged server-side paginated view 

Resources
---------

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
