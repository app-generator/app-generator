`Volt Dashboard <https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard>`__
==============================================================================================

.. title:: Volt Dashboard -  Modern, Responsive admin template created by ThemesBerg
.. meta::
    :description: Open-source dashboard template built on top of Bootstrap 5 - contains components and pre-built pages 

**Volt Dashboard** is a premium Bootstrap 5 admin dashboard created by Themesberg. It features a modern design system with carefully crafted components, extensive customization options, and a robust technical foundation. 
The dashboard is particularly notable for its clean interface, dark mode support, and extensive data visualization capabilities.

- 👉 `Volt Dashboard <https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard>`__ - Product page 
- 👉 `Volt Dashboard <https://demo.themesberg.com/volt/>`__ - Live Demo

.. include::  /_templates/components/banner-top.rst

.. image:: https://user-images.githubusercontent.com/51070104/168843604-b026fd94-5969-4be7-81ac-5887cf0958e5.png
   :alt: Volt Dashboard - Open-source dashboard template from Themesberg 

Project Structure
-----------------

.. code-block:: bash

    volt-dashboard/
        ├── dist/                      # Production files
        ├── src/
        │   ├── assets/
        │   │   ├── css/
        │   │   │   ├── volt.css
        │   │   │   └── vendor/
        │   │   ├── js/
        │   │   │   ├── volt.js
        │   │   │   └── modules/
        │   │   ├── img/
        │   │   │   ├── brand/
        │   │   │   ├── icons/
        │   │   │   └── illustrations/
        │   │   └── scss/
        │   │       ├── volt/
        │   │       │   ├── components/
        │   │       │   ├── layout/
        │   │       │   ├── mixins/
        │   │       │   └── vendor/
        │   │       └── volt.scss
        │   ├── pages/
        │   └── partials/
        ├── node_modules/
        ├── package.json
        └── gulpfile.js    

Component System
----------------

Advanced Cards with Stats
*************************

.. code-block:: html 

    <div class="card border-light shadow-sm">
        <div class="card-body">
            <div class="row d-block d-xl-flex align-items-center">
                <div class="col-12 col-xl-5 text-xl-center mb-3 mb-xl-0 d-flex align-items-center justify-content-xl-center">
                    <div class="icon-shape icon-shape-primary rounded me-4 me-sm-0">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <div class="d-sm-none">
                        <h2 class="h5">Customers</h2>
                        <h3 class="mb-1">345,678</h3>
                    </div>
                </div>
                <div class="col-12 col-xl-7 px-xl-0">
                    <div class="d-none d-sm-block">
                        <h2 class="h5">Customers</h2>
                        <h3 class="mb-1">345,678</h3>
                    </div>
                    <small class="d-flex align-items-center">
                        <span class="text-success me-2">
                            <i class="fas fa-arrow-up"></i> 18.2%
                        </span>
                        <span class="text-gray-500">Since last month</span>
                    </small>
                </div>
            </div>
        </div>
    </div>    

Data Tables
***********

.. code-block:: html     
    
    <div class="card border-light shadow-sm mb-4">
        <div class="card-body">
            <div class="table-responsive">
                <table class="table table-centered table-nowrap mb-0 rounded">
                    <thead class="thead-light">
                        <tr>
                            <th class="border-0">#</th>
                            <th class="border-0">Traffic Source</th>
                            <th class="border-0">Source Type</th>
                            <th class="border-0">Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Table rows -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>

Resources
---------

- Documentation: Available in Themesberg documentation
- Support: Through Themesberg support system
- Updates: Regular through npm
- Community: Themesberg forums

Remember to keep your Volt Dashboard installation updated for the latest features and security patches.

.. include::  /_templates/components/footer-links.rst
