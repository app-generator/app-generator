:og:description: Vite - The modern frontend build tool

Vite
====

.. title:: Vite - The modern frontend build tool
.. meta::
    :description: build tool that offers a faster and leaner development experience compared to older bundlers like webpack.

Vite (French word for "quick") is a modern frontend build tool that offers a faster and leaner development experience compared to older bundlers like webpack.

.. include::  /_templates/components/banner-top.rst

When you start a development server with Vite, it leverages native ES modules, which means it doesn't need to bundle your entire application before you can start working. 
This results in an almost instant server start-up time, even for larger applications. 

When you make changes to your code, Vite only needs to rebuild the specific module you modified, leading to lightning-fast hot module replacement.

Integrations
------------

- `Django, DaisyUI and Vite <./django/integrate-daisyui.html>`__ - coding sample included
- `Django, Flowbite and Vite <./django/integrate-flowbite.html>`__ - coding sample included
- `Flask, DaisyUI and Vite <./flask/integrate-daisyui.html>`__ - coding sample included
- `Flask, Flowbite and Vite <./flask/integrate-flowbite.html>`__ - coding sample included

Resources
---------

.. toctree::
   :maxdepth: 1
   
   vite/index
   vite/vite-vs-webpack
