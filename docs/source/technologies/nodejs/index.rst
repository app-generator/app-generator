Getting Started
=====================

Getting Started with NodeJS. Here's a step-by-step guide to getting started with Node.js:

**Step 1: Prerequisites**

- Node.js: Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.
- npm: npm (Node Package Manager) is included with Node.js and is used to manage packages for your Node.js applications.

**Step 2: Install Node.js and npm**

Download and install Node.js from the **official website**. This installation will include npm. Follow the instructions specific to your operating system.

You can verify the installation by running the following commands in your terminal or command prompt:

.. code-block:: bash

    node -v
    npm -v

These commands should output the versions of Node.js and npm installed on your system.

**Step 3: Initialize a New Node.js Project**

Create a new directory for your project and navigate into it:

.. code-block:: bash

    mkdir my-node-app
    cd my-node-app

Initialize a new Node.js project by running:

.. code-block:: bash

    npm init -y

This command will create a `package.json`` file with default settings. The `package.json` file manages the dependencies and scripts for your Node.js project.

**Step 4: Install Express**

Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.

Install Express using npm:

.. code-block:: bash

    npm install express --save

**Step 5: Create a Basic Server**

Create a new file named `app.js` in your project directory and add the following code to set up a basic Express server:

.. code-block:: javascript

    const express = require('express');
    const app = express();
    const port = 3000;

    app.get('/', (req, res) => {
    res.send('Hello, World!');
    });

    app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
    });

This code creates a basic web server that listens on port 3000 and responds with `Hello, World!` when the root URL ("/") is accessed.

**Step 6: Run the Server**

Start your server by running the following command in your terminal:

.. code-block:: bash

    node app.js

You should see the message `Example app listening at http://localhost:3000` in your terminal.

**Step 7: Access Your Application**

Open your web browser and navigate to `http://localhost:3000`. You should see `Hello, World!` displayed on the page.

**Step 8: Add More Routes**

To add more routes, open the `app.js` file and add additional route handlers. For example:

.. code-block:: javascript

    app.get('/about', (req, res) => {
    res.send('About Page');
    });

    app.get('/contact', (req, res) => {
    res.send('Contact Page');
    });

Now, when you navigate to `http://localhost:3000/about` and `http://localhost:3000/contact`, you will see "About Page" and "Contact Page" respectively.

At this point, you should be familiar with the basic concepts regarding Node.JS 

******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
