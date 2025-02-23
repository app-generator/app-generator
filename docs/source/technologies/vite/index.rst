:og:description: Getting Started with Vite - The modern build tool used in frontend development

Getting Started
===============

.. title:: Getting Started with Vite - The modern build tool used in frontend development  
.. meta::
    :description: Vite takes a fundamentally different approach to development compared to Webpack. 

When it comes to modern web development, choosing the right build tool can significantly impact your development experience. Vite takes a fundamentally different approach to development compared to Webpack. 

Vite (French word for "quick") is a modern frontend build tool that offers a faster and leaner development experience compared to older bundlers like webpack.

.. include::  /_templates/components/banner-top.rst

Key Features
------------

- Lightning-fast server start
- Instant Hot Module Replacement (HMR)
- True on-demand compilation
- Out-of-the-box TypeScript support
- Built-in optimized build command

Getting Started
---------------

Creating a New Project
**********************

.. code-block:: bash

    # Using npm
    npm create vite@latest my-app

    # Using yarn
    yarn create vite my-app

    # Using pnpm
    pnpm create vite my-app     

When you run this command, Vite will prompt you to choose:

- A framework (React, Vue, Svelte, etc.)
- A variant (JavaScript or TypeScript)

Project Structure
*****************

.. code-block:: bash

    my-app/
    ├── public/              # Static assets
    ├── src/                # Source files
    │   ├── assets/         # Project assets
    │   ├── components/     # Components
    │   ├── App.jsx        # Root component
    │   └── main.jsx       # Entry point
    ├── index.html          # Entry HTML
    ├── package.json        # Dependencies and scripts
    └── vite.config.js      # Vite configuration    

Basic Configuration (vite.config.js)
------------------------------------

.. code-block:: javascript

    import { defineConfig } from 'vite'
    import react from '@vitejs/plugin-react'

    export default defineConfig({
        plugins: [react()],
        server: {
            port: 3000,
            open: true
        },
        build: {
            outDir: 'dist',
            minify: 'esbuild'
        }
    })    

Starting Servers
----------------

.. code-block:: bash 

    npm run dev   # development 
    npm run build # production

The production build includes Code splitting, Asset handling, CSS minification.

Advanced Features
-----------------

Environment Variables
*********************

.. code-block:: javascript

    // .env
    VITE_API_URL=https://api.example.com

    // Usage in code
    console.log(import.meta.env.VITE_API_URL)        

CSS Modules
***********

.. code-block:: css

    /* styles.module.css */
    .button {
        background: blue;
    }    

.. code-block:: javascript

    import styles from './styles.module.css'

    function Component() {
        return <button className={styles.button}>Click me</button>
    }        

Static Asset Handling
*********************

.. code-block:: javascript

    // Images
    import img from './img.png'

    // CSS
    import './styles.css'

    // JSON
    import data from './data.json'    

Plugins
*******

.. code-block:: javascript

    // vite.config.js
    import { defineConfig } from 'vite'
    import react from '@vitejs/plugin-react'
    import legacy from '@vitejs/plugin-legacy'

    export default defineConfig({
        plugins: [
            react(),
            legacy({
                targets: ['defaults', 'not IE 11']
            })
        ]
    })    


Setting Up API Proxy
********************

.. code-block:: javascript

    // vite.config.js
    export default defineConfig({
    server: {
        proxy: {
            '/api': {
                target: 'http://localhost:3001',
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/api/, '')
            }
        }
    }
    })    

Adding Global SCSS Variables
****************************

.. code-block:: javascript 

    // vite.config.js
    export default defineConfig({
        css: {
            preprocessorOptions: {
                scss: {
                    additionalData: `@import "./src/styles/variables.scss";`
                }
            }
        }
    })

Optimizing Dependencies
***********************

.. code-block:: javascript 

    // vite.config.js
    export default defineConfig({
        optimizeDeps: {
            include: ['lodash', 'react', 'react-dom']
        }
    })    

.. include::  /_templates/components/footer-links.rst
