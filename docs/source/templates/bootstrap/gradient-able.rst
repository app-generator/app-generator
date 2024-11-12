`Gradient Able <https://codedthemes.com/item/gradient-able-bootstrap-lite/?ref=appseed>`__
==========================================================================================

.. title:: Gradient Able -  Pixel-perfect, colorfull and responsive admin template created by CodedThemes
.. meta::
    :description: Open-source admin template styled with Bootstrap 5 - Gradient Design Kit

**Gradient Able** differentiates itself through its extensive use of vibrant gradients and modern design aesthetics. 
This admin template from CodedThemes emphasizes visual hierarchy through carefully crafted color transitions and gradient overlays, 
making it particularly suitable for data-rich applications where visual distinction between elements is crucial.

- 👉 `Gradient Able <https://codedthemes.com/item/gradient-able-bootstrap-lite/?ref=appseed>`__ - Product page 
- 👉 `Gradient Able <https://lite.codedthemes.com/gradient-able/bootstrap/?ref=appseed>`__ - Live Demo

.. include::  /_templates/components/banner-top.rst

.. image:: https://github.com/user-attachments/assets/28de9e57-9e9c-4ae5-baa5-799ecbb2d52c
   :alt: Gradient Able - open-source dashboard template provided by CodedThemes

Framework Availability
----------------------

The dashboard template is available in multiple technological implementations:
- HTML/CSS/jQuery (Classic version)
- React.js (with Redux support)
- Angular
- Vue.js
- Laravel
- Django
- ASP.NET Core

Core Architecture
-----------------

The template follows a structured organization that emphasizes its gradient-based design system:

.. code-block:: bash 

    gradient-able/
        ├── dist/
        │   ├── assets/
        │   │   ├── css/
        │   │   ├── js/
        │   │   └── images/
        ├── src/
        │   ├── assets/
        │   │   ├── scss/
        │   │   │   ├── themes/
        │   │   │   │   ├── _gradients.scss
        │   │   │   │   ├── _variables.scss
        │   │   │   │   └── _components.scss
        │   │   │   ├── partials/
        │   │   │   └── style.scss
        │   │   ├── js/
        │   │   │   ├── vendor/
        │   │   │   ├── pages/
        │   │   │   └── core.js
        │   ├── html/
        │   │   ├── layouts/
        │   │   └── components/
        │   └── plugins/
        └── documentation/

The Gradient Design System
--------------------------

Gradient Able's signature look comes from its carefully crafted gradient system:

.. code-block:: scss

    // Core gradient definitions
    $gradient-colors: (
        primary: (
            start: #1de9b6,
            end: #1dc4e9
        ),
        danger: (
            start: #FF5370,
            end: #ff869a
        ),
        warning: (
            start: #f4c22b,
            end: #f1dfa7
        ),
        info: (
            start: #3c4fb1,
            end: #33b5e5
        ),
        dark: (
            start: #4099ff,
            end: #73b4ff
        )
    );

    // Gradient mixing function
    @function create-gradient($direction, $start-color, $end-color) {
        @return linear-gradient($direction, $start-color, $end-color);
    }

    // Gradient generator mixin
    @mixin gradient-background($type: 'primary', $direction: 45deg) {
        $colors: map-get($gradient-colors, $type);
        background: create-gradient(
            $direction,
            map-get($colors, 'start'),
            map-get($colors, 'end')
        );
    }

Basic Layout Structure
----------------------

Here's the foundational layout structure for Gradient Able pages:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Gradient Able</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="assets/css/style.css">
    </head>
    <body>
        <!-- [ Pre-loader ] start -->
        <div class="loader-bg">
            <div class="loader-track">
                <div class="loader-fill"></div>
            </div>
        </div>
        
        <!-- [ Navigation Menu ] start -->
        <nav class="pcoded-navbar menu-light">
            <div class="navbar-wrapper">
                <div class="navbar-content scroll-div">
                    <!-- Navigation content -->
                </div>
            </div>
        </nav>
        
        <!-- [ Header ] start -->
        <header class="navbar pcoded-header navbar-expand-lg header-blue">
            <!-- Header content -->
        </header>
        
        <!-- [ Main Content ] start -->
        <div class="pcoded-main-container">
            <div class="pcoded-content">
                <!-- Content goes here -->
            </div>
        </div>
    </body>
    </html>

Component Implementation
------------------------

Let's look at some key components that showcase Gradient Able's design approach:

Gradient Cards
**************

