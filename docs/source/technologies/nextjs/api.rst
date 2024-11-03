API Sample
==========

This documentation provides a quick step-by-step guide to exposing a secure API on top of a `NextJS <./index.html>`__ project with an SQLite database.

We'll be creating a simple `Transaction` database that can be interacted with via an API deployed to Vercel.

.. include::  /_templates/components/banner-top.rst

Project Setup
-------------

You will need the following:

- **Node.js and npm**: You'll need Node.js installed on your machine. It comes with npm (Node Package Manager), which is used to manage dependencies. You can download it from the official `Next.js website <https://nextjs.org/>`__.
- **NextJS**: Follow `this guide <https://github.com/app-generator/core-nextjs>`__ to set up a simple NextJS project.

Step 1: Configure SQLite
------------------------

First, run this command to install SQLite:

.. code-block:: bash

    npm install sqlite sqlite3

Next, create an empty `database.db` file in a `db` folder. This file will contain your database schema.

.. code-block:: bash

    mkdir db
    touch db/database.db

Then define the database schema by creating a `dbSetup.js` file in the root directory of your NextJS project. This will set up the `Transaction` table.

Add the following code to `dbSetup.js`:

.. code-block:: javascript

    const sqlite3 = require('sqlite3').verbose();
    const db = new sqlite3.Database('./db/database.db');

    db.serialize(() => {
    db.run(`
        CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        amount REAL,
        date TEXT
        )
    `);
    });

    db.close();

Finally, run this to create your database and `Transaction` table:

.. code-block:: bash

    node dbSetup.js

Step 2: Create an API with Next.js API Routes
---------------------------------------------

Now to create the API, start by creating a new `pages` folder at the root of your project.

In the `pages` folder, create an `api/transactions` folder and create a file named `index.js` for handling requests.

Add this to your `index.js` file:

.. code-block:: javascript

    import sqlite3 from 'sqlite3';
    import { open } from 'sqlite';

    async function openDb() {
        return open({
            filename: './db/database.db',
            driver: sqlite3.Database
        });
    }

    export default async function handler(req, res) {
        const db = await openDb();
        const { method } = req;

        if (method === 'POST') {
            // Code to create a transaction
            const { amount, description } = req.body;
            await db.run(
            'INSERT INTO transactions (amount, description) VALUES (?, ?)',
            [amount, description]
            );
            res.status(201).json({ message: 'Transaction created successfully' });
        } else if (method === 'GET') {
            // Code to get all transactions
            const transactions = await db.all('SELECT * FROM transactions');
            res.status(200).json(transactions);
        } else {
            res.status(405).end(`Method ${method} Not Allowed`);
        }
    }

Feel free to add additional API methods routes for updating and deleting transactions.

Step 3: Secure the API
----------------------

Next, secure the API. To secure the API we will do the following:

- Add CORS (Cross-Origin Resource Sharing) to allow cross-origin requests.
- Add authentication via a simple access token.

1. **Add CORS**

To add CORS to your API, install the `cors` npm package:

.. code-block:: bash

    npm install cors

Once installed, add this code to your `api/transactions/index.js` file:

.. code-block:: javascript

    import Cors from "cors";

    // Initializing the cors middleware
    const cors = Cors({
    methods: ["POST", "GET", "HEAD"],
    });

2. **Add Authentication Token**

To add an authentication token, first, install the `dotenv` npm package:

.. code-block:: bash

    npm install dotenv --save

At the root of your project, create a `.env` file and add your desired API key (token) to it:

.. code-block:: text

    API_KEY=[your_api_key]

3. Update API

Finally, update your API code to use authentication.

Update your `api/transactions/index.js` file to look like this:

.. code-block:: javascript

    import sqlite3 from "sqlite3";
    import { open } from "sqlite";
    import Cors from "cors";
    require("dotenv").config();

    const cors = Cors({
        methods: ["POST", "GET", "HEAD"],
    });

    // Helper function to run Middleware
    function runMiddleware(req, res, fn) {
        return new Promise((resolve, reject) => {
            fn(req, res, (result) => {
            if (result instanceof Error) {
                return reject(result);
            }
            return resolve(result);
            });
        });
    }

    // Authentication middleware
    function auth(req, res, next) {
        const authHeader = req.headers["authorization"];
        const token = authHeader && authHeader.split(" ")[1];

        if (!token) {
            res.status(401).json({ error: "Unauthorized: No token provided" });
            return next(new Error("No token provided"));
        }

        if (token === process.env.API_KEY) {
            return next();
        }

        res.status(403).json({ error: "Forbidden: Invalid token" });
        return next(new Error("Invalid token"));
    }

    let db = null;

    // Access database
    async function openDb() {
        if (!db) {
            db = await open({
            filename: "./db/database.db",
            driver: sqlite3.Database,
            });
        }
        return db;
    }

    export default async function handler(req, res) {
        try {
            // Run Middleware
            await runMiddleware(req, res, cors);
            await runMiddleware(req, res, auth);

            const db = await openDb();

            if (req.method === "POST") {
                const { amount, description } = req.body;
                if (!amount || !description) {
                    return res.status(400).json({ error: "Invalid values provided" });
                }

                await db.run(
                    "INSERT INTO transactions (amount, description) VALUES (?, ?)",
                    [amount, description]
                );
                return res
                    .status(201)
                    .json({ message: "Transaction created successfully" });
            }

            if (req.method === "GET") {
                const transactions = await db.all("SELECT * FROM transactions");
                return res.status(200).json(transactions);
                }

                return res.status(405).json({ error: `Method ${req.method} Not Allowed` });
        } catch (error) {
            console.error("API Error:", error);
            if (!res.headersSent) {
                return res.status(500).json({ error: "Internal server error" });
            }
        }
    }

Step 4: Deploy on Vercel
------------------------

Next, we deploy the API to Vercel.

First, install the Vercel CLI:

.. code-block:: bash

    npm install -g vercel

Next, deploy the API:

.. code-block:: bash

    vercel

Follow the CLI prompts to deploy to `Vercel <https://vercel.com>`__. You'll need to sign into an active account to complete this step.

Step 5: Test the API with Postman
---------------------------------

Finally, test the API with Postman once the app has been deployed successfully.

Visit the `Postman web app <https://www.postman.com/>`__ and sign up/log in to your account.

- Send a `POST` request to `api/transactions` to create a transaction.
- Send a `GET` request to `api/transactions` to fetch all transactions.

Remember to include the API key as a header in your requests, like this:

.. code-block:: bash

    BEARER <API_KEY>

Also, include `amount` and `description` values in your `POST` requests to create new transactions.

.. include::  /_templates/components/footer-links.rst
