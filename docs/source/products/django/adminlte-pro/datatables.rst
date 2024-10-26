AdminLTE PRO DataTables 
=======================

This page explains how the **Dynamic DataTables** feature of **Django AdminLTE PRO** can be used to manage any DB table using a powerful paginated view:

- 👉 `Django Dynamic DataTables <https://django-adminlte-pro.onrender.com/tables/>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Configuration 
-------------

**Dynamic DataTable** section provides a simple way to specify the models that are automatically managed. 

The section is a dictionary where the key is the segment of the endpoint and the value the import path of the model. Here are the DEMOs for the default models: 

.. code-block:: python
    :caption: core/settings.py  

    # Syntax: Complete import path for Model & Form
    DYNAMIC_DATATB = {
        # Model -> Form 
        'apps.common.models.Sales' : "apps.common.forms.SalesForm",
        'apps.common.models.Products' : "apps.common.forms.ProductsForm",
    }   

Add a new Model  
---------------

Besides the default tables view (Sales and Product models), the Dynamic DataTable feature can be extended to any new model. 
Here are the steps to enable a new endpoint 

- **Define a new model** `Homework` in the `common` aplication

.. code-block:: python
    :caption: apps/common/models.py  

    class Homework(models.Model):
        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length=100)
        content = models.TextField(blank=True, null=True, default='')

- **Migrate the database** 

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate    

- **Define a form for the new model** 

.. code-block:: python
    :caption: apps/common/forms.py  

    class HomeworkForm(forms.ModelForm):

        class Meta:
            model = Homework
            fields = '__all__'    

- **Update the configuration**: `DYNAMIC_API` section 

.. code-block:: python
    :caption: core/settings.py  

    # Syntax: Complete import path for Model & Form
    DYNAMIC_DATATB = {
        # Model -> Form 
        'apps.common.models.Sales' : "apps.common.forms.SalesForm",
        'apps.common.models.Products' : "apps.common.forms.ProductsForm",
        'apps.common.models.Titanic' : "apps.common.forms.TitanicForm",    # <-- NEW 
    }  

- **The new view** is now listed in the **Dynamic DataTable** page and ready to be used. 

.. image:: https://github.com/user-attachments/assets/066992e2-91de-4279-b236-923a4b2882cf
   :alt: Django AdminLTE PRO - Dynamic DataTable View 
   
.. include::  /_templates/components/footer-links.rst
