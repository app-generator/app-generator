`StarAdmin <https://www.bootstrapdash.com/product/star-admin-free>`__
=====================================================================

.. title:: StarAdmin -  Iconic admin template crafted by BootstrapDash
.. meta::
    :description: Open-source material-design dashboard styled with Bootstrap 

**StarAdmin** is a clean and minimalist Bootstrap admin template that focuses on simplicity and usability. 
The template distinguishes itself through its crisp design, straightforward layout structure, and efficient use of white space. 

- 👉 `StarAdmin <https://www.bootstrapdash.com/product/star-admin-free>`__ - Product page 

It's particularly well-suited for projects that require a clean, professional interface without overwhelming visual elements.

.. include::  /_templates/components/banner-top.rst

.. image:: https://github.com/user-attachments/assets/0323c09e-3482-470c-8198-65d57f75656f
   :alt: StarAdmin - Clean and minimalist Bootstrap admin template

Project Information
-------------------

Star Admin Free is an admin dashboard template built on Bootstrap 5, featuring a light theme with predominantly blue elements that enhance readability and provide a professional appearance. 

It includes a default admin dashboard layout, various UI elements such as buttons, dropdowns, and typography, and offers multiple form elements, charts, tables, icons, and user pages. 

This comprehensive solution for admin dashboard is customizable under the MIT license, allowing users to create a unique interface. 

Project Architecture
--------------------

The template follows a well-organized structure:

.. code-block:: bash

    staradmin/
        ├── dist/                     # Production-ready files
        ├── src/
        │   ├── assets/
        │   │   ├── css/
        │   │   │   ├── style.css
        │   │   │   └── vendor.css
        │   │   ├── fonts/
        │   │   ├── images/
        │   │   ├── js/
        │   │   │   ├── off-canvas.js
        │   │   │   ├── hoverable-collapse.js
        │   │   │   ├── misc.js
        │   │   │   └── dashboard.js
        │   │   └── scss/
        │   │       ├── components/
        │   │       ├── mixins/
        │   │       ├── vendor/
        │   │       └── style.scss
        │   ├── pages/
        │   └── partials/
        ├── gulp-tasks/
        ├── documentation/
        └── package.json

Component System
----------------

Cards and Widgets
*****************

StarAdmin provides clean, minimal card designs:

.. code-block:: html 

    <div class="card">
        <div class="card-body">
            <h4 class="card-title">Basic Card</h4>
            <p class="card-description">Basic card content</p>
            <div class="card-stats">
                <div class="d-flex justify-content-between align-items-center">
                    <div class="statistics">
                        <p class="statistics-title">Bounce Rate</p>
                        <h3 class="rate-percentage">32.53%</h3>
                        <p class="text-danger d-flex">
                            <i class="mdi mdi-menu-down"></i>
                            <span>-0.5%</span>
                        </p>
                    </div>
                    <div class="icon-statistics">
                        <i class="mdi mdi-chart-line"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>    


Navigation Components
*********************

.. code-block:: html 

    <nav class="sidebar sidebar-offcanvas" id="sidebar">
        <ul class="nav">
            <li class="nav-item nav-profile">
                <div class="nav-profile-image">
                    <img src="assets/images/faces/face1.jpg" alt="profile">
                    <span class="login-status online"></span>
                </div>
                <div class="nav-profile-text">
                    <span class="font-weight-bold mb-2">David Grey</span>
                    <span class="text-secondary text-small">Project Manager</span>
                </div>
            </li>
            
            <li class="nav-item">
                <a class="nav-link" href="index.html">
                    <i class="mdi mdi-home menu-icon"></i>
                    <span class="menu-title">Dashboard</span>
                </a>
            </li>
            
            <li class="nav-item">
                <a class="nav-link" data-toggle="collapse" href="#ui-basic" aria-expanded="false">
                    <i class="mdi mdi-crosshairs-gps menu-icon"></i>
                    <span class="menu-title">UI Elements</span>
                    <i class="menu-arrow"></i>
                </a>
                <div class="collapse" id="ui-basic">
                    <ul class="nav flex-column sub-menu">
                        <li class="nav-item">
                            <a class="nav-link" href="pages/ui-features/buttons.html">Buttons</a>
                        </li>
                    </ul>
                </div>
            </li>
        </ul>
    </nav>

Chart Integration
-----------------

StarAdmin integrates smoothly with **Chart.js**:

.. code-block:: javascript

    // Line chart configuration
    const lineChartConfig = {
        type: 'line',
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            datasets: [{
                label: 'Revenue',
                data: [10, 19, 3, 5, 2, 3],
                borderColor: '#464dee',
                backgroundColor: 'rgba(70, 77, 238, 0.1)',
                borderWidth: 2,
                fill: true
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            legend: {
                display: false
            },
            elements: {
                point: {
                    radius: 0
                }
            }
        }
    };

    // Initialize chart
    new Chart(document.getElementById('lineChart'), lineChartConfig);     

Support Resources
------------------

- Documentation: Available in the package
- Support Email: Listed in the documentation
- Updates: Through npm
- Community: GitHub issues and discussions

.. include::  /_templates/components/footer-links.rst
