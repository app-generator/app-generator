`Argon Dashboard </product/argon-dashboard/>`__
===============================================

.. title:: Argon Dashboard -  Modern, responsive admin template created by Creative-Tim 
.. meta::
    :description: Open-source admin dashboard template and control panel theme built on top of Bootstrap 5 

`Argon Dashboard <https://www.creative-tim.com/product/argon-dashboard?AFFILIATE=128200>`__ is a modern, 
responsive admin template created by `Creative Tim </agency/creative-tim/>`__, built with Bootstrap 5. 
It offers a clean, modern design with carefully crafted components for building administrative interfaces, dashboards, and web applications.

**Argon Dashboard** serves as a solid foundation for different web applications including project management tools, basic analytics interfaces, content administration systems, and lightweight business applications. 
Its responsive design ensures consistent performance across devices, adapting smoothly from desktop workstations to mobile screens.

- 👉 `Argon PRO Starters </product/argon-dashboard-pro/>`__ - Bundle provided by `App Generator </>`__ platorm

.. include::  /_templates/components/banner-top.rst

The template provides developers with a well-curated selection of essential components and layouts necessary for creating effective dashboard experiences. 
Its streamlined structure balances visual appeal with practical functionality, making it suitable for developers at various skill levels.

.. image:: https://github.com/user-attachments/assets/140d4157-f88b-409d-9bb8-559f1c1012a5
   :alt: Argon Dashboard - open-source dashboard template provided by Creative-Tim 

Available Versions
------------------

- Free Bootstrap 5 version
- PRO Bootstrap 5 version
- React version
- Angular version
- Vue.js version
- Laravel version

Key Features
------------

- Bootstrap 5 Framework
- SASS/SCSS files included
- 100% Responsive design
- Custom components
- Plugin integration
- Documentation included
- Regular updates
- MIT License (Free version)

Technical Stack
---------------

- **Frontend Framework**: Bootstrap 5
- **CSS Preprocessor**: SASS/SCSS
- **JavaScript**: Vanilla JS & jQuery
- **Build System**: npm/Gulp
- **Icons**: Nucleo Icons & Font Awesome

Directory Structure
-------------------

.. code-block:: bash

    argon-dashboard/
        ├── assets/
        │   ├── css/
        │   │   ├── argon.css
        │   │   └── argon.min.css
        │   ├── js/
        │   │   ├── argon.js
        │   │   └── argon.min.js
        │   ├── img/
        │   │   ├── brand/
        │   │   └── theme/
        │   ├── fonts/
        │   └── scss/
        │       ├── argon.scss
        │       ├── custom/
        │       └── core/
        ├── docs/
        ├── pages/
        └── gulpfile.js

Core Components
---------------- 

1. Layout Structure
*******************

.. code-block:: html

    <body>
        <!-- Sidenav -->
        <nav class="sidenav navbar navbar-vertical fixed-left navbar-expand-xs navbar-light bg-white">
            <!-- Sidenav content -->
        </nav>
        
        <!-- Main content -->
        <main class="main-content">
            <!-- Navbar -->
            <nav class="navbar navbar-top navbar-expand navbar-dark bg-primary border-bottom">
            <!-- Navbar content -->
            </nav>
            
            <!-- Page content -->
            <div class="container-fluid mt--6">
            <!-- Content -->
            </div>
        </main>
    </body>


2. Navigation Components
************************

Sidebar Navigation
^^^^^^^^^^^^^^^^^^

.. code-block:: html

    <nav class="sidenav navbar navbar-vertical fixed-left navbar-expand-xs navbar-light bg-white">
        <div class="scrollbar-inner">
            <div class="sidenav-header align-items-center">
            <a class="navbar-brand" href="javascript:void(0)">
                <img src="../assets/img/brand/blue.png" class="navbar-brand-img" alt="...">
            </a>
            </div>
            <div class="navbar-inner">
            <div class="collapse navbar-collapse" id="sidenav-collapse-main">
                <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" href="#dashboard">
                    <i class="ni ni-tv-2 text-primary"></i>
                    <span class="nav-link-text">Dashboard</span>
                    </a>
                </li>
                </ul>
            </div>
            </div>
        </div>
    </nav>


3. Cards and Widgets
************************

Basic Card
^^^^^^^^^^

.. code-block:: html

    <div class="card">
        <div class="card-header">
            <h3 class="mb-0">Card Title</h3>
        </div>
        <div class="card-body">
            Content goes here
        </div>
    </div>

Stat Card
^^^^^^^^^^

.. code-block:: html

    <div class="card card-stats">
        <div class="card-body">
            <div class="row">
            <div class="col">
                <h5 class="card-title text-uppercase text-muted mb-0">Total traffic</h5>
                <span class="h2 font-weight-bold mb-0">350,897</span>
            </div>
            <div class="col-auto">
                <div class="icon icon-shape bg-gradient-red text-white rounded-circle shadow">
                <i class="ni ni-active-40"></i>
                </div>
            </div>
            </div>
        </div>
    </div>


Customization
-------------

1. SCSS Variables
***************** 

.. code-block:: scss

    // Core variables
    $primary: #5e72e4;
    $secondary: #f7fafc;
    $success: #2dce89;
    $info: #11cdef;
    $warning: #fb6340;
    $danger: #f5365c;

    // Custom spacing
    $spacer: 1rem;
    $spacers: (
    0: 0,
    1: ($spacer * .25),
    2: ($spacer * .5),
    3: $spacer,
    4: ($spacer * 1.5),
    5: ($spacer * 3)
    );

    // Sidebar variables
    $navbar-vertical-width: 250px;
    $navbar-vertical-padding-x: 1.5rem;


2. Theme Configuration
**********************

.. code-block:: javascript

    // assets/js/argon.js
    'use strict';

    var Layout = (function() {
    function initNavbarCollapse() {
        // Initialize navbar collapse logic
    }
    
    function initColoredShadows() {
        // Initialize colored shadows
    }
    
    return {
        init: function() {
        initNavbarCollapse();
        initColoredShadows();
        }
    };
    })();


Plugin Integration
------------------

1. Chart.js Integration
***********************

.. code-block:: javascript

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
        datasets: [{
        label: 'Sales',
        data: [50, 20, 10, 30, 15, 40, 20],
        borderColor: '#5e72e4'
        }]
    },
    options: {
        responsive: true
    }
    });


2. Datatable Integration
************************

.. code-block:: javascript

    $(document).ready(function() {
        $('#datatable-basic').DataTable({
            responsive: true,
            language: {
                paginate: {
                    previous: "<i class='fas fa-angle-left'>",
                    next: "<i class='fas fa-angle-right'>"
                }
            }
        });
    });

License
-------

- Free Version: MIT License
- PRO Version: Check Creative-Tim's license terms

.. include::  /_templates/components/footer-links.rst
