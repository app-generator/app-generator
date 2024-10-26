`Django Rocket <https://github.com/app-generator/rocket-django>`__
==================================================================

.. title:: Django Rocket - Open-Source Django Template 
.. meta::
    :description: Open-Source Django Template crafted on top of Tailwind and Flowbite
    :keywords: django, starter, django template, rocket design, tailwind, flowbite

**Rocket Django** is an Open-Source Django Starter project desgined to streamline
the development process and help you build modern, responsive web applications based on a
template with ease. Packed with pre-built components, Tailwind CSS styling, and best
coding practices, Rocket Django is a ready to deploy package provides a solid foundation for your next Django project.

.. include::  /_templates/components/signin-invite.rst

Key features
------------

* **Pre-built tools:** A feature-rich library of apps that accelerate development and ensures consistency across your application.
* **Tailwind CSS integration:** Tailwind CSS provides a utility-first approach to styling, offering flexibility and efficiency in creating visually appealing interfaces.
* **Best coding practices:** Adherence to industry-standard coding practices promotes maintainability, scalability, and readability.
* **Ready-to-deploy structure:** Rocket Django is designed for easy deployment, saving developers time and effort.
* **API via Django REST Framework**: An option integrate the application with API using DRF.

.. image:: https://github.com/user-attachments/assets/4d7513cd-8005-4ba6-94f0-66011f91f6b4
   :alt: Rocket Django - Open-source Starter


Who is it for?
--------------

You can use Rocket Django to quickly kickstart your Django project without spending time on
boilerplate code and styling. It's used for building web applications like SaaS tools,
analytics dashboards, or any other type of web app that you require.

* **Django Developers:** Seasoned Django developers can leverage Rocket Django to streamline their workflows and rapidly build complex web applications.

* **Beginners:** Those new to Django can benefit from Rocket Django's pre-configured structure, reducing the learning curve and enabling them to focus on core application logic.


How to use it?
--------------

The free tier is available for you to use and customize as you like. On this page, we'll
check out the different modules that this tier has to offer and how we can set it up.


Clone the repository
--------------------

* Head over to this repo and clone it locally on your desktop

The source code can be downloaded from the official page or the GitHub repository.

.. code-block:: shell

    git clone https://github.com/app-generator/rocket-django.git
    cd rocket-django 

Once the source code is cloned, we'll compile the code and it'll be ready for deployment.


Building the project
--------------------

It's best to use a Python virtual environment for installing the project dependencies. You can use the following
code to create the virtual environment

.. code-block:: bash

    virtualenv env

To start the environment

* If you're on Windows

.. code-block:: shell

    .\env\Scripts\activate.bat

* If you're using Linux

.. code-block:: bash

    source env/bin/activate

Finally, after activating the virtual environment, you can install the dependencies using

.. code-block::

    pip install -r requirements.txt

You'll also need to install the Tailwind CSS dependencies and the application functionality
using NPM. You can do this in a separate terminal with the virtual environment enabled.

.. code-block:: bash

    npm install

Setting up the database
-----------------------

**By default**, the application **uses SQLite** for persistence. In order to use `MySql`/`PostgreSQL`,
you'll need to install the Python driver:

.. code-block:: bash

    pip install mysqlclient # for MySql
    # OR 
    pip install psycopg2    # for PostgreSQL

To connect the application with your mySQL database, you'll need to fill in the credentials
int the `.env` file and run the migrations.

.. code-block:: text
    :caption: .env

    DB_ENGINE=mysql
    # OR 
    DB_ENGINE=postgresql

    # DB credentials below
    DB_HOST=localhost
    DB_NAME=<DB_NAME_HERE>
    DB_USERNAME=<DB_USER_HERE>
    DB_PASS=<DB_PASS_HERE>
    DB_PORT=3306

Use the following commands to seed your data:

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate


Running the project
-------------------

You can run Rocket Django locally or deploy it on Render. If you want to run
the server locally, you'll need to run the following command:

.. code-block:: bash

    python manage.py runserver

Furthermore, you'll also need to start the frontend using:

.. code-block:: bash

    npm run dev

.. tip::

        If you want to customize the template locally and want the project
        to hot reload, you'll have to use the following command instead:

        .. code-block:: bash

                npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css --watch

