`Datta Able <https://codedthemes.com/item/datta-able-bootstrap-lite/?ref=appseed>`__
====================================================================================

**Datta Able** represents CodedThemes' vision of a modern, flexible admin dashboard framework. 
It combines clean design principles with powerful functionality, making it suitable for a wide range of administrative interfaces.
The template stands out for its extensive customization options and well-organized codebase.

- 👉 `Datta Able <https://codedthemes.com/item/datta-able-bootstrap-lite/?ref=appseed>`__ - Product page 
- 👉 `Datta Able <https://lite.codedthemes.com/datta-able/bootstrap/?ref=appseed>`__ - Live Demo

.. include::  /_templates/components/banner-top.rst

.. image:: https://github.com/user-attachments/assets/a586e400-3337-4004-b2e1-610fe885c2ef
   :alt: Datta Able - open-source dashboard template provided by CodedThemes

Available Versions 
------------------

Datta Able is available in several technological implementations:

- Bootstrap (Default version)
- React
- Angular
- Vue.js
- Laravel
- ASP.NET Core
- Django

Core Architecture
-----------------

The dashboard follows a modular architecture that promotes maintainability and scalability. Here's the project structure:

.. code-block:: bash 

    datta-able/
        ├── dist/                  # Production build files
        ├── src/
        │   ├── assets/
        │   │   ├── css/
        │   │   │   ├── style.css
        │   │   │   └── layouts/
        │   │   ├── js/
        │   │   │   ├── vendor/
        │   │   │   ├── pages/
        │   │   │   └── menu-setting.js
        │   │   ├── scss/
        │   │   │   ├── themes/
        │   │   │   ├── components/
        │   │   │   └── style.scss
        │   │   └── images/
        │   ├── html/
        │   │   ├── layouts/
        │   │   └── components/
        │   └── plugins/          # Third-party plugins
        └── documentation/


Building Layouts with Datta Able
--------------------------------

The foundation of any Datta Able page starts with this basic structure:

.. code-block:: html 

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Datta Able</title>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        
        <!-- Datta Able CSS -->
        <link rel="stylesheet" href="assets/css/style.css">
    </head>
    <body>
        <!-- [ Pre-loader ] start -->
        <div class="loader-bg">
            <div class="loader-track">
                <div class="loader-fill"></div>
            </div>
        </div>

        <!-- [ navigation menu ] start -->
        <nav class="pcoded-navbar">
            <div class="navbar-wrapper">
                <div class="navbar-brand header-logo">
                    <a href="index.html" class="b-brand">
                        <div class="b-bg">
                            <i class="feather icon-trending-up"></i>
                        </div>
                        <span class="b-title">Datta Able</span>
                    </a>
                    <a class="mobile-menu" id="mobile-collapse" href="javascript:"><span></span></a>
                </div>
                <div class="navbar-content scroll-div">
                    <!-- Navigation items -->
                </div>
            </div>
        </nav>

        <!-- [ Header ] start -->
        <header class="navbar pcoded-header navbar-expand-lg navbar-light">
            <div class="m-header">
                <a class="mobile-menu" id="mobile-collapse1" href="javascript:"><span></span></a>
                <a href="index.html" class="b-brand">
                    <div class="b-bg">
                        <i class="feather icon-trending-up"></i>
                    </div>
                    <span class="b-title">Datta Able</span>
                </a>
            </div>
            <a class="mobile-menu" id="mobile-header" href="javascript:">
                <i class="feather icon-more-horizontal"></i>
            </a>
            <!-- Header content -->
        </header>

        <!-- [ Main Content ] start -->
        <div class="pcoded-main-container">
            <div class="pcoded-wrapper">
                <div class="pcoded-content">
                    <div class="pcoded-inner-content">
                        <!-- Page content goes here -->
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>


Theme Configuration System
--------------------------

Datta Able implements a sophisticated theming system through SCSS variables and mixins:

.. code-block:: scss

    // Theme colors
    $theme-colors: (
        primary: #04a9f5,
        secondary: #9C27B0,
        success: #2ed8b6,
        info: #00bcd4,
        warning: #FFB64D,
        danger: #FF5370,
        dark: #223035,
        light: #f2f2f2
    );

    // Layout configurations
    $header-height: 70px;
    $menu-width: 264px;
    $menu-collapsed-width: 70px;

    // Menu customization
    .pcoded-navbar {
        &.menu-light {
            background: #fff;
            color: $theme-dark;
            
            .pcoded-inner-navbar {
                > li {
                    &.active > a,
                    &:focus > a,
                    &:hover > a {
                        color: $primary-color;
                    }
                }
            }
        }
    }


