Git Interface 
=============

.. title:: Git Interface - Django CLI Package      
.. meta::
    :description: Interact with Git/Github via the Django CLI Package     
    :keywords: django cli, git, github cli, manage commits

This page explains the Git Helpers shipped by the `Django CLI Package <./index.html>`__. 

.. include::  /_templates/components/banner-top.rst

.. include::  /_templates/components/django-cli-install.rst

Print Changes
-------------

.. code-block:: python
    :caption: git_changes()

    >>> from cli import * 
    >>> git_changes()


Print Git LOG
-------------

.. code-block:: python
    :caption: git_log()

    >>> from cli import * 
    >>> git_log()


Commit Changes  
--------------

.. code-block:: python
    :caption: git_commit()

    >>> from cli import * 
    >>> git_commit()


Tag Changes  
--------------

.. code-block:: python
    :caption: git_tag()

    >>> from cli import * 
    >>> git_tag()


Lits Git Tags
--------------

.. code-block:: python
    :caption: git_list_tags()

    >>> from cli import * 
    >>> git_list_tags()    


Revert Commit 
-------------

.. code-block:: python
    :caption: git_revert()

    >>> from cli import * 
    >>> git_revert()    

.. include::  /_templates/components/footer-links.rst
