:og:description: Getting Started with DaisyUI - The basics of using Tailwind and DaisyUI

Getting Started
===============

.. title:: Getting Started with daisyUI - The basics of using Tailwind and DaisyUI   
.. meta::
    :description: Learn how to integrate DaisyUI and Tailwind in different frameworks and later customize and update

DaisyUI is a plugin for Tailwind CSS that provides pre-made component classes while maintaining Tailwind's utility-first approach. 
Instead of writing multiple utility classes for common components, DaisyUI provides semantic class names that bundle these utilities together.

.. include::  /_templates/components/banner-top.rst

For example, instead of writing:

.. code-block:: html

    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
    Button
    </button>    

With DaisyUI, you can simply write:

.. code-block:: html

    <button class="btn btn-primary">
    Button
    </button>

Key features of DaisyUI
-----------------------

- Component classes that follow consistent naming conventions
- Customizable themes with built-in dark mode support
- Semantic color names (primary, secondary, accent, etc.)
- Responsive components that maintain Tailwind's flexibility
- No JavaScript dependencies - it's purely CSS-based

Getting Started with DaisyUI
----------------------------

First, install Tailwind CSS and DaisyUI in your project:

.. code-block:: bash 

    # Install Tailwind CSS
    npm install -D tailwindcss

    # Install DaisyUI
    npm install -D daisyui

Then, add DaisyUI to your **tailwind.config.js**:

.. code-block:: javascript 

    module.exports = {
        plugins: [require("daisyui")],
    }


Basic Components Examples
-------------------------

Buttons
*******

.. code-block:: html 

    <!-- Basic buttons -->
    <button class="btn">Button</button>
    <button class="btn btn-primary">Primary</button>
    <button class="btn btn-secondary">Secondary</button>
    <button class="btn btn-accent">Accent</button>

    <!-- Button sizes -->
    <button class="btn btn-lg">Large</button>
    <button class="btn">Normal</button>
    <button class="btn btn-sm">Small</button>
    <button class="btn btn-xs">Tiny</button>

    <!-- Button states -->
    <button class="btn btn-outline">Outline</button>
    <button class="btn btn-disabled">Disabled</button>
    <button class="btn loading">Loading</button>    

Cards
*****

.. code-block:: html 

    <div class="card w-96 bg-base-100 shadow-xl">
        <figure>
            <img src="image.jpg" alt="Card Image"/>
        </figure>
        <div class="card-body">
            <h2 class="card-title">Card Title</h2>
            <p>This is a basic card with image and text.</p>
            <div class="card-actions justify-end">
                <button class="btn btn-primary">Action</button>
            </div>
        </div>
    </div>

Form Elements
*************

.. code-block:: html 

    <!-- Input fields -->
    <input type="text" placeholder="Regular input" class="input input-bordered w-full max-w-xs" />
    <input type="text" placeholder="Primary input" class="input input-primary w-full max-w-xs" />

    <!-- Select -->
    <select class="select select-bordered w-full max-w-xs">
        <option disabled selected>Pick one</option>
        <option>Option 1</option>
        <option>Option 2</option>
    </select>

    <!-- Checkbox -->
    <div class="form-control">
        <label class="label cursor-pointer">
            <span class="label-text">Remember me</span>
            <input type="checkbox" class="checkbox checkbox-primary" />
        </label>
    </div>    


Theming
*******

DaisyUI comes with several built-in themes. You can configure them in your **tailwind.config.js**:

.. code-block:: javascript 

    module.exports = {
        plugins: [require("daisyui")],
        daisyui: {
            themes: ["light", "dark", "cupcake", "bumblebee", "emerald", "corporate"],
        },
    }

To apply a theme, add the data-theme attribute to your HTML:

.. code-block:: html 

    <html data-theme="light">
        <!-- Your content -->
    </html>    

Best Practices
**************

- **Component Modifiers**: Use consistent modifiers like btn-primary, btn-secondary for semantic meaning.
- **Responsive Design**: DaisyUI components are responsive by default, but you can use Tailwind's responsive prefixes:

.. code-block:: html 

    <button class="btn btn-sm md:btn-md lg:btn-lg">Responsive Button</button>

- **Theme Colors**: Use semantic color names instead of specific colors:    

- primary
- secondary
- accent
- info

- **Layout Components**: Combine DaisyUI components with Tailwind's layout utilities:

.. code-block:: html 

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div class="card"><!-- Card content --></div>
        <div class="card"><!-- Card content --></div>
        <div class="card"><!-- Card content --></div>
    </div>    

.. include::  /_templates/components/footer-links.rst
