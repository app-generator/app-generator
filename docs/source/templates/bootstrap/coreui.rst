`CoreUI <https://coreui.io/bootstrap/?AFFILIATE=128200>`__
==========================================================

.. title:: CoreUI -  Modern, dark-themed admin template created by CoreUI Agency
.. meta::
    :description: Open-source material design dashboard and control panel styled with Bootstrap 5

**CoreUI** is a robust, enterprise-grade admin template built on top of Bootstrap. 
It distinguishes itself through its modular architecture, comprehensive component library, and strong focus on real-world application needs. 

- 👉 `CoreUI <https://coreui.io/bootstrap/?AFFILIATE=128200>`__ - Product page 
- 👉 `CoreUI <https://coreui.io/demos/bootstrap/5.0/free/?AFFILIATE=128200>`__ - Live Demo

The template is designed for building responsive, cross-browser web applications while maintaining high performance and accessibility standards.

.. include::  /_templates/components/banner-top.rst

.. image:: https://user-images.githubusercontent.com/51070104/171336361-b125ca1d-8936-4f4a-b662-9e45ee25f404.png
   :alt: CoreUI - open-source dashboard template provided by CoreUI Agency

Project Structure
-----------------

CoreUI follows a well-organized directory structure:

.. code-block:: bash

    coreui/
        ├── dist/                # Compiled production files
        ├── src/
        │   ├── assets/
        │   │   ├── brand/      # Logo and brand assets
        │   │   ├── icons/      # CoreUI Icons
        │   │   └── img/        # Images
        │   ├── js/
        │   │   ├── core/       # Core functionality
        │   │   ├── widgets/    # Widget components
        │   │   └── main.js     # Main JavaScript file
        │   ├── pug/            # Pug templates (optional)
        │   ├── scss/
        │   │   ├── style.scss  # Main style file
        │   │   ├── _custom.scss
        │   │   ├── _variables.scss
        │   │   └── vendors/    # Third-party styles
        │   └── views/          # HTML templates
        ├── build/              # Build scripts
        └── node_modules/       # Dependencies

Core Layout Structure
---------------------

Here's the fundamental layout structure for CoreUI pages:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CoreUI</title>
        <!-- CoreUI CSS -->
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body class="c-app">
        <!-- Sidebar -->
        <div class="c-sidebar c-sidebar-dark c-sidebar-fixed c-sidebar-lg-show" id="sidebar">
            <div class="c-sidebar-brand">
                <img class="c-sidebar-brand-full" src="assets/brand/coreui-base.svg" height="46">
                <img class="c-sidebar-brand-minimized" src="assets/brand/coreui-signet.svg" height="46">
            </div>
            
            <ul class="c-sidebar-nav">
                <!-- Sidebar navigation items -->
            </ul>
            
            <button class="c-sidebar-minimizer c-class-toggler" type="button"></button>
        </div>

        <!-- Main content wrapper -->
        <div class="c-wrapper">
            <!-- Header -->
            <header class="c-header c-header-light c-header-fixed">
                <button class="c-header-toggler" type="button">
                    <span class="c-header-toggler-icon"></span>
                </button>
                
                <ul class="c-header-nav ml-auto">
                    <!-- Header navigation items -->
                </ul>
            </header>

            <!-- Main content -->
            <div class="c-body">
                <main class="c-main">
                    <div class="container-fluid">
                        <!-- Page content -->
                    </div>
                </main>
            </div>

            <!-- Footer -->
            <footer class="c-footer">
                <div>CoreUI © 2024</div>
                <div class="ml-auto">Powered by CoreUI</div>
            </footer>
        </div>
    </body>
    </html>


Component System
----------------

Card Components
***************

CoreUI extends Bootstrap's card component with additional features:

.. code-block:: html

    <div class="card">
        <div class="card-header">
            Featured
            <div class="card-header-actions">
                <a class="card-header-action btn-setting" href="#">
                    <i class="cil-settings"></i>
                </a>
                <a class="card-header-action btn-minimize" href="#">
                    <i class="cil-arrow-circle-top"></i>
                </a>
                <a class="card-header-action btn-close" href="#">
                    <i class="cil-x"></i>
                </a>
            </div>
        </div>
        <div class="card-body">
            Content
        </div>
    </div>


Sidebar Navigation
******************

CoreUI provides extensive sidebar customization:

.. code-block:: html

    <ul class="c-sidebar-nav">
        <li class="c-sidebar-nav-item">
            <a class="c-sidebar-nav-link" href="#">
                <i class="c-sidebar-nav-icon cil-speedometer"></i> Dashboard
                <span class="badge badge-info">NEW</span>
            </a>
        </li>
        
        <li class="c-sidebar-nav-dropdown">
            <a class="c-sidebar-nav-dropdown-toggle" href="#">
                <i class="c-sidebar-nav-icon cil-puzzle"></i> Components
            </a>
            <ul class="c-sidebar-nav-dropdown-items">
                <li class="c-sidebar-nav-item">
                    <a class="c-sidebar-nav-link" href="#">
                        <span class="c-sidebar-nav-icon"></span> Buttons
                    </a>
                </li>
            </ul>
        </li>
    </ul>


Customization
-------------

SCSS Variables
**************

CoreUI provides extensive customization through SCSS variables:

