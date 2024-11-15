:og:description: Edge Functions - Learn how it works in Next.js

Edge Functions
==============

.. title:: Edge Functions - Learn how it works in Next.js   
.. meta::
    :description: Learn how Edge Functions works in Next.js - Complete kickOff and practical aspects
    :keywords: edge functions, next.js edge functions, edge functions tutorial, edge functions kickoff 

This documentation provides a quick, step-by-step guide on how to use **Edge Functions** with `NextJS <./index.html>`__. 
Edge functions are specialized serverless functions that execute at the "edge," bringing your code closer to end users.

.. include::  /_templates/components/banner-top.rst

By distributing code across servers worldwide, Edge functions serve requests from the nearest server, reducing latency and improving load times for a faster user experience.
This guide will walk you through creating a simple "Hello, World!" Edge function and deploying it to Vercel.

Before we proceed with the tutorial, let's consider **the pros and cons of using Edge Functions**.

Pros
----

- **Reduced Latency**: Edge functions execute closer to the user, reducing the time it takes to process requests and improving load times.
- **Scalability**: They can handle large volumes of requests without needing centralized servers, automatically scaling based on user location.
- **Enhanced Performance**: By distributing load across multiple regions, Edge functions alleviate bottlenecks at a single origin, offering more consistent performance across different geographies.
- **Improved Security**: Edge functions enable real-time security updates at the edge level, reducing the risk of vulnerabilities.

Cons
----

- **Limited Execution Time**: Edge functions are designed for lightweight tasks and may not be suitable for long-running processes due to time constraints.
- **Environment Limitations**: Some libraries may not be compatible with Edge runtimes, so testing and compatibility checks are crucial.
- **Cold Start Times**: Although minimized, there may still be occasional "cold starts" (initial setup delays) in certain Edge environments.

When to Use Edge Functions
--------------------------

Edge functions are ideal for situations where speed, scalability, and global distribution are priorities. Consider using Edge functions for:

- **Personalization and A/B Testing**: Serve personalized content (e.g., language or region-based) directly from the edge, adapting responses without central server requests.
- **Real-Time Analytics and Monitoring**: Collect or update user behavior data in real time, allowing for immediate insights with minimal latency.
- **Data Fetching and API Proxies**: Fetching remote API data closer to users, reducing response times—or use as secure API gateways with pre-validation.

Project Setup
-------------

Before we begin, you'll need the following:

- **Node.js and npm**: Ensure Node.js is installed on your machine. It comes with npm (Node Package Manager), used to manage dependencies. You can download it from the official `Node.js website <https://nodejs.org/>`__.
- **Next.js Project**: Set up a simple Next.js project by following the instructions in this `starter guide <https://github.com/app-generator/docs-nextjs-edge-functions>`__.

How to Create and Deploy an Edge Function
-----------------------------------------

After setting up a NextJS project using the starter guide, follow these steps to create and deploy your first Edhge Function.

We will create a simple Edge function that responds with "Hello from the Edge!".

Step 1: Create a Basic Edge Function
------------------------------------

At the root of your NextJS project, create a new `hello.js` file with the following directory: `api/edge/hello.js`.

Add the following code to hello.js:

.. code-block:: javascript

  export const config = {
    runtime: 'edge',
  };

  export default async function handler(req) {
    return new Response(JSON.stringify({ message: "Hello from the Edge!" }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  }

This code exports a handler function that responds with a simple JSON message. The config object specifies that this function should run in the Edge runtime, enabling it to execute closer to users for faster responses.

Step 2: Test Your Edge Function Locally
---------------------------------------

You can test Edge functions locally before deploying by running your NextJS project and making a request to the desired endpoint. To run your Next.js app locally:

.. code-block:: bash

  npm run dev

Open your browser and go to http://localhost:3000/api/edge/hello (assuming your project runs on `localhost:3000`). You should see the "Hello, World!" response message.

If you see the message, then everything is working as expected and the Edge function is ready to be deployed.

Step 3: Deploy to Vercel
------------------------

Next.js Edge functions are best deployed on Vercel, which optimizes the runtime environment for Edge functions.

Install the Vercel CLI if you haven't already:

.. code-block:: bash

  npm install -g vercel

Login to Vercel:

.. code-block:: bash

  vercel login

Deploy the project:

.. code-block:: bash

  vercel

Follow the prompts from the Vercel CLI to complete the deployment. Once deployed, Vercel will provide a URL where you can access your app.

Note that you will need an active Vercel account to complete these steps.

Step 4: Test the Edge Function
------------------------------

After deployment, simply navigate to the deployed URL (via your browser or a tool like Postman) and add `/api/edge/hello` to the end of the provided URL to access your Edge function. You should see the JSON response just as you did locally.

You can also customize your Edge function to add additional functionality, such as the ability to different HTTP request methods.

For example, modify `hello.js` to handle `GET` and `POST` requests:

.. code-block:: javascript

  export const config = {
    runtime: 'edge',
  };

  export default async function handler(req) {
    if (req.method === 'GET') {
      return new Response(JSON.stringify({ message: "Hello, GET request!" }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    } else if (req.method === 'POST') {
      return new Response(JSON.stringify({ message: "Hello, POST request!" }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    }
    return new Response("Method Not Allowed", { status: 405 });
  }

This change allows your Edge function to respond differently based on the HTTP method. Writing an Edge Function is mostly the same as writing regular API request handlers.

Deploy your changes to Vercel as described above to test the new behavior.

Conclusion
----------

You've now created and deployed a basic Edge function with Next.js. With this foundation, you can explore more complex functionalities, such as authentication, custom headers, and data fetching.

.. include:: /_templates/components/footer-links.rst
