:og:description: React Hook Form Basics - Learn how middlewar it works in Next.js

React Hook Form Basics
======================

.. title:: React Hook Form Basics - Learn how middlewar it works in Next.js
.. meta::
    :description: React Hook Form: Theory and pratical aspects in Next.js
    :keywords: next.js forms, React Hook Form, React Hook Form tutorial, next.js hook forms tutorial


This guide demonstrates the basics of using `React Hook Form </https://react-hook-form.com/>`__ in `Next.js <./index.html>`__. 
We cover the most fundamental RHF APIs for implementing performant React forms with intuitive client side field validations and form submission.

.. include::  /_templates/components/banner-top.rst

Pre-requisites
--------------

Next.js & TypeScript
"""""""""""""""""""""""

This guide assumes you're hands on with Next.js and are pretty wearied of building complex forms with controlled React fields. Also, you are keen on building nuanced React forms with TypeScript.


Next.js App with React Hook Form
--------------------------------

First, start a Next.js app named ``nextjs-rhf`` with app router, TypeScript and TailwindCSS. So, in your terminal execute:

..	code-block:: bash

		npx create-next-app@latest

And choose a configuration similar to the following: ::

	✔ What is your project named? … nextjs-rhf
	✔ Would you like to use TypeScript? … Yes
	✔ Would you like to use ESLint? … Yes
	✔ Would you like to use Tailwind CSS? … Yes
	✔ Would you like your code inside a `src/` directory? … Yes
	✔ Would you like to use App Router? (recommended) … Yes
	✔ Would you like to use Turbopack for next dev? … No
	✔ Would you like to customize the import alias (@/* by default)? … Yes
	✔ What import alias would you like configured? … @/*

Once initialized, run the application with:

..	code-block:: bash

		npm run dev


This should have the app live on: ``http://localhost:3000/``


Set Up React hook Form
""""""""""""""""""""""

React Hook Form is a robust React form management library that helps build nuanced form experiences, from simple forms to advanced multi-step forms that demand integration to third party libraries.

There's only one package for using all native features of React Hook Form. It already comes with supported TS types, so no DefinitelyTyped packages are needed.

To install React Hook Form, run:

..	code-block::

	npm i react-hook-form


This sets us up for implementing neat React forms by managing a form's data, its overall state, errors, individual fields data, their states, validations, and much more -- using just one hook, the ``useForm()`` hook.


Additional Packages
"""""""""""""""""""

The example app built in this guide uses `TailwindCSS <https://tailwindcss.com/docs/installation/framework-guides/>`__ with `DaisyUI <https://daisyui.com/docs/install//>`__. It also uses a `JSON Server </https://github.com/typicode/json-server/tree/v0?tab=readme-ov-file#getting-started>`__ to store and query data via REST endpoints.
Feel free to refer to their respective docs in case you need to dive into their setup.


Working with React Hook Form in Next.js
---------------------------------------

Inside a React component, we have to initialize a React Hook Form instance with the ``useForm()`` hook ``import``-ed from the ``react-hook-form`` package.

..  code-block::
    :emphasize-lines: 7

    const {
      register,
      handleSubmit,
      watch,
      getValues,
      formState: { errors, isDirty, isValid },
    } = useForm<TPost>({
          mode: "onChange",
	  criteriaMode: "all",
	  reValidateMode: "onSubmit",
        });


Doing so gives a local RHF object with a bunch of methods and objects to construct the form according to our needs. The most essential React Hook Form APIs include ``register``, ``formState``, ``handleSubmit`` and ``reset``. ``formState`` encapsulates different states the form can be in. For this demo, we're interested in the ``errors``, ``isDirty`` and ``isValid`` properties.

With these fundamental RHF APIs, we can build some decent form features with responsive field validations and error feedback that are superior than those painfully built from scratch.


