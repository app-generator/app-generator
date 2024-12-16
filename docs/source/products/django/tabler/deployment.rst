Deploy Tabler
=============

This page explains how to deploy **Django Tabler** on Render, a popular service for developers.   

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
        name: django-tabler
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

* Authenticate on `Render <https://render.com/>`__
* You'll need to create a Blueprint instance on Render by going to this `link`_.
* Connect the repository that you want to deploy.
* Fill in the Service Group Name and click on the Update Existing Resources button.
* Click on Environment and add key called ``PYTHON_VERSION`` and set it equal to ``3.12.0``.
* After you make this change, the deployment will start automatically.

.. _link: https://dashboard.render.com/blueprints

In the end you should have a LIVE deployment identical to the official `Django Tabler DEMO <https://django-tabler.onrender.com/>`__. 

.. image:: https://github.com/user-attachments/assets/826e18b5-998d-41ec-b57b-35654c210a9b
   :alt: Homepage Django Tabler - open-source starter built on top of Tabler Design 


.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
