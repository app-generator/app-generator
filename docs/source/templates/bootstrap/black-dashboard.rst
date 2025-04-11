`Black Dashboard </product/black-dashboard/>`__
===============================================

.. title:: Black Dashboard -  Modern, dark-themed admin template created by Creative-Tim 
.. meta::
    :description: Open-source dark-themed dashboard and control panel styled with Bootstrap CSS

`Black Dashboard </product/black-dashboard/>`__ is a premium Bootstrap 4 admin template designed by `Creative Tim </agency/creative-tim/>`__. 
It features a dark-themed design language with vibrant accent colors and a modern, sleek interface ideal for modern web applications and admin panels.

    👉 `Black Dashboard Starters </product/black-dashboard/>`__ - Bundle provided by `App Generator </>`__ platorm

The template provides a well-curated selection of essential components and page layouts necessary for creating effective dashboard interfaces. 
Its streamlined structure combines visual impact with practical functionality, making it suitable for developers seeking to create dashboards with a contemporary look.

.. image:: https://github.com/user-attachments/assets/b26c6a1c-b10a-4e5a-8145-fefbeb54ef88
   :alt: Black Dashboard - open-source dashboard template provided by Creative-Tim 

**Black Dashboard** serves as an excellent starting point for various web applications including creative project management tools, media control panels, basic monitoring interfaces, and stylish business applications. 
Its responsive design ensures consistent performance across devices, adapting smoothly from desktop workstations to mobile screens.

Available Versions
------------------

- Bootstrap 4/5 (Free & PRO)
- React.js
- Vue.js
- Angular
- Laravel
- Node.js

Key Features
------------

- Dark theme design
- Bootstrap 4/5 Framework
- SCSS files included
- Responsive layout
- Custom dark-themed components
- Gradient cards and backgrounds
- Premium plugins integration
- Regular updates
- MIT License (Free version)

Technical Stack
----------------

- **Frontend Framework**: Bootstrap 4/5
- **CSS Preprocessor**: SASS/SCSS
- **JavaScript**: jQuery
- **Charts**: Chart.js
- **Icons**: Nucleo Icons & Font Awesome
- **Notifications**: Bootstrap Notify
- **Perfect Scrollbar**: Custom scrollbars

Directory Structure
-------------------

.. code-block:: bash

    black-dashboard/
        ├── assets/
        │   ├── css/
        │   │   ├── black-dashboard.css
        │   │   └── black-dashboard.min.css
        │   ├── demo/
        │   ├── fonts/
        │   ├── img/
        │   ├── js/
        │   │   ├── core/
        │   │   ├── plugins/
        │   │   ├── black-dashboard.js
        │   │   └── black-dashboard.min.js
        │   └── scss/
        │       ├── black-dashboard.scss
        │       └── black-dashboard/
        │           ├── bootstrap/
        │           ├── custom/
        │           └── plugins/
        ├── docs/
        ├── examples/
        └── gulpfile.js


Core Components
---------------

1. Basic Layout Structure
*************************

.. code-block:: html

    <body class="dark-theme">
        <!-- Sidebar -->
        <div class="sidebar">
            <div class="sidebar-wrapper">
            <!-- Sidebar content -->
            </div>
        </div>

        <div class="main-panel">
            <!-- Navbar -->
            <nav class="navbar navbar-expand-lg navbar-absolute navbar-transparent">
                
            </nav>

            <!-- Main content -->
            <div class="content">
                <div class="container-fluid">
                    <!-- Page content -->
                </div>
            </div>
        </div>
    </body>


2. Sidebar Component
********************

.. code-block:: html

    <div class="sidebar">
        <div class="sidebar-wrapper">
            <div class="logo">
            <a href="javascript:void(0)" class="simple-text logo-mini">
                BD
            </a>
            <a href="javascript:void(0)" class="simple-text logo-normal">
                Black Dashboard
            </a>
            </div>
            <ul class="nav">
            <li class="active">
                <a href="./dashboard.html">
                <i class="tim-icons icon-chart-pie-36"></i>
                <p>Dashboard</p>
                </a>
            </li>
            <!-- More nav items -->
            </ul>
        </div>
    </div>

3. Card Components
******************

Gradient Card
^^^^^^^^^^^^^

.. code-block:: html

    <div class="card card-chart">
        <div class="card-header">
            <h4 class="card-title">Gradient Card</h4>
            <div class="dropdown">
            <button type="button" class="btn btn-link dropdown-toggle btn-icon">
                <i class="tim-icons icon-settings-gear-63"></i>
            </button>
            </div>
        </div>
        <div class="card-body">
            <div class="chart-area">
            <canvas id="chartBig1"></canvas>
            </div>
        </div>
    </div>


Stat Card
^^^^^^^^^

.. code-block:: html

    <div class="card card-stats">
        <div class="card-body">
            <div class="row">
            <div class="col-5">
                <div class="info-icon text-center icon-warning">
                <i class="tim-icons icon-chat-33"></i>
                </div>
            </div>
            <div class="col-7">
                <div class="numbers">
                <p class="card-category">Number</p>
                <h3 class="card-title">150GB</h3>
                </div>
            </div>
            </div>
        </div>
    </div>

Theme Customization
-------------------

1. SCSS Variables
*****************

.. code-block:: html

    // Core Colors
    $default: #344675;
    $primary: #e14eca;
    $secondary: #f4f5f7;
    $success: #00f2c3;
    $info: #1d8cf8;
    $warning: #ff8d72;
    $danger: #fd5d93;

    // Background Colors
    $background-black: #1e1e2f;
    $background-states-black: #1e1e24;

    // Card Variables
    $card-black-background: #27293d;
    $card-shadow: 0 1px 20px 0px rgba(0, 0, 0, 0.1);

    // Sidebar Variables
    $sidebar-width: 260px;
    $sidebar-mini-width: 80px;


2. Theme Modes
**************

.. code-block:: javascript

    // Theme toggle functionality
    function toggleTheme() {
        const body = document.getElementsByTagName('body')[0];
        if (body.classList.contains('white-content')) {
            body.classList.remove('white-content');
        } else {
            body.classList.add('white-content');
        }
    }


Charts Integration
------------------

1. Chart.js Configuration
*************************

.. code-block:: javascript

    var ctx = document.getElementById('chartBig1').getContext('2d');
    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);
    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.1)');
    gradientStroke.addColorStop(0.4, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)');

    var config = {
    type: 'line',
    data: {
        labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL'],
        datasets: [{
            label: "Data",
            fill: true,
            backgroundColor: gradientStroke,
            borderColor: '#d346b1',
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: '#d346b1',
            pointBorderColor: 'rgba(255,255,255,0)',
            pointHoverBackgroundColor: '#d346b1',
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            data: [80, 160, 200, 160, 250, 280, 220]
        }]
    },
    options: {
        // Chart options
    }
    };


Created with practical implementation in mind, this template includes carefully selected components that deliver core functionality without unnecessary complexity. 
The demonstration version illustrates a thoughtfully implemented example, highlighting the template's distinctive visual approach while showing how it can be adapted to meet specific project requirements without extensive customization.

.. include::  /_templates/components/footer-links.rst
