`Material Dashboard <https://www.creative-tim.com/product/material-dashboard?AFFILIATE=128200>`__
=================================================================================================

**Material Dashboard** beautifully implements Google's Material Design principles in a modern dashboard interface. 
Created by Creative-Tim, this dashboard brings together the best of Material Design's visual language with practical dashboard functionality.
It's more than just a template – it's a complete design system that helps you build consistent, modern web applications.

- 👉 `Material Dashboard <https://www.creative-tim.com/product/material-dashboard?AFFILIATE=128200>`__ - Product page 
- 👉 `Material Dashboard <https://demos.creative-tim.com/material-dashboard/pages/dashboard.html?AFFILIATE=128200>`__ - Live Demo

.. include::  /_templates/components/banner-top.rst

The dashboard comes in several editions: a free Bootstrap version, a PRO version with additional components, and framework-specific versions for React, Vue, and Angular. 
Each version maintains strict adherence to Material Design principles while leveraging the strengths of its respective technology stack.

.. image:: https://github.com/user-attachments/assets/532e06c1-1af3-4439-93fc-6de3a9d43c52
   :alt: Material Dashboard - open-source dashboard template provided by Creative-Tim 

The Material Design Foundation
------------------------------

Material Dashboard builds upon these core Material Design concepts:

.. code-block:: scss

    // Core elevation shadows that create depth
    $shadow-key-umbra-opacity: 0.2;
    $shadow-key-penumbra-opacity: 0.14;
    $shadow-ambient-shadow-opacity: 0.12;

    // The dashboard uses Material's elevation levels
    $mdb-shadow-2dp: 0 2px 2px 0 rgba(0, 0, 0, $shadow-key-penumbra-opacity),
                    0 3px 1px -2px rgba(0, 0, 0, $shadow-key-umbra-opacity),
                    0 1px 5px 0 rgba(0, 0, 0, $shadow-ambient-shadow-opacity);

    // Material's signature color palette
    $primary: (
    "main": #9c27b0,
    "light": #ab47bc,
    "dark": #8e24aa,
    "contrast": #ffffff
    );


Project Organization
--------------------

The dashboard follows a thoughtful organization structure that separates concerns and makes maintenance straightforward:

.. code-block:: bash 

    material-dashboard/
        ├── assets/
        │   ├── css/
        │   │   ├── material-dashboard.css
        │   │   └── material-dashboard.min.css
        │   ├── js/
        │   │   ├── core/
        │   │   ├── plugins/
        │   │   └── material-dashboard.js
        │   ├── scss/
        │   │   ├── material-dashboard/
        │   │   │   ├── bootstrap/
        │   │   │   ├── plugins/
        │   │   │   └── variables/
        │   │   └── material-dashboard.scss
        │   └── img/
        ├── pages/
        └── documentation/


Building Material Interfaces
----------------------------

Let's walk through creating interfaces that embody Material Design principles. Here's the foundation of a Material Dashboard page:

.. code-block:: html

    <body class="g-sidenav-show bg-gray-200">
        <!-- Material Sidenav -->
        <aside class="sidenav navbar navbar-vertical navbar-expand-xs border-0 border-radius-xl my-3 fixed-start ms-3 bg-gradient-dark" id="sidenav-main">
            <div class="sidenav-header">
            <a class="navbar-brand m-0" href="#">
                <span class="ms-1 font-weight-bold text-white">Material Dashboard</span>
            </a>
            </div>

            <hr class="horizontal light mt-0 mb-2">

            <div class="collapse navbar-collapse w-auto" id="sidenav-collapse-main">
            <ul class="navbar-nav">
                <!-- Navigation items with Material icons -->
            </ul>
            </div>
        </aside>

        <main class="main-content position-relative max-height-vh-100 h-100 border-radius-lg">
            <!-- Your content goes here -->
        </main>
    </body>


Material cards are a fundamental building block. Here's how to create them properly:

.. code-block:: html

    <div class="card">
        <div class="card-header p-3 pt-2">
            <div class="icon icon-lg icon-shape bg-gradient-primary shadow-primary text-center border-radius-xl mt-n4 position-absolute">
            <i class="material-icons opacity-10">weekend</i>
            </div>
            <div class="text-end pt-1">
            <p class="text-sm mb-0 text-capitalize">Today's Users</p>
            <h4 class="mb-0">2,300</h4>
            </div>
        </div>
        <hr class="dark horizontal my-0">
        <div class="card-footer p-3">
            <p class="mb-0"><span class="text-success text-sm font-weight-bolder">+3% </span>than yesterday</p>
        </div>
    </div>


Working with Material Design Components
---------------------------------------

Material Dashboard includes carefully crafted components that follow Material Design specifications. Here's how to implement some key components:

