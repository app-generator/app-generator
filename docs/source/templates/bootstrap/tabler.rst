`Tabler <https://tabler.io/admin-template>`__
=============================================

**Tabler** is a premium and open-source dashboard template built on Bootstrap's framework. It stands out for its modern design, extensive UI components, and developer-friendly approach. 
The template emphasizes clean code, semantic markup, and high customization possibilities while maintaining excellent performance.

- 👉 `Tabler <https://tabler.io/admin-template>`__ - Product page 
- 👉 `Tabler <https://tabler.io/admin-template/preview>`__ - Live Demo

.. include::  /_templates/components/banner-top.rst

.. image:: https://github.com/user-attachments/assets/f1fa943d-7e6c-4346-9734-281a8cd2e093
   :alt: Tabler Dashboard - open-source dashboard template 

Project Structure
-----------------

.. code-block:: bash

    tabler/
        ├── dist/                  # Production files
        ├── src/
        │   ├── assets/
        │   │   ├── css/
        │   │   ├── fonts/
        │   │   ├── images/
        │   │   └── js/
        │   ├── pages/            # Page templates
        │   ├── partials/         # Reusable components
        │   └── scss/
        │       ├── ui/           # UI components
        │       ├── vendor/       # Third-party styles
        │       ├── _variables.scss
        │       └── tabler.scss
        ├── .browserslistrc
        ├── gulpfile.js
        ├── package.json
        └── README.md

Component System
----------------

Cards
*****

Tabler's card system extends Bootstrap with additional features:

.. code-block:: html

    <div class="card">
        <div class="card-status-top bg-primary"></div>
        <div class="card-header">
            <h3 class="card-title">Card title</h3>
            <div class="card-actions">
            <a href="#" class="btn btn-primary">
                Action
            </a>
            </div>
        </div>
        <div class="card-body">
            <div class="card-title">Card title</div>
            <p class="text-muted">Some quick example text</p>
        </div>
        <div class="card-footer">
            Card footer
        </div>
    </div>

Form Elements
*************

.. code-block:: html

    <form>
        <div class="form-floating mb-3">
            <input type="email" class="form-control" id="floating-input" placeholder="name@example.com">
            <label for="floating-input">Email address</label>
        </div>
        
        <div class="mb-3">
            <label class="form-label">Select with search</label>
            <select class="form-select" data-search="on">
            <option value="1">Option 1</option>
            <option value="2">Option 2</option>
            <option value="3">Option 3</option>
            </select>
        </div>
        
        <div class="mb-3">
            <label class="form-label">Toggle switches</label>
            <label class="form-check form-switch">
            <input class="form-check-input" type="checkbox">
            <span class="form-check-label">Toggle switch element</span>
            </label>
        </div>
    </form>

Charts and Data Visualization
-----------------------------

Tabler integrates with **ApexCharts**:

.. code-block:: javascript

    // Line chart configuration
    const options = {
    chart: {
        type: 'line',
        height: 300,
        parentHeightOffset: 0,
        toolbar: {
        show: false,
        }
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'smooth',
        width: 2,
        lineCap: 'round',
    },
    series: [{
        name: 'Sales',
        data: [31, 74, 64, 42, 48, 82, 56]
    }],
    grid: {
        padding: {
        top: -20,
        right: 0,
        bottom: -4,
        left: -4
        },
        strokeDashArray: 4,
    },
    xaxis: {
        labels: {
        padding: 0,
        },
        tooltip: {
        enabled: false
        },
        type: 'datetime',
    },
    yaxis: {
        labels: {
        padding: 4
        },
    },
    colors: ['#206bc4'],
    legend: {
        show: false,
    },
    };

    new ApexCharts(document.querySelector('#chart'), options).render();    

Additional Resources
--------------------

- Documentation: https://preview.tabler.io/docs/
- GitHub Repository: https://github.com/tabler/tabler
- Demos: https://preview.tabler.io/
- Support: Through GitHub issues

Keep your Tabler installation updated for the latest features and security patches.

.. include::  /_templates/components/footer-links.rst
