Unicode Decode 0x9d Error
=========================

.. title:: UnicodeDecodeError 'charmap' codec can't decode byte 0x9d     
.. meta::
    :description: How to Fix UnicodeDecodeError: charmap codec can't decode byte 0x9d in position X: character maps to undefined

This page explains How to Fix UnicodeDecodeError: charmap codec can't decode byte 0x9d in position X: character maps to undefined

.. include::  /_templates/components/banner-top.rst

This issue is environmental and might occur during package installation (via PIP) or simply at runtime when files are loaded and processed by Python. 

A fix that worked for a Windows OS with Python 3.9 was to force in the environment the UTF8 encoding:

.. code-block:: bash

    $ set PYTHONUTF8=1 # For Windows CMD

.. include::  /_templates/components/footer-links.rst
