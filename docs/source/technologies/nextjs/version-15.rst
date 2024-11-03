Version 15
==========

This documentation provides an easy guide on how to upgrade to the newly-released `Next.js <./index.html>`__ version 15.

It also covers how to upgrade projects built with older Next.js versions.

.. include::  /_templates/components/banner-top.rst

Pre-requisites
--------------

To follow along, you will need:

- **Node.js and npm**: You'll need Node.js installed on your machine. It comes with npm (Node Package Manager), which is used to manage dependencies. You can download it from the official `Next.js website <https://nextjs.org/>`__.

NextJS 15 Key New Features
--------------------------

Here's a quick rundown of the key new features of NextJS 15:

Codemod CLI for Easy Upgrades
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next.js 15 introduces an improved `@next/codemod` CLI for smoother upgrades. This CLI automates updates for breaking changes and simplifies dependency management.

Refer to the **How to Upgrade to NextJS 15** section below for instructions on how to use it.

Async Request APIs
^^^^^^^^^^^^^^^^^^^

A shift to asynchronous APIs enables optimized rendering and caching by allowing non-request-specific data to load in advance.

This change affects APIs like cookies, headers, and params, with a codemod provided to help automate updates.

Caching Overhaul
^^^^^^^^^^^^^^^^

GET route handlers and client router caches are now uncached by default. This change improves data freshness on page reloads and navigations, though users can still opt into caching if desired.

React 19 Support
^^^^^^^^^^^^^^^^

With React 19 on the horizon, Next.js 15 offers experimental support for the React Compiler, which reduces the need for manual optimizations like `useMemo` and `useCallback`.

Enhanced Forms
^^^^^^^^^^^^^^

The new `<Form>` component enriches HTML forms with features like `prefetching <https://nextjs.org/docs/app/building-your-application/routing/linking-and-navigating#2-prefetching>`__, `client-side navigation <https://nextjs.org/docs/app/building-your-application/routing/linking-and-navigating#5-soft-navigation>`__, and progressive enhancement for faster interactions.

Stable Turbopack
^^^^^^^^^^^^^^^^

Turbopack has now been made stable and offers significant speed boosts. It improves server startup by up to 76% and Fast Refresh by over 90%, which can enhance productivity during local development.

How to Upgrade to Next.js 15
----------------------------

Here's a simple guide on how to upgrade to the latest NextJS 15.

Starting a New Project
^^^^^^^^^^^^^^^^^^^^^^

To start a new Next.js project with Next.js 15, run the following command:

.. code-block:: bash

    npx create-next-app@latest <my-nextjs-app>

Replace `<my-nextjs-app>` with the name of your NextJS app.

Upgrade an Existing Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upgrading existing projects to NextJS is straightforward. The `@next/codemod` CLI provides automated code transformations to assist with the upgrade.

To upgrade using the codemod CLI, navigate to the root of your project and run:

.. code-block:: bash

    npx @next/codemod@canary upgrade latest

Then follow the prompts provided by the CLI.

This will upgrade your project to use NextJS 15 and React 19 (latest release candidate) and modify parts of your codebase as necessary.

Upgrading Manually
""""""""""""""""""

You can also upgrade manually without using the codemod CLI. To upgrade manually, run:

.. code-block:: bash

    npm install next@latest react@rc react-dom@rc

This will install the latest version of Next.js along with the release candidate versions of React and React DOM.

.. include::  /_templates/components/footer-links.rst
