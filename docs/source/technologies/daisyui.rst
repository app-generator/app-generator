:og:description: DaisyUI/Tailwind - Resources for students and developers: components and starters | App-Generator.dev

DaisyUI
========

.. title:: DaisyUI/Tailwind - Resources for students and developers: components and starters | App-Generator.dev
.. meta::
    :description: Unified index for DaisyUI/Tailwind resources: tutorials, scripts, best practices and dev tips

DaisyUI is a plugin for Tailwind CSS that provides pre-made component classes while maintaining Tailwind's utility-first approach. 
Instead of writing multiple utility classes for common components, DaisyUI provides semantic class names that bundle these utilities together.

.. include::  /_templates/components/banner-top.rst

Key Points of DaisyUI
---------------------

Semantic Component Classes
**************************

DaisyUI introduces semantic class names that make your HTML much cleaner and more readable. 
Instead of writing multiple Tailwind utility classes, you can use simple component classes like btn or card. 
For example, rather than writing **bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded**, you can simply write **btn btn-primary**.

Theme System
************

One of DaisyUI's strongest features is its powerful theming system. It comes with 20+ pre-built themes, and you can easily switch between them using the data-theme attribute. 
You can also create custom themes by modifying CSS variables. The theme system handles both light and dark modes seamlessly.

Modifier-Based Styling
**********************

DaisyUI follows a consistent modifier pattern that makes styling components intuitive. You can add modifiers like **btn-primary**, **btn-outline**, or **btn-lg** to change the appearance and size of components. 
This approach maintains consistency across your project while keeping the code clean.

Zero JavaScript Dependencies
****************************

Unlike many other component libraries, DaisyUI is purely CSS-based. This means you get all the styling and component variations without adding any JavaScript to your bundle. 
This results in better performance and simpler maintenance.

Customization Options
*********************

While DaisyUI provides pre-built components, it's designed to work seamlessly with Tailwind's utility classes. 
You can easily customize any component by adding Tailwind classes alongside DaisyUI classes. 
This gives you the best of both worlds - quick development with pre-built components and unlimited customization options.

Responsive Components
*********************

DaisyUI components are responsive by default, but they also work perfectly with Tailwind's responsive prefixes. 
You can create components that change their appearance across different screen sizes by combining DaisyUI classes with Tailwind's responsive modifiers.

Color System
************

DaisyUI introduces a semantic color system that makes it easier to maintain consistent colors across your application. 
Instead of using specific color values, you can use semantic names like **primary**, **secondary**, **accent**, and **neutral**. This makes it easier to maintain and update your color scheme.

Form Components
***************

DaisyUI provides a comprehensive set of form components that are both functional and aesthetically pleasing. 
From inputs and selects to checkboxes and radio buttons, all form elements follow the same design language and can be customized using consistent modifiers.

Layout Components
*****************

The library includes several layout components like navbar, drawer, modal, and hero that help you quickly build common webpage layouts. 
These components are designed to work together and can be nested to create complex layouts while maintaining clean HTML structure.

Component States
****************

DaisyUI handles component states elegantly. Whether it's hover states, focus states, or disabled states, each component comes with well-designed state variations. 
For example, buttons automatically show hover effects, loading states, and disabled appearances without requiring additional JavaScript.

Practical Example
-----------------

Here's a practical example that demonstrates several of these key points:

.. code-block:: html 

    <div class="card w-96 bg-base-100 shadow-xl" data-theme="light">
        <figure>
            <img src="image.jpg" alt="Card Image"/>
        </figure>
        <div class="card-body">
            <h2 class="card-title">Card Title</h2>
            <p>This card demonstrates semantic classes, theming, and component structure.</p>
            <div class="card-actions justify-end">
                <button class="btn btn-primary">Default</button>
                <button class="btn btn-primary btn-outline">Outline</button>
                <button class="btn btn-primary loading">Loading</button>
            </div>
        </div>
    </div>    

This example shows how DaisyUI's semantic classes, theming system, and component states work together to create a clean, maintainable, and visually appealing interface. 

Resources
---------

.. toctree::
   :maxdepth: 1
   
   daisyui/index
   daisyui/daisyui-vs-flowbite
