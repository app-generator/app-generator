NextJS 
======

Next.js is a powerful React framework that enables features like server-side rendering, static site generation, and API routes right out of the box. 
It's developed by Vercel and has become one of the most popular choices for building modern web applications.

.. include::  /_templates/components/banner-top.rst

Here's what makes Next.js powerful:

- **Rendering options**: Choose between server-side rendering (SSR), static site generation (SSG), and client-side rendering
- **File-based routing**: Create pages by simply adding files to the pages directory
- **API routes**: Build your backend API alongside your frontend
- **Image optimization**: Automatically optimize images for better performance
- **Zero configuration**: Works out of the box with sensible defaults

A simple example of a Next.js page:

.. code-block:: jsx

   // pages/index.js
   import { useState } from 'react'

   export default function HomePage() {
   const [count, setCount] = useState(0)
   
   return (
      <div>
         <h1>Welcome to Next.js!</h1>
         <p>You clicked the button {count} times</p>
         <button onClick={() => setCount(count + 1)}>
         Click me
         </button>
      </div>
   )
   }

To fetch data server-side with Next.js:

.. code-block:: jsx

   // pages/blog/[slug].js
   export async function getServerSideProps({ params }) {
   const { slug } = params
   const postData = await fetchPostData(slug)
   
   return {
      props: {
         postData
      }
   }
   }

   export default function BlogPost({ postData }) {
   return (
      <article>
         <h1>{postData.title}</h1>
         <div>{postData.content}</div>
      </article>
   )
   }

Is there a specific aspect of Next.js you'd like to know more about?

.. include::  /_templates/components/footer-links.rst
   
Resources
---------

.. toctree::
   :maxdepth: 1
   
   nextjs/index
