`Pixel UI Kit </product/pixel-bootstrap/>`__
============================================

.. title:: Pixel UI Kit -  Open-source material-design UI Kit created by ThemesBerg
.. meta::
    :description: Open-source UI Kit with pixel patterns built on top of Bootstrap 5

`Pixel UI Kit </product/pixel-bootstrap/>`__ is a premium Bootstrap-based UI toolkit from `Themesberg </agency/themesberg/>`__ that combines modern design aesthetics with extensive functionality. 
The kit is known for its pixel-perfect design system, comprehensive component library, and attention to detail in both visual and technical implementation.

    👉 `Pixel Kit Starters </product/pixel-bootstrap/>`__ - Bundle provided by `App Generator </>`__ platorm

The template features an extensive array of meticulously crafted elements, from navigation systems and form controls to complex interactive components, all working harmoniously to deliver cohesive user experiences
Its modular structure enables developers and designers to efficiently assemble distinctive interfaces without sacrificing visual consistency.

.. image:: https://user-images.githubusercontent.com/51070104/168753915-d61b2f97-57b2-4d14-a774-d217d120ff62.png
   :alt: Pixel UI Kit - Open-source UI Kit from Themesberg 

Project Architecture
--------------------

.. code-block:: bash

    pixel-ui-kit/
        ├── dist/                    # Compiled files
        │   ├── css/
        │   ├── js/
        │   ├── vendor/
        │   └── img/
        ├── src/
        │   ├── assets/
        │   │   ├── img/
        │   │   │   ├── brand/
        │   │   │   ├── icons/
        │   │   │   └── illustrations/
        │   │   ├── js/
        │   │   │   ├── core/
        │   │   │   ├── components/
        │   │   │   └── pixel.js
        │   │   └── scss/
        │   │       ├── components/
        │   │       ├── mixins/
        │   │       ├── custom/
        │   │       └── pixel.scss
        │   ├── partials/
        │   └── pages/
        ├── docs/
        └── gulpfile.js

Component System
----------------

Advanced Cards
**************

Pixel UI Kit provides sophisticated card components:

.. code-block:: html

    <div class="card border-light shadow-soft">
        <div class="card-header p-3">
            <div class="row align-items-center">
                <div class="col">
                    <h2 class="h5 mb-0">Card Title</h2>
                </div>
                <div class="col">
                    <div class="d-flex align-items-center justify-content-end">
                        <!-- Card actions -->
                    </div>
                </div>
            </div>
        </div>
        <div class="card-body">
            <div class="d-flex align-items-center">
                <!-- Card content -->
            </div>
        </div>
    </div>    

Form Components
***************

Enhanced form elements with Pixel styling:

.. code-block:: html

    <form>
        <!-- Input with icon -->
        <div class="form-group">
            <div class="input-group mb-4">
                <span class="input-group-text">
                    <span class="fas fa-search"></span>
                </span>
                <input class="form-control" placeholder="Search" type="text">
            </div>
        </div>
        
        <!-- Custom select -->
        <div class="form-group">
            <select class="custom-select" id="exampleCustomSelect">
                <option selected>Open this select menu</option>
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>
        </div>
        
        <!-- Custom range -->
        <div class="form-group">
            <label class="form-control-label">Custom Range</label>
            <div class="input-slider-container">
                <div id="input-slider" class="input-slider"></div>
            </div>
        </div>
    </form>    

Charts and Data Visualization
-----------------------------

.. code-block:: javascript

    // Line chart configuration
    const lineChartConfig = {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June'],
            datasets: [{
                label: 'Performance',
                data: [65, 59, 80, 81, 56, 55],
                borderColor: pixelKit.colors.primary,
                tension: 0.4,
                pointRadius: 0,
                borderWidth: 4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    grid: {
                        display: false
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    };   

Resources
---------

- Documentation: Themesberg docs
- Support: Through Themesberg support system
- Updates: Regular through npm
- Community: Themesberg forums

Keep your Pixel UI Kit updated for the latest features and security patches.     

.. include::  /_templates/components/footer-links.rst
