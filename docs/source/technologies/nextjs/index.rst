Getting Started
===============

This page explains how to get started with `Next.js <https://nextjs.org/>`__, a popular framework built on top of `React <../react/index.html>`__.

Before you can begin working with Next.js, ensure you have the following:

- **Node.js and npm**: You'll need Node.js installed on your machine. It comes with npm (Node Package Manager), which is used to manage dependencies. You can download it from the official `Next.js website <https://nextjs.org/>`__.
- **Create-Next-App CLI**: This allows you to set up a basic NextJS app quickly. You do not need to pre-install it.

.. include:: /_templates/components/banner-top.rst

Spin Up a Next.js App
---------------------

Run this code to create your first Next.js project:

.. code-block:: bash

    npx create-next-app@latest my-next-app
    cd my-next-app
    npm run dev

What’s Happening?
-----------------

- `npx create-next-app@latest my-next-app`: This command uses the Next.js CLI to create a new project called my-next-app. It sets up a basic folder structure and installs necessary dependencies.
- `cd my-next-app`: Navigate into your new project directory.
- `npm run dev`: This command starts the development server, making your app accessible, usually at http://localhost:3000.

Project Structure
-----------------

After running the commands above, you’ll notice several files and folders inside the `my-next-app` directory.

The key parts of your Next.js project are:

- `pages/`: This is where you define all the pages of your website. Each file inside this directory automatically becomes a route.
- `public/`: Static assets like images and fonts are stored here.
- `styles/`: A place to organize your global and modular CSS files.


Create a new Page
-----------------

Let’s create a simple page that displays a welcome message. Next.js uses pages to define the routes of your application.

For example, to create the homepage (route `/`), you need to create a file called `index.js` inside the `pages/` directory.

Then, and add your code to it, such as this simple homepage component:

.. code-block:: jsx

    export default function HomePage() {
        return (
            <div>
                <h1>Welcome to Next.js!</h1>
                <p>This is your first Next.js app.</p>
            </div>
        );
    }


Build Project and Deploying
---------------------------

Once you're ready to deploy your app, you can generate a production build and deploy it with the following code.

.. code-block:: bash

    npm run build
    npm start

What’s Happening?
-----------------

- `npm run build`: This compiles your application for production.
- `npm start`: After building, this command starts the production server.

.. include:: /_templates/components/footer-links.rst