Material Buttons
****************

.. code-block:: html

    <!-- Contained button (raised) -->
    <button class="btn bg-gradient-primary">Primary</button>

    <!-- Text button (flat) -->
    <button class="btn btn-text">Text Button</button>

    <!-- Outlined button -->
    <button class="btn btn-outline-primary">Outlined</button>

    <!-- Button with icon -->
    <button class="btn bg-gradient-primary">
        <i class="material-icons">favorite</i>
        With Icon
    </button>

Material Form Controls
**********************

.. code-block:: html

    <div class="input-group input-group-outline">
        <label class="form-label">Email</label>
        <input type="email" class="form-control">
    </div>

    <div class="form-check">
        <input class="form-check-input" type="checkbox" id="customCheck1">
        <label class="custom-control-label" for="customCheck1">Remember me</label>
    </div>

Implementing Material Data Visualizations
*****************************************

Charts and data displays in Material Dashboard follow Material Design's data visualization guidelines. Here's how to create a chart that adheres to these principles:

.. code-block:: javascript

    const ctx = document.getElementById('materialChart').getContext('2d');
    new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
            datasets: [{
            label: 'Sales',
            tension: 0,
            borderWidth: 0,
            pointRadius: 5,
            pointBackgroundColor: 'rgba(255, 255, 255, .8)',
            pointBorderColor: 'transparent',
            borderColor: 'rgba(255, 255, 255, .8)',
            borderColor: 'rgba(255, 255, 255, .8)',
            borderWidth: 4,
            backgroundColor: 'transparent',
            fill: true,
            data: [50, 40, 300, 320, 500, 350, 200],
            maxBarThickness: 6
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
        legend: {
            display: false,
        }
        },
        interaction: {
        intersect: false,
        mode: 'index',
        },
        scales: {
        y: {
            grid: {
            drawBorder: false,
            display: true,
            drawOnChartArea: true,
            drawTicks: false,
            borderDash: [5, 5],
            color: 'rgba(255, 255, 255, .2)'
            },
            ticks: {
            display: true,
            color: '#f8f9fa',
            padding: 10,
            font: {
                size: 14,
                weight: 300,
                family: "Roboto",
                style: 'normal',
                lineHeight: 2
            },
            }
        },
        x: {
            grid: {
            drawBorder: false,
            display: false,
            drawOnChartArea: false,
            drawTicks: false,
            borderDash: [5, 5]
            },
            ticks: {
            display: true,
            color: '#f8f9fa',
            padding: 10,
            font: {
                size: 14,
                weight: 300,
                family: "Roboto",
                style: 'normal',
                lineHeight: 2
            },
            }
        },
        },
    },
    });

Material Colors and Typography
------------------------------

Material Design's color system is based on intentional, accessible choices. Here's how to implement the color system:

.. code-block:: scss

    // Primary colors
    $md-primary: (
        50: #e3f2fd,
        100: #bbdefb,
        200: #90caf9,
        300: #64b5f6,
        400: #42a5f5,
        500: #2196f3,  // Primary color
        600: #1e88e5,
        700: #1976d2,
        800: #1565c0,
        900: #0d47a1
    );

    // Material typography
    body {
        font-family: Roboto, "Helvetica Neue", sans-serif;
        font-size: 1rem;
        font-weight: 400;
        line-height: 1.5;
        letter-spacing: 0.00938em;
    }

    h1 {
        font-size: 6rem;
        font-weight: 300;
        line-height: 1.167;
        letter-spacing: -0.01562em;
    }

Animations and Transitions
--------------------------

Material Design is known for its meaningful animations. Here's how to implement Material motion:

.. code-block:: scss

    // Standard Material easing
    $ease-standard: cubic-bezier(0.4, 0.0, 0.2, 1);
    $ease-decelerate: cubic-bezier(0.0, 0.0, 0.2, 1);
    $ease-accelerate: cubic-bezier(0.4, 0.0, 1, 1);

    .md-element {
        transition: all 200ms $ease-standard;
        
        &:hover {
            transform: translateY(-2px);
            box-shadow: $mdb-shadow-2dp;
        }
    }

Getting Started with Development
--------------------------------

To begin working with Material Dashboard:

1. Install dependencies: `npm install`
2. Start development server: `npm start`
3. Build for production: `npm run build`

Remember to check the documentation on Creative-Tim's website for detailed guides and examples. 
The Material Design guidelines (material.io) are also an invaluable resource for understanding the design principles being implemented.

The dashboard supports modern browsers and maintains backwards compatibility according to Material Design's browser support guidelines. 
Regular updates ensure compatibility with the latest Material Design specifications and web standards.

.. include::  /_templates/components/footer-links.rst
