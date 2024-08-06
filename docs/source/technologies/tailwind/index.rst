Getting Started
=====================

This page aims to help developers getting started with `Tailwind CSS <https://tailwindcss.com/>`__, a utility-first **CSS framework** that allows you to build custom user interfaces rapidly. 

***************
Installation
***************

First, you'll need to have Node.js installed on your computer.

- Create a new project directory and navigate to it in your terminal.
- Initialize a new Node.js project:

.. code-block:: bash

    npm init -y

- Install Tailwind CSS and its peer dependencies

.. code-block:: bash

    npm install -D tailwindcss@latest postcss@latest autoprefixer@latest

- Generate your Tailwind config file:

.. code-block:: bash

    npx tailwindcss init -p

***************
Configuration
***************

Open the generated `tailwind.config.js` file and add the paths to all of your template files:

.. code-block:: javascript

    module.exports = {
    content: ["./**/*.{html,js}"],
    theme: {
        extend: {},
    },
        plugins: [],
    }

- Create your CSS file

Create a new file called `input.css` and add the Tailwind directives:

.. code-block:: css

    @tailwind base;
    @tailwind components;
    @tailwind utilities;

- Build your CSS

Add a build script to your `package.json` file:

.. code-block:: json

    "scripts": {
        "build": "tailwindcss -i ./input.css -o ./output.css --watch"
    }

Run the build script:

.. code-block:: bash

    npm run build

***************
HTML Code
***************

Create an `index.html` file and link your compiled CSS:

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tailwind CSS Tutorial</title>
        <link href="./output.css" rel="stylesheet">
    </head>
    <body>
        <h1 class="text-3xl font-bold underline">
            Hello, Tailwind CSS!
        </h1>
    </body>
    </html>

******************************
Understanding Tailwind Classes 
******************************

Now that you have Tailwind set up, let's explore some basic utility classes

   Typography

- `text-{size}`: Sets font size (e.g., `text-sm`, `text-lg`, `text-3xl`)
- `font-{weight}`: Sets font weight (e.g., `font-bold`, `font-light`)
- `text-{color}`: Sets text color (e.g., `text-blue-500`, `text-gray-700`)

   Spacing

- `m-{size}`: Sets margin (e.g., `m-4`, `mx-2`, `mt-6`)
- `p-{size}`: Sets padding (e.g., `p-4`, `px-2`, `pt-6`)   

   Flexbox

- `flex`: Creates a flex container
- `items-center`: Aligns items vertically
- `justify-between`: Spaces items horizontally

   Grid

- `grid``: Creates a grid container
- `grid-cols-{number}`: Sets number of columns (e.g., `grid-cols-3`)
- `gap-{size}`: Sets gap between grid items

   Responsive Design

Use prefixes like `sm:`, `md:`, `lg:` for responsive designs (e.g., `md:text-lg` applies `text-lg` on medium screens and larger)

Having this in mind, let's code a simple tailwind Component 

.. code-block:: html

    <div class="max-w-sm mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl m-4">
        <div class="md:flex">
            <div class="md:flex-shrink-0">
                <img class="h-48 w-full object-cover md:w-48" src="https://via.placeholder.com/150" alt="Example image">
            </div>
            <div class="p-8">
                <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">Case study</div>
                <a href="#" class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">Finding customers for your new business</a>
                <p class="mt-2 text-gray-500">Getting a new business off the ground is a lot of hard work. Here are five ideas you can use to find your first customers.</p>
            </div>
        </div>
    </div>

This example demonstrates how to combine Tailwind's utility classes to create a responsive card component.

- Customization

To customize Tailwind, you can modify the `tailwind.config.js` file. For example, to add a custom color:

.. code-block:: javascript 

    module.exports = {
        theme: {
            extend: {
                colors: {
                    'custom-blue': '#1da1f2',
                },
            },
        },
    }    

Now you can use `text-custom-blue` or `bg-custom-blue` in the HTML code.

******************************
Best Practices
******************************

- Use Tailwind's JIT (Just-In-Time) mode for faster development and smaller file sizes.
- Leverage Tailwind's `@apply` directive in your CSS to create reusable component classes.
- Use Tailwind's plugins to extend functionality when needed.

This tutorial should give you a solid foundation to start working with Tailwind CSS. Remember, the key to mastering Tailwind is practice and exploring its extensive utility classes. 
As you build more projects, you'll become more familiar with the classes and how to combine them effectively.

******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
