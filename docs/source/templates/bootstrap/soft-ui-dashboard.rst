`Soft Dashboard <https://www.creative-tim.com/product/soft-ui-dashboard?AFFILIATE=128200>`__
===============================================================================================

.. title:: Soft UI Dashboard -  Modern, Responsive admin template created by Creative-Tim 
.. meta::
    :description: Open-source soft-design dashboard template built on top of Bootstrap 5 

**Soft UI Dashboard** is a modern, responsive dashboard template created by Creative-Tim, built with **Bootstrap 5**.  
This dashboard template combines soft shadows, pastel colors, and carefully crafted lighting effects to create an interface that appears to float above the background. 
The design philosophy emphasizes depth and dimensionality while maintaining excellent readability and user experience.

- 👉 `Soft UI Dashboard <https://www.creative-tim.com/product/soft-ui-dashboard?AFFILIATE=128200>`__ - Product page 
- 👉 `Soft UI Dashboard <https://demos.creative-tim.com/soft-ui-dashboard/pages/dashboard.html?AFFILIATE=128200>`__ - Live Demo

.. include::  /_templates/components/banner-top.rst

The dashboard is available in several technology stacks to suit different development needs. 
You can find it implemented in plain Bootstrap 5, React, Vue.js, Angular, and Laravel versions. Each version maintains the core Soft UI aesthetic while leveraging the strengths of its respective framework.

.. image:: https://github.com/user-attachments/assets/b011b4c6-9367-4d04-b1e1-de58d951c6aa
   :alt: Soft UI Dashboard - open-source dashboard template provided by Creative-Tim 

Technical Foundation
--------------------

The dashboard is built on a robust technical foundation. At its core, you'll find Bootstrap 5 handling the heavy lifting of layouts and responsiveness. 
The styling is implemented through SASS, giving you tremendous flexibility in customization. 

The JavaScript layer primarily uses vanilla JS with some jQuery where needed, and it integrates several carefully chosen plugins for specific functionality.

**Here's how the project is structured**:

.. code-block:: bash

    soft-ui-dashboard/
        ├── assets/
        │   ├── css/
        │   │   ├── soft-ui-dashboard.css
        │   │   └── soft-ui-dashboard.min.css
        │   ├── js/
        │   │   ├── core/
        │   │   ├── plugins/
        │   │   └── soft-ui-dashboard.js
        │   ├── img/
        │   └── scss/
        │       ├── soft-ui-dashboard/
        │       └── soft-ui-dashboard.scss
        ├── pages/
        └── documentation/


Building with Soft UI Components
--------------------------------

Let's walk through how to create interfaces using Soft UI's core components. The heart of any dashboard page starts with this basic layout structure:

.. code-block:: html

    <div class="g-sidenav-show">
        <!-- Soft UI Sidenav -->
        <aside class="sidenav navbar navbar-vertical navbar-expand-xs border-0 border-radius-xl my-3 fixed-start ms-3">
            <div class="sidenav-header">
            <i class="fas fa-times p-3 cursor-pointer text-secondary opacity-5 position-absolute end-0 top-0 d-none d-xl-none"></i>
            <a class="navbar-brand m-0" href="#">
                <img src="assets/img/logo-ct.png" class="navbar-brand-img h-100" alt="main_logo">
                <span class="ms-1 font-weight-bold">Soft UI Dashboard</span>
            </a>
            </div>
            
            <hr class="horizontal dark mt-0">
            
            <div class="collapse navbar-collapse w-auto max-height-vh-100 h-100" id="sidenav-collapse-main">
            <!-- Navigation items go here -->
            </div>
        </aside>

        <main class="main-content position-relative max-height-vh-100 h-100 ps">
            <!-- Your page content goes here -->
        </main>
    </div>


One of the most distinctive features of Soft UI is its card design. Here's how to create those characteristic floating cards with soft shadows:

