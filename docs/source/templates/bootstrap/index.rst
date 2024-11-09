Getting Started
===============

Bootstrap is the world's most popular framework for building responsive, mobile-first websites and applications. 
It provides a comprehensive collection of pre-built components, utilities, and a powerful grid system that makes web development faster and more efficient.

.. include::  /_templates/components/banner-top.rst

Installation Methods
--------------------

1. CDN (Quickest Method)
************************

.. code-block:: html 

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bootstrap Project</title>
        
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <!-- Your content here -->
        
        <!-- Bootstrap Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>    

2. Package Manager (NPM)
************************

.. code-block:: bash 

    # Install Bootstrap
    npm install bootstrap

    # Install dependencies
    npm install @popperjs/core

3. Source Files Download

Download the compiled CSS and JS files from the official Bootstrap website and include them in your project:

.. code-block:: html 

    <link href="/css/bootstrap.min.css" rel="stylesheet">
    <script src="/js/bootstrap.bundle.min.js"></script>

Essential Concepts
------------------

1. Grid System
**************

.. code-block:: html 

    <div class="container">
        <div class="row">
            <!-- Equal width columns -->
            <div class="col">Column 1</div>
            <div class="col">Column 2</div>
            <div class="col">Column 3</div>
            
            <!-- Specific width columns -->
            <div class="col-12 col-md-6 col-lg-4">Responsive Column</div>
        </div>
    </div>    

2. Responsive Breakpoints
*************************

.. code-block:: scss 

    // Bootstrap breakpoints
    $grid-breakpoints: (
        xs: 0,
        sm: 576px,
        md: 768px,
        md: 992px,
        lg: 1200px,
        xl: 1400px
    );

    // Usage example
    <div class="col-12 col-md-6 col-lg-4">
        <!-- Full width on mobile, half on tablet, third on desktop -->
    </div>    

3. Container Types
******************

.. code-block:: html 

    <!-- Fixed-width container -->
    <div class="container">
        <!-- Content -->
    </div>

    <!-- Fluid container (full-width) -->
    <div class="container-fluid">
        <!-- Content -->
    </div>

    <!-- Responsive containers -->
    <div class="container-sm">
    <div class="container-md">
    <div class="container-lg">
    <div class="container-xl">    

Resources
---------

- Official Documentation: getbootstrap.com/docs
- GitHub Repository: github.com/twbs/bootstrap
- Bootstrap Icons: icons.getbootstrap.com
- Bootstrap Themes: themes.getbootstrap.com

Getting Help
------------

- Stack Overflow: Tag 'bootstrap'
- Bootstrap's GitHub Issues
- Bootstrap's Official Blog
- Bootstrap Community Forums

Remember to keep your Bootstrap installation updated for the latest features and security patches.

.. include::  /_templates/components/footer-links.rst
