`AdminLTE </product/adminlte/>`__ 
==================================

.. title:: AdminLTE - A popular open-source admin dashboard template    
.. meta::
    :description: Open-source admin dashboard template and control panel theme built on top of Bootstrap 

`AdminLTE <https://adminlte.io>`__ is a popular open-source admin dashboard template and control panel theme built on top of Bootstrap. 
It provides a collection of ready-to-use UI components and layouts specifically designed for building admin panels, dashboards, and other web applications requiring an administrative interface.

- 👉 `AdminLTE Starters </product/adminlte/>`__ - Bundle provided by `App Generator </>`__ platorm

.. include::  /_templates/components/banner-top.rst

Built on Bootstrap and featuring modern UI components, AdminLTE provides developers with an extensive collection of ready-to-use elements including charts, tables, form controls, and navigation systems. 
The template's thoughtful organization facilitates rapid development while maintaining visual consistency across different sections of an application.

.. image:: https://github.com/user-attachments/assets/a59d18e7-3861-4eb0-8730-8efcf6f13892
   :alt: AdminLTE - open-source dashboard template  

Key Features
-------------

- Responsive Design
- Cross-browser compatibility
- Built on Bootstrap 4/5
- Modular architecture
- SCSS/SASS support
- RTL support
- Dark/Light mode
- Extensive UI components library

Technical Stack
---------------

- Frontend Framework: Bootstrap 4/5
- jQuery (required)
- Popper.js
- Font Awesome (icons)
- Chart.js (for charts)
- DataTables (for enhanced tables)
- Select2 (for enhanced dropdowns)
- Various Bootstrap plugins


Directory Structure
-------------------

.. code-block:: bash

    adminlte/
        ├── dist/                   # Compiled files
        │   ├── css/               # Compiled CSS
        │   ├── js/                # Compiled JavaScript
        │   └── img/               # Images
        ├── plugins/               # Third-party plugins
        ├── pages/                 # Example pages
        └── src/                   # Source files
            ├── scss/             # SCSS source files
            └── js/               # JavaScript source files

Layout Components
-----------------

- **Main Header** (main-header): Top navigation bar
- **Main Sidebar** (main-sidebar): Left navigation menu
- **Content Wrapper** (content-wrapper): Main content area
- **Control Sidebar** (control-sidebar): Right sidebar for settings
- **Footer** (main-footer): Page footer

UI Components
-------------

Navigation
**********

.. code-block:: html

    <!-- Main Sidebar -->
    <aside class="main-sidebar sidebar-dark-primary elevation-4">
        <!-- Brand Logo -->
        <a href="index.html" class="brand-link">
            <img src="logo.png" class="brand-image">
            <span class="brand-text">AdminLTE</span>
        </a>
        
        <!-- Sidebar -->
        <div class="sidebar">
            <nav class="mt-2">
                <ul class="nav nav-pills nav-sidebar flex-column">
                    <!-- Add icons to the links using the .nav-icon class -->
                    <li class="nav-item">
                        <a href="#" class="nav-link active">
                            <i class="nav-icon fas fa-tachometer-alt"></i>
                            <p>Dashboard</p>
                        </a>
                    </li>
                </ul>
            </nav>
        </div>
    </aside>

Cards
*****

.. code-block:: html

    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Card Title</h3>
            <div class="card-tools">
                <!-- Card tools go here -->
            </div>
        </div>
        <div class="card-body">
            Content goes here
        </div>
        <div class="card-footer">
            Footer content
        </div>
    </div>    


Customization
-------------

**SCSS Variables**: Key variables that can be customized

.. code-block:: scss

    // Main colors
    $primary: #007bff;
    $secondary: #6c757d;
    $success: #28a745;
    $info: #17a2b8;
    $warning: #ffc107;
    $danger: #dc3545;

    // Sidebar
    $sidebar-dark-bg: #343a40;
    $sidebar-dark-hover-bg: #2c3136;
    $sidebar-width: 250px;

    // Header
    $main-header-height: 57px;    

Layout Options
--------------

Available layout classes for **body** tag:

- **layout-fixed**: Fixed sidebar
- **layout-navbar-fixed**: Fixed navbar
- **layout-footer-fixed**: Fixed footer
- **sidebar-collapse**: Collapsed sidebar
- **sidebar-mini**: Mini sidebar mode
- **dark-mode**: Enable dark mode

.. include::  /_templates/components/footer-links.rst
