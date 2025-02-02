`Soft UI Design <https://www.creative-tim.com/product/soft-ui-design-system?AFFILIATE=128200>`__
================================================================================================

.. title:: Soft UI Design -  Open-source soft-design UI Kit created by Creative-Tim 
.. meta::
    :description: Open-source UI Kit built on top of Bootstrap 5 - contains Soft UI components and pre-built Pages

**Soft UI Design** System represents a modern approach to interface design, emphasizing soft shadows, subtle gradients, and light/dark contrasts to create a neumorphic appearance. 
This design system, created by Creative Tim, focuses on creating depth and dimensionality through careful use of shadows and highlights rather than traditional material elevation.

- 👉 `Soft UI Design <https://www.creative-tim.com/product/soft-ui-design-system?AFFILIATE=128200>`__ - Product page 
- 👉 `Soft UI Design <https://demos.creative-tim.com/material-kit/index.html?AFFILIATE=128200>`__ - Live Demo

.. include::  /_templates/components/banner-top.rst

.. image:: https://github.com/user-attachments/assets/ce56cfce-5194-4409-af80-097fc4492589
   :alt: Soft UI Design - open-source UI Kit template provided by Creative-Tim 

Project Architecture
--------------------

.. code-block:: bash

    soft-ui-design/
        ├── dist/                   # Production files
        ├── src/
        │   ├── assets/
        │   │   ├── css/
        │   │   │   ├── soft-ui-design.css
        │   │   │   └── soft-design.min.css
        │   │   ├── scss/
        │   │   │   ├── soft-ui/
        │   │   │   │   ├── components/
        │   │   │   │   ├── mixins/
        │   │   │   │   └── variables/
        │   │   │   └── soft-ui.scss
        │   │   ├── js/
        │   │   │   ├── core/
        │   │   │   ├── plugins/
        │   │   │   └── soft-ui.js
        │   │   └── img/
        │   ├── pages/
        │   └── sections/
        ├── docs/
        └── gulpfile.js    

Soft UI Components
------------------

Neumorphic Cards
****************

The signature component of Soft UI Design System:

.. code-block:: html 

    <div class="card card-background shadow-soft border-radius-xl">
        <div class="full-background" style="background-image: url('path/to/img')"></div>
        <div class="card-body text-start p-3 w-100">
            <div class="row">
                <div class="col-12">
                    <div class="blur shadow-blur bg-white border-radius-lg p-3">
                        <h4 class="mb-0">Soft UI Component</h4>
                        <p class="text-sm mb-0">
                            This is an example of a neumorphic card component
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>    

Soft Buttons
************

Implementation of neumorphic buttons:

.. code-block:: html 

    <!-- Primary soft button -->
    <button class="btn bg-gradient-primary shadow-soft-md">
        Primary Button
    </button>

    <!-- Secondary soft button -->
    <button class="btn btn-outline-primary shadow-soft">
        Secondary Button
    </button>

    <!-- Icon button -->
    <button class="btn btn-icon-only shadow-soft-lg">
        <i class="fas fa-heart"></i>
    </button>

Resources
---------

- Official Documentation: Creative Tim website
- Support: Through Creative Tim's support system
- Updates: Regular through npm
- Community: Creative Tim forums

Remember to keep your Soft UI Design System installation updated for the latest features and improvements.

.. include::  /_templates/components/footer-links.rst