.. code-block:: html

    <div class="card">
        <div class="card-header gradient-card-header bg-primary">
            <h5 class="text-white">Gradient Card</h5>
            <div class="card-header-right">
                <div class="btn-group card-option">
                    <button type="button" class="btn dropdown-toggle" data-toggle="dropdown">
                        <i class="feather icon-more-horizontal"></i>
                    </button>
                    <ul class="list-unstyled card-option dropdown-menu dropdown-menu-right">
                        <li><i class="feather icon-maximize full-card"></i></li>
                        <li><i class="feather icon-minus minimize-card"></i></li>
                        <li><i class="feather icon-refresh-cw reload-card"></i></li>
                        <li><i class="feather icon-trash close-card"></i></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="card-body">
            <p>Card content goes here</p>
        </div>
    </div>


Gradient Buttons
****************

.. code-block:: html

    <button class="btn bg-gradient-primary">Primary Gradient</button>
    <button class="btn bg-gradient-secondary">Secondary Gradient</button>
    <button class="btn btn-gradient-success">Success Gradient</button>
    <button class="btn btn-gradient-danger">Danger Gradient</button>

Gradient Charts
***************

.. code-block:: javascript

    // Area chart with gradient
    const gradientChart = {
        chart: {
            height: 350,
            type: 'area',
            toolbar: {
                show: false
            }
        },
        colors: ['#1de9b6', '#1dc4e9'],
        fill: {
            type: 'gradient',
            gradient: {
                shadeIntensity: 1,
                opacityFrom: 0.7,
                opacityTo: 0.9,
                stops: [0, 90, 100]
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth',
            width: 2
        },
        series: [{
            name: 'Series 1',
            data: [30, 40, 35, 50, 49, 60, 70]
        }],
        xaxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        }
    };

    new ApexCharts(document.querySelector("#gradient-chart"), gradientChart).render();

Advanced Features
-----------------

Theme Configuration
*******************

Gradient Able provides extensive theme customization options:

.. code-block:: javascript

    const themeConfig = {
        layout: 'vertical', // vertical, horizontal
        themeType: 'gradient', // gradient, default
        gradientColors: {
            primary: {
                start: '#1de9b6',
                end: '#1dc4e9'
            },
            // Add custom gradients
        },
        navbarGradient: true,
        headerGradient: true,
        sidebarGradient: false
    };

    // Initialize theme
    document.addEventListener('DOMContentLoaded', function() {
        GradientAble.init(themeConfig);
    });

Navigation System
*****************

The navigation system supports gradient backgrounds and hover effects:

.. code-block:: scss

    .pcoded-navbar {
        &.menu-gradient {
            @include gradient-background('primary', 180deg);
            
            .nav-link {
                color: rgba(255,255,255,0.8);
                
                &:hover {
                    color: #fff;
                    background: rgba(255,255,255,0.1);
                }
            }
            
            .active {
                background: rgba(255,255,255,0.15);
            }
        }
    }


Animation and Transitions
-------------------------

Gradient Able includes smooth transitions for its gradient effects:

.. code-block:: scss

    // Gradient transition mixin
    @mixin gradient-transition($property: all, $duration: 0.3s) {
        transition: $property $duration ease-in-out;
        background-size: 200% auto;
        
        &:hover {
            background-position: right center;
        }
    }

    // Implementation
    .btn-gradient {
        @include gradient-background('primary');
        @include gradient-transition;
    }

Development Best Practices
--------------------------

1. Gradient Usage Guidelines:
   - Use gradients purposefully to highlight important elements
   - Maintain consistent gradient directions
   - Ensure sufficient contrast for text visibility
   - Consider performance impact on mobile devices

2. Performance Considerations:
   - Minimize the number of gradient elements visible at once
   - Use CSS gradients instead of images where possible
   - Implement proper caching strategies
   - Optimize gradient animations

3. Accessibility:
   - Ensure sufficient contrast ratios with gradient backgrounds
   - Provide alternative styles for reduced motion preferences
   - Test with screen readers
   - Support keyboard navigation

## Browser Support

Gradient Able supports modern browsers with proper gradient rendering:
- Chrome 26+
- Firefox 16+
- Safari 6.1+
- Edge 12+
- Opera 12+

## Getting Help

For support with Gradient Able:
- Check the official documentation
- Visit CodedThemes support portal
- Explore the example pages
- Join the community forums

Keep your installation updated for the latest gradient effects and optimizations. CodedThemes regularly updates the template with new features and improvements.

.. include::  /_templates/components/footer-links.rst
