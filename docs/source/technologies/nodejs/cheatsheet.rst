Cheatsheet
==========

A quick reference guide for common `Node.js <./index.html>`__ commands, patterns, and modules.

.. include:: /_templates/components/banner-top.rst

Basic Commands
--------------

**Check Node.js and npm Versions**

.. code-block:: bash

    node -v
    npm -v

**Initialize a New Project**

.. code-block:: bash

    npm init -y

**Install a Package**

.. code-block:: bash

    npm install <package-name>

Built-in Modules
----------------

**File System (fs)**

Reading a file:

.. code-block:: javascript

    const fs = require('fs');
    fs.readFile('file.txt', 'utf8', (err, data) => {
        if (err) throw err;
        console.log(data);
    });

Writing to a file:

.. code-block:: javascript

    fs.writeFile('file.txt', 'Hello, Node.js', (err) => {
        if (err) throw err;
        console.log('File written!');
    });

**HTTP Module**

Creating a basic server:

.. code-block:: javascript

    const http = require('http');

    const server = http.createServer((req, res) => {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello, World!\n');
    });

    server.listen(3000, '127.0.0.1', () => {
        console.log('Server running at http://127.0.0.1:3000/');
    });

Third-party Modules
-------------------

Node.js projects commonly use third-party modules to add functionality, often installed through npm.

Here’s how to work with third-party modules:

**Importing Modules**

Install a module with npm, then import it in your project using `require()`:

.. code-block:: bash

    npm install <module-name>

.. code-block:: javascript

    const dotenv = require('dotenv');
    dotenv.config();

**Exporting Custom Modules**

Define and export custom functions or objects from your modules using `module.exports`:

.. code-block:: javascript

    // In myModule.js
    const myFunction = () => {
        console.log('Hello from myModule!');
    };

    module.exports = myFunction;

Import it in another file:

.. code-block:: javascript

    const myFunction = require('./myModule');
    myFunction();

NPM Scripts
-----------

**Run a Script**

Add a script in `package.json`:

.. code-block:: json

    "scripts": {
        "start": "node app.js"
    }

Run the script:

.. code-block:: bash

    npm start

Environment Variables
---------------------

Environment variables are ideal for storing configuration and sensitive data in a NodeJS project.

Use `process.env` to access environment variables.

.. code-block:: javascript

    const port = process.env.PORT || 3000;
    console.log(`Server will run on port ${port}`);

To load variables from a `.env` file, install and use the `dotenv` package:

.. code-block:: bash

    npm install dotenv

Load the `.env` file at the top of the file where you need it.

.. code-block:: bash

    require('dotenv').config();

Error Handling
--------------

**Try-Catch Block**

.. code-block:: javascript

    try {
        // Code that may throw an error
    } catch (error) {
        console.error('Error:', error);
    }

**Promise Handling**

Using `.then()` and `.catch()`:

.. code-block:: javascript

    someAsyncFunction()
        .then(result => console.log(result))
        .catch(error => console.error(error));

Using `async/await`:

.. code-block:: javascript

    async function asyncCall() {
        try {
            const result = await someAsyncFunction();
            console.log(result);
        } catch (error) {
            console.error(error);
        }
    }

Best Practices
--------------

- Always use environment variables for configuration and sensitive data.
- Handle errors gracefully.
- Follow asynchronous programming patterns.
- Keep modules small and focused.

.. include:: /_templates/components/footer-links.rst