.. code-block:: scss

    // Core variables
    $sidebar-width: 256px;
    $sidebar-minimized-width: 56px;
    $sidebar-brand-height: 56px;

    // Theme colors
    $primary: #321fdb;
    $secondary: #ced2d8;
    $success: #2eb85c;
    $info: #39f;
    $warning: #f9b115;
    $danger: #e55353;

    // Layout options
    $enable-sidebar-nav-rounded: true;
    $enable-footer-fixed: true;
    $enable-header-fixed: true;
    $enable-sidebar-fixed: true;

    // Typography
    $font-family-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue";
    $font-size-base: 0.875rem;

JavaScript Configuration
************************

CoreUI's behavior can be customized through JavaScript:

.. code-block:: javascript

    // Initialize CoreUI
    window.addEventListener('load', function() {
        coreui.Sidebar._jQueryInterface.call($('#sidebar'), 'show');
        
        // Custom sidebar configuration
        var sidebar = new coreui.Sidebar('#sidebar', {
            minimize: true,
            unfoldable: false,
            breakpoints: {
                xs: 'c-sidebar-show',
                sm: 'c-sidebar-sm-show',
                md: 'c-sidebar-md-show',
                lg: 'c-sidebar-lg-show',
                xl: 'c-sidebar-xl-show'
            }
        });
    });

// Configure tooltip options globally
coreui.Utils.setTooltipDistance(10);

Advanced Features
-----------------

State Management
****************

CoreUI implements a robust state management system:

.. code-block:: javascript

    // State management for sidebar
    class SidebarState {
        constructor() {
            this.minimized = false;
            this.unfoldable = false;
            this.mobile = window.innerWidth < 992;
        }
        
        toggle() {
            this.minimized = !this.minimized;
            document.body.classList.toggle('c-sidebar-minimized');
        }
        
        // Persist state
        save() {
            localStorage.setItem('sidebar-state', JSON.stringify({
                minimized: this.minimized,
                unfoldable: this.unfoldable
            }));
        }
    }

    const sidebarState = new SidebarState();


Custom Events
*************

CoreUI provides custom events for component interactions:

.. code-block:: javascript

    // Listen for sidebar events
    const sidebar = document.querySelector('#sidebar');

    sidebar.addEventListener('classtoggle.coreui.sidebar', function(event) {
        console.log('Sidebar class toggled:', event.detail);
    });

    sidebar.addEventListener('minimize.coreui.sidebar', function(event) {
        console.log('Sidebar minimized:', event.detail);
    });

Performance Optimization
------------------------

Lazy Loading
************

Implement lazy loading for better performance:

.. code-block:: javascript

    // Lazy load components
    document.addEventListener('DOMContentLoaded', function() {
        const lazyComponents = document.querySelectorAll('[data-load]');
        
        const loadComponent = (element) => {
            const componentUrl = element.dataset.load;
            fetch(componentUrl)
                .then(response => response.text())
                .then(html => {
                    element.innerHTML = html;
                    element.removeAttribute('data-load');
                });
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    loadComponent(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        });
        
        lazyComponents.forEach(component => observer.observe(component));
    });

Asset Optimization
******************

.. code-block:: javascript

    // Configure webpack for optimal asset loading
    module.exports = {
        optimization: {
            splitChunks: {
                chunks: 'all',
                cacheGroups: {
                    vendors: {
                        test: /[\\/]node_modules[\\/]/,
                        priority: -10
                    },
                    default: {
                        minChunks: 2,
                        priority: -20,
                        reuseExistingChunk: true
                    }
                }
            }
        }
    };

## Responsive Design

CoreUI implements a mobile-first approach:

.. code-block:: scss

    // Responsive breakpoints
    $grid-breakpoints: (
        xs: 0,
        sm: 576px,
        md: 768px,
        lg: 992px,
        xl: 1200px,
        xxl: 1400px
    );

    // Responsive utilities
    @include media-breakpoint-down(md) {
        .c-sidebar {
            position: fixed;
            z-index: $zindex-fixed + 1;
            transform: translateX(-100%);
            
            &.c-sidebar-show {
                transform: translateX(0);
            }
        }
    }

Best Practices
--------------

1. Component Organization:
   - Keep components modular and reusable
   - Follow CoreUI's naming conventions
   - Maintain consistent component structure
   - Document component dependencies

2. Performance Guidelines:
   - Minimize HTTP requests
   - Optimize asset loading
   - Use proper caching strategies
   - Implement lazy loading where appropriate

3. Accessibility:
   - Maintain ARIA labels
   - Ensure keyboard navigation
   - Provide sufficient color contrast
   - Support screen readers

Browser Support
---------------

CoreUI supports all modern browsers:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Opera (latest)
- Internet Explorer 11 (with polyfills)

Development Workflow
--------------------

.. code-block:: bash

    # Install dependencies
    npm install

    # Start development server
    npm run serve

    # Build for production
    npm run build

    # Run tests
    npm test

Resources and Support
---------------------

- Official Documentation: [CoreUI Documentation](https://coreui.io/docs)
- GitHub Repository: [CoreUI GitHub](https://github.com/coreui/coreui)
- Support Forums: [CoreUI Community](https://community.coreui.io/)
- Updates: Regular releases through npm

Remember to keep your CoreUI installation updated for the latest features and security patches.

.. include::  /_templates/components/footer-links.rst