Component Implementation
------------------------

Let's examine how to implement some key components:

Cards with Advanced Features
****************************

.. code-block:: html

    <div class="card">
        <div class="card-header">
            <h5>Card Title</h5>
            <div class="card-header-right">
                <div class="btn-group card-option">
                    <button type="button" class="btn dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="feather icon-more-horizontal"></i>
                    </button>
                    <ul class="list-unstyled card-option dropdown-menu dropdown-menu-right">
                        <li class="dropdown-item full-card">
                            <a href="javascript:"><span><i class="feather icon-maximize"></i> maximize</span></a>
                        </li>
                        <li class="dropdown-item minimize-card">
                            <a href="javascript:"><span><i class="feather icon-minus"></i> collapse</span></a>
                        </li>
                        <li class="dropdown-item reload-card">
                            <a href="javascript:"><span><i class="feather icon-refresh-cw"></i> reload</span></a>
                        </li>
                        <li class="dropdown-item close-card">
                            <a href="javascript:"><span><i class="feather icon-trash"></i> remove</span></a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="card-body">
            <p class="mb-0">Card content</p>
        </div>
    </div>


### Interactive Data Tables

.. code-block:: javascript

    $(document).ready(function() {
        $('#advanced-table').DataTable({
            responsive: true,
            select: true,
            dom: 'Bfrtip',
            buttons: [
                'copy', 'csv', 'excel', 'pdf', 'print'
            ],
            initComplete: function() {
                var api = this.api();
                api.$('.switchery').each(function() {
                    new Switchery(this, { color: '#04a9f5' });
                });
            }
        });
    });

Advanced Features and Customization
-----------------------------------

Layout Configuration
********************

Datta Able provides layout control through data attributes:

.. code-block:: html

    <body data-layout-type="vertical" data-nav-headerbg="blue" data-headerbg="blue">
        <!-- This will create a vertical layout with blue header and navigation -->
    </body>

Menu Configuration
******************

The menu system can be customized through JavaScript:

.. code-block:: javascript

    // Menu configuration object
    var menuConfig = {
        layout: 'vertical', // vertical, horizontal
        navFixed: true,
        headerFixed: false,
        themeColor: 'blue', // blue, red, purple, theme1, theme2
        menuDropdownIcon: 'style1', // style1, style2, style3
        menuListIcon: 'style1' // style1, style2, style3
    };

    // Initialize menu with configuration
    $(document).ready(function() {
        $('#pcoded').pcodedmenu(menuConfig);
    });


Chart Integration
*****************

Datta Able comes with pre-configured chart options that match its design language:

.. code-block:: javascript

    // Area chart configuration
    var areaChartConfig = {
        chart: {
            height: 350,
            type: 'area',
            toolbar: {
                show: false
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth',
            width: 2
        },
        colors: ['#04a9f5', '#2ed8b6'],
        series: [{
            name: 'Series 1',
            data: [31, 40, 28, 51, 42, 109, 100]
        }],
        xaxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        },
        tooltip: {
            theme: 'dark'
        }
    };

    // Initialize chart
    var chart = new ApexCharts(
        document.querySelector("#area-chart"),
        areaChartConfig
    );
    chart.render();

Browser Compatibility and Support
**********************************

Datta Able is tested and optimized for:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Opera (latest)
- Internet Explorer 11 (basic support)

Development Workflow
********************

Here's a recommended workflow for developing with Datta Able:

1. Initial Setup

.. code-block:: bash

    # Install dependencies
    npm install

    # Start development server
    npm run start

    # Build for production
    npm run build


2. Customization Steps

- Modify SCSS variables in `src/scss/themes/_variables.scss`
- Add custom components in `src/scss/components/`
- Update layouts in `src/html/layouts/`
- Add new pages in `src/html/pages/`

Help and Support
****************

For assistance with Datta Able:
- Visit the official documentation on CodedThemes website
- Check the GitHub repository issues
- Contact CodedThemes support team
- Join the community forum

Remember to keep your installation updated with the latest version to receive bug fixes and new features. The template is actively maintained and regularly updated by CodedThemes.

.. include::  /_templates/components/footer-links.rst
