Download `Dynamic Django </docs/developer-tools/dynamic-django/index.html>`__
-----------------------------------------------------------------------------

For newcomers, **Dynamic Django** is a commercial tool that aims to simplify the data processing and consolidation via generated APIs, DataTables, Charts and CLI tools. 

To get the product navigate to the `payment page <https://appseed.gumroad.com/l/devtool-dynamic-django>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell
   :caption: Unzip Dynamic Django

   unzip dynamic-django.zip
   cd dynamic-django 

The project set up is the usual one for any Django project: 

.. code-block:: shell
   :caption: Start the project 

   virtualenv env                    # create a virtual environment 
   source env/bin/activate           # activate VENV
   pip install -r requirements.txt   # install modules 
   python manage.py makemigrations   # migrate DB
   python manage.py migrate          # apply changes 
   python manage.py runserver        # start Dynamic Django tool

At this point, we can visit the tool in the browser at **localhost:8000**.