Configuring React Hook Form
"""""""""""""""""""""""""""

We pass a configuration object to ``useForm()`` in order to prefer certain form behaviors. For example:

..  code-block::
    :emphasize-lines: 2-9

    const form = useForm<TPost>({
      mode: "onChange",
      defaultValues: {
        title: "",
        subtitle: "",
        content: "",
      },
      criteriaMode: "all",
      reValidateMode: "onSubmit",
    });


Here, ``mode`` lets us choose when field validations should run, and we want them to run on the ``"onChange"`` event. With ``reValidateMode: "onSubmit"``, we want to run a revalidation when form submission is invoked. And with ``criteriaMode: "all"``, we want access to all errors on a particular field.
We have also set default values of the fields with the ``defaultValues`` property.

Other behaviors we can set are ``values``, ``shouldFocusError``, ``resetOptions``, ``shouldUnregister``, etc. For details, please refer to the `React Hook Form configuration docs here </https://react-hook-form.com/docs/useform#mode>`__.


Form Data & Field Registration
""""""""""""""""""""""""""""""

Form data in React Hook Form is central to all its features. RHF form data is automatically availed to the ``handleSubmit()`` method for submission and is generally inferred as ``data``. It can be accessed by ``getValues()`` as well as via ``watch()``.

Form ``data`` is a ``null``-ish object at initialization. We have to explicitly add fields to it with the ``register()`` method. As with the ``title`` field shown below:

..  code-block:: 
    :emphasize-lines: 2

    <input
      {...register("title")}
      type="text"
      placeholder="Add a title"
    />


The ``register()`` method produces React Hook Form specific values for ``name``, ``ref``, ``onChange`` and ``onBlur`` properties for us to place on a target form field. So, with the above ``{...register("title")}`` spread operation, we are registering ``title`` to the form data, and setting React Hook Form values for ``name``, ``ref``, ``onChange`` and ``onBlur`` on the ``<input />`` field.

That way, ``title`` is now registered as a field on the form ``data`` object. And the ``<input />`` field inherits the behavior of a React Hook Form input field.


Setting Validation Rules
""""""""""""""""""""""""

We set up validation rules while registering a field. For example, for the ``title`` field, we have two rules:

..  code-block::
	:emphasize-lines: 3-10
	
	<input
		{...register("title", {
			minLength: {
				value: 3,
				message: "Title should be at least 3 characters."
			},
			maxLength: {
				value: 60,
				message: "Title exceeded the limit of 60 characters."
			},
		})}
	/>


Here, we have defined ``maxLength`` and ``minLength`` rules with custom messages using React Hook Form's long format. For shorter validation formats, feel free to check `this section of RHF docs </https://react-hook-form.com/docs/useform/register#options>`__.


Displaying Errors in React Hook Form
""""""""""""""""""""""""""""""""""""

React Hook Form gives us the ``formState`` object that keeps track of various states of the form. States stored in ``formState`` include ``errors`` and other details related to whether the form or a particular field has been touched, changed; or the form is loading, submitting or submitted, etc.

We can destructure the ``formState.errors`` object and display validation feedbacks while a specific field gets filled. For example, for the ``title`` ``<input />`` field, we can display its error in a ``<span />`` tag:


..  code-block::

    { errors?.title && <span className="my-2 text-xs text-red-700">{errors?.title?.message}</span> } 
 


Submitting a Form in RHF
""""""""""""""""""""""""

For submitting a form, we pass the ``handleSubmit()`` method to ``onSubmit`` event on the ``<form/>`` element:

..  code-block::
    :emphasize-lines: 2

    <form
      onSubmit={handleSubmit(createNewPost)}
    >
    ...
    </form>


The ``handleSubmit()`` method accepts a form submission handler and hands over the form's ``data`` to it. For this form, we have a ``createNewPost()`` function that creates a post from the form data. It looks like this:

..  code-block::
    :emphasize-lines: 2

    const createNewPost = async (data: TPost) => {
      await createPost(data);

      reset(defaultValues);
      redirect("/");
    };


The submit handler (``createNewPost`` here), typically uses ``data`` to performs database operations. In our case, it invokes a Next.js server action: ``createPost()``.


Resetting a Form in RHF
#######################

We can reset the RHF form to a desired value with the React Hook Form ``reset()`` API. For example, inside the ``createNewPost()`` function, we have reset our form to ``defaultValues``:

..  code-block::
    
    reset(defaultValues);



Using Form States in React Hook Form
"""""""""""""""""""""""""""""""""""""""

React Hook Form makes it extremely convenient to implement superior form experiences. For example, we can apply a button lock when the form is ``isDirty`` and is not valid (``!isValid``):

..  code-block::
    :emphasize-lines: 2

    <button
      disabled={isDirty && !isValid}
      type="submit"
      className="btn btn-primary"
    >
      Create Post
    </button>



So, here, we picked ``isDirty`` and ``isValid`` from ``formState`` to build a lock that disables the button when a form field ``isDirty`` and the form is in invalid state. This way, the button is enabled only when the user has entered something and they are valid values.


React Hook Form: TypeScript Support
"""""""""""""""""""""""""""""""""""

React Hook Form inherently supports TypeScript. It means when we're using React Hook Form in a TypeScript based application, it automatically infers appropriate TypeScript types for form entities. For example, it infers the type for form values from ``defaultValues``.

If you want the form data to conform explicitly to a type, you can pass it to ``useForm()``:

..  code-block::
    :emphasize-lines: 6

    const {
      register,
      handleSubmit,
      reset,
      formState: { errors, isValid, isDirty }
    } = useForm<TPost>();


Here, we want the form to handle form data with the ``TPost`` type. And we are explicit about it.

React Hook Form has types support for all necessary entities and functions. Please refer to `this section of RHF docs </https://react-hook-form.com/ts>`__ for relevant information.


React Hook Form: Next.js Specific Notes
"""""""""""""""""""""""""""""""""""""""

Next.js app router pages, by default, are rendered serverside for performance benefits. However, this default behavior renders static pages to the client. So, a form action in default rendered pages is not accessible from the browser.

For this reason, forms in Next.js and in particular, React Hook Form which needs dynamic rendering to run field validations, need to be rendered client side. This has to be done explicitly with the ``"use client"`` directive declared at the top of the component.


Next.js - React Hook Form Example App
-------------------------------------

For more insight, you can explore the example Next.js app for this guide in `this branch </>`__ of the `repository over here </>`__. Please follow the instructions on the ``README.md`` file for setting up and geting a copy running.


.. include::  /_templates/components/footer-links.rst
