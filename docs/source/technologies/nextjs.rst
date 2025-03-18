:og:description: Next.js - Resources for students and developers | App-Generator.dev 

Next.js
=======

.. title:: Next.js: Resources for students and developers | App-Generator.dev
.. meta::
    :description: Unified index for Next.js resources: tutorials, starters, best practices and dev tips


Next.js is a React framework for building full-stack web applications.
It extends React's capabilities with server-side rendering, static site generation, and a powerful routing system, while maintaining a developer-friendly experience.

.. include::  /_templates/components/banner-top.rst

Key Features
------------

- **Hybrid Rendering**: Server-side rendering (SSR), static site generation (SSG), and client-side rendering
- **File-based Routing**: Intuitive page-based routing system
- **API Routes**: Built-in API endpoint creation within the same codebase
- **Image Optimization**: Automatic image optimization with the Image component
- **Zero Config**: Works out of the box with sensible defaults
- **Fast Refresh**: Instant feedback during development
- **TypeScript Support**: Built-in TypeScript integration
- **App Router**: Modern React features with Server Components, Streaming, and more

Quick Start
-----------

.. code-block:: jsx

    // pages/index.js
    export default function Home() {
        return (
            <div>
            <h1>Welcome to Next.js!</h1>
            <p>Get started by editing this page</p>
            </div>
        )
    }

    // pages/about.js
    export default function About() {
        return <h1>About Page</h1>
    }

Install and run:

.. code-block:: bash

    npx create-next-app@latest my-next-app
    cd my-next-app
    npm run dev

Next.js combines the best of static and server rendering, with innovative features like Incremental Static Regeneration and Server Components, 
making it ideal for creating modern web applications ranging from simple marketing pages to complex, data-heavy applications.

.. include::  /_templates/components/footer-links.rst

Resources
---------

.. toctree::
   :maxdepth: 1
   
   nextjs/index
   nextjs/cheatsheet
   nextjs/app-router
   nextjs/middleware
   nextjs/api
   nextjs/drizzle-orm
   nextjs/edge-functions
   nextjs/react-hooks-form
   nextjs/integrate-recharts
   nextjs/shadcn-components
   nextjs/deploy
   nextjs/versions