.. code-block:: html

    <div class="card">
        <div class="card-header p-3 pt-2">
            <div class="icon icon-lg icon-shape bg-gradient-dark shadow-dark shadow text-center border-radius-xl mt-n4 position-absolute">
            <i class="material-icons opacity-10">weekend</i>
            </div>
            <div class="text-end pt-1">
            <p class="text-sm mb-0 text-capitalize">Bookings</p>
            <h4 class="mb-0">281</h4>
            </div>
        </div>
        <hr class="dark horizontal my-0">
        <div class="card-footer p-3">
            <p class="mb-0"><span class="text-success text-sm font-weight-bolder">+55% </span>than last week</p>
        </div>
    </div>


Soft UI Customization
---------------------

The visual magic of Soft UI comes from its carefully crafted SCSS variables and mixins. Here's how you can customize the core aspects of your dashboard:

.. code-block:: scss

    // Core theme colors
    $soft-ui-theme-colors: (
        "primary":    #cb0c9f,
        "secondary":  #8392ab,
        "success":    #82d616,
        "info":       #17c1e8,
        "warning":    #fbcf33,
        "danger":     #ea0606,
        "light":      #e9ecef,
        "dark":       #344767
    );

    // Soft shadows that create the characteristic neumorphic effect
    $box-shadow-soft: 0 20px 27px 0 rgba(0, 0, 0, 0.05);

    // The special gradient backgrounds that give depth to the design
    @mixin gradient-background($color) {
        background: linear-gradient(310deg, 
            darken($color, 10%) 0%,
            lighten($color, 10%) 100%
        );
    }


Bringing Charts and Data to Life
--------------------------------

Soft UI Dashboard shines when displaying data. It includes pre-configured chart designs that maintain the soft UI aesthetic. Here's how to create a chart that fits the design language:

.. code-block:: javascript

    const ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
            label: 'Organic Search',
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#cb0c9f",
            borderWidth: 3,
            backgroundColor: gradientStroke1,
            fill: true,
            data: [50, 40, 300, 220, 500, 250, 400, 230, 500],
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
            borderDash: [5, 5]
            },
            ticks: {
            display: true,
            padding: 10,
            color: '#b2b9bf',
            font: {
                size: 11,
                family: "Open Sans",
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
            color: '#b2b9bf',
            padding: 20,
            font: {
                size: 11,
                family: "Open Sans",
                style: 'normal',
                lineHeight: 2
            },
            }
        },
        },
    },
    });

Creating Smooth Interactions
----------------------------

The dashboard's interactivity is built around smooth transitions and subtle animations. Here's how to implement the signature navigation behavior:

.. code-block:: javascript

    // Smooth sidebar toggle
    const iconNavbarSidenav = document.getElementById('iconNavbarSidenav');
    const iconSidenav = document.getElementById('iconSidenav');
    const sidenav = document.getElementById('sidenav-main');
    let body = document.getElementsByTagName('body')[0];
    let className = 'g-sidenav-pinned';

    function toggleSidenav() {
        if (body.classList.contains(className)) {
            body.classList.remove(className);
            setTimeout(function() {
            sidenav.classList.remove('bg-white');
            }, 100);
            sidenav.classList.remove('bg-transparent');
        } else {
            body.classList.add(className);
            sidenav.classList.add('bg-white');
            sidenav.classList.remove('bg-transparent');
            iconSidenav.classList.remove('d-none');
        }
    }


Making It Your Own
------------------

The true power of Soft UI Dashboard lies in its customizability. You can adjust the design system to match your brand while maintaining the soft UI aesthetic. Some key areas to consider:

1. Color Scheme: Modify the primary colors while maintaining the soft gradients and shadows
2. Typography: The dashboard uses the "Open Sans" font family, but you can easily switch to your preferred typeface
3. Spacing: Adjust the padding and margin variables to create your desired layout density
4. Shadows: Fine-tune the shadow values to increase or decrease the neumorphic effect

Getting Help and Support
------------------------

The Soft UI Dashboard comes with comprehensive support options. You'll find detailed documentation at Creative-Tim's website, and their support team is ready to help with technical questions. 
The community forum is also an excellent resource for sharing experiences and solutions with other developers using the dashboard.

Remember that while the free version includes the core features, the PRO version offers additional components, plugins, and example pages that might speed up your development process.

.. include::  /_templates/components/footer-links.rst
