`Material Kit <https://www.creative-tim.com/product/material-kit?AFFILIATE=128200>`__
=====================================================================================

.. title:: Material Kit -  Open-source material-design UI Kit created by Creative-Tim 
.. meta::
    :description: Open-source UI Kit built on top of Bootstrap 5 - contains UI components and free sample pages

**Material Kit** represents Creative-Tim's interpretation of Google's Material Design principles, crafted specifically for web applications. 
This kit goes beyond basic Material Design implementation by adding carefully curated animations, color schemes, 
and enhanced components while maintaining the core principles of material elevation, motion, and interaction.

- 👉 `Material Kit <https://www.creative-tim.com/product/material-kit?AFFILIATE=128200>`__ - Product page 
- 👉 `Material Kit <https://demos.creative-tim.com/material-kit/index.html?AFFILIATE=128200>`__ - Live Demo

.. include::  /_templates/components/banner-top.rst

.. image:: https://github.com/user-attachments/assets/96b55233-cae7-4000-af56-4acb645b5ea1
   :alt: Material Kit - open-source dashboard template provided by Creative-Tim 

Project Architecture
--------------------

.. code-block:: bash

    material-kit/
        ├── dist/                   # Production-ready files
        ├── src/
        │   ├── assets/
        │   │   ├── css/
        │   │   │   ├── material-kit.css
        │   │   │   └── material-kit.min.css
        │   │   ├── scss/
        │   │   │   ├── material-kit/
        │   │   │   │   ├── bootstrap/
        │   │   │   │   ├── cards/
        │   │   │   │   ├── mixins/
        │   │   │   │   └── variables/
        │   │   │   └── material-kit.scss
        │   │   ├── js/
        │   │   │   ├── core/
        │   │   │   ├── plugins/
        │   │   │   └── material-kit.js
        │   │   └── img/
        │   ├── docs/
        │   └── pages/
        └── gulpfile.js    

Material Components
-------------------

Cards with Elevation
********************

Material Kit provides enhanced card components that follow Material Design elevation principles:

.. code-block:: html

    <div class="card move-on-hover">
        <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
            <a class="d-block blur-shadow-image">
                <img src="image.jpg" alt="img-blur-shadow" class="img-fluid shadow border-radius-lg">
            </a>
            <div class="colored-shadow" style="background-image: url(image.jpg)"></div>
        </div>
        
        <div class="card-body text-center">
            <h5 class="font-weight-normal">
                <a href="javascript:;">Material Card</a>
            </h5>
            <p class="mb-0">
                Find unique solutions for your design needs
            </p>
        </div>
    </div>    

Material Buttons
****************

.. code-block:: html

    <!-- Contained button (raised) -->
    <button class="btn bg-gradient-primary">Primary</button>

    <!-- Text button -->
    <button class="btn btn-text">Text Button</button>

    <!-- Outlined button -->
    <button class="btn btn-outline-primary">Outlined</button>

    <!-- Button with icon -->
    <button class="btn bg-gradient-primary">
        <i class="material-icons">favorite</i>
        With Icon
    </button>

    <!-- Floating action button -->
    <button class="btn btn-primary btn-fab btn-round">
        <i class="material-icons">add</i>
    </button>    

Additional Resources
--------------------

- Material Design Guidelines: material.io
- Creative Tim Documentation
- Support Forums
- GitHub Repository
- Regular Updates via npm

Remember to keep your Material Kit installation updated for the latest features and Material Design specification updates.

.. include::  /_templates/components/footer-links.rst