Open `localhost` on your browser and you can interact with the application. 

.. _localhost: http://127.0.0.1:8000/

.. code-block:: shell

        # Optional (kill all existing containers)
        docker container kill $(docker ps -q) ; docker container rm $(docker ps -a -q) ; docker network prune -f 
        # Start the APP
        docker-compose up --build 
    
Once the image is finished building and the container has been deployed, you can access the application
on your `localhost\:5085`.

.. _localhost:5085: http://localhost:5085


Moreover, if you want to deploy the application on Render, you'll have to
modify the ``render.yaml`` file.

.. attention::

        Make sure to change the application name to match your repository
        name on GitHub.

.. code-block:: yaml
    :caption: render.yaml

	services:
	  - type: web
		name: rocket-django # <-- change this name to match your repositoy
		plan: starter
		env: python
		region: frankfurt  # region should be same as your database region.
		buildCommand: "./build.sh"
		startCommand: "gunicorn core.wsgi:application"
		envVars:
			- key: DEBUG
			  value: False
			- key: SECRET_KEY
			  generateValue: true
			- key: WEB_CONCURRENCY
			  value: 4

* You'll need to create a Blueprint instance on Render by going to this `link`_. 
* Connect the repository that you want to deploy.
* Fill in the Service Group Name and click on the Update Existing Resources button.
* Click on Environment and add key called ``PYTHON_VERSION`` and set it equal to ``3.12.0``.
* After you make this change, the deployment will start automatically.

.. _link: https://dashboard.render.com/blueprints

Modules
-------

In this section, we'll go over the features that the starter template has to offer.
Right off the bat, we get access to a dashboard that shows us our product analytics. However,
if we want to make any changes, we'll have to sign in first. The dummy credentials for an admin
user are given on the Sign In screen. This brings us to our first functionality.

Extended ``User`` model
-----------------------

One feature worth mentioning is the extended user model included
in the free version. This pre-made model allows for different functionality accross the application.
We can change this information in the Profile tab.

.. code-block:: python

        class Profile(models.Model):
            user      = models.OneToOneField(User, on_delete=models.CASCADE)
            role      = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
            full_name = models.CharField(max_length=255, null=True, blank=True)
            country   = models.CharField(max_length=255, null=True, blank=True)
            city      = models.CharField(max_length=255, null=True, blank=True)
            zip_code  = models.CharField(max_length=255, null=True, blank=True)
            address   = models.CharField(max_length=255, null=True, blank=True)
            phone     = models.CharField(max_length=255, null=True, blank=True)
            avatar    = models.ImageField(upload_to='avatar', null=True, blank=True)

            def __str__(self):
                return self.user.username

DataTables
----------

Let's have a look at the data table.

.. figure:: https://github.com/user-attachments/assets/082dc336-480e-4457-9557-09ddacd31362
    :alt: A view of the data table

The data table shows us the products in our database. We can perform basic CRUD operations on this screen.

Charts
------

The next best thing in this template are the charts made using ApexCharts. There are two ways we can populate them:
* Using Django's object-relational mapper, for people that want to avoid working in JavaScript

.. figure:: https://github.com/user-attachments/assets/afe85ff7-049b-42be-b7b4-4a3ca7a90231
    :alt: Default template charts

* Using an API via Django REST framework

.. figure:: https://github.com/user-attachments/assets/7b206e29-1bf9-4edf-9ad7-6822dbeaaed6
    :alt: Charts using API via DRF

API via DRF
-----------

The DRF provides us with a GUI that we can use to perform CRUD operations on our data and view the JSON information as well.

.. figure:: https://github.com/user-attachments/assets/b5bbda2d-772d-4851-af77-d8c77e70842a
    :alt: GUI for CRUD operations in DRF

Async Tasks (Celery)
--------------------

Finally, the last feature integrated into the application is the task scheduler, which allows you to schedule a particular task
with a set time interval. Rocket Django uses ``Celery`` for this purpose. ``Celery`` runs time-consuming tasks in the background without slowing down your application
or making it unresponsive.

.. figure:: https://github.com/user-attachments/assets/7130073b-a8ba-4718-8c78-7815e764dc5c
    :alt: Tasks

`Django Rocket PRO` Index

.. toctree::
   :maxdepth: 1
   :caption: Contents:
   
   source-code   
