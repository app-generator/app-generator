
:og:description: Building Components with Shadcn/ui

.. title::  Building Components with Shadcn/ui
.. meta::
    :description: Learn with examples how to build scalable React components with Shadcn/ui in Next.JS
    :keywords: next.js, shadcn, shadcn/ui in next.js, shadcn/ui tutorial


Building Components with Shadcn/ui
==================================

This guide goes through the process of initializing Shadcn/ui for building components in a Next.js application. It also briefly highlights the packages Shadcn incorporates and demonstrates with a couple of examples how to build your own library of robust and scalable React components styled with TailwindCSS.


Introduction
------------

`Shadcn/ui <https://ui.shadcn.com/docs>`__ is a React components generator that helps build bespoke UI component libraries styled with Tailwind variants. It accommodates a headless philosophy of separating the UI design of a component from its logical internal implementation.

Shadcn/ui produces fully customizable boilerplate code for highly composable components from scratch with basic JSX and `Radix UI <https://www.radix-ui.com/themes/docs/overview/getting-started>`__ on top of React. It derives and distributes Tailwind based variant props & classes with the help of `Class Variance Authority <https://cva.style/docs>`__ and employs a number of other open source libraries for charts, forms, tables, etc.

This guide is aimed at providing a good understanding of Shadcn fundamentals and helping developers get going on easily building robust TailwindCSS based React component libraries of their own.


Overview
--------

We first go through the initialization process and configurations for setting up the Shadcn/ui generator within a Next.js application. And then briefly discuss what goes under the hood in Shadcn with no package / component of its own, its headless UI paradigm, as well as the packages it uses / aligns with.

We get familiar with how to generate components using the Shadcn CLI. And with examples of a `React Hook Form <https://react-hook-form.com/get-started>`__ based form and a `Tanstack React Table <https://tanstack.com/table/latest/docs/introduction>`__ based data table, we also demonstrate how to compose powerful React components from Shadcn generated ones. Towards the end, we cover how to customize themes generated / managed by Shadcn.


.. include::  /_templates/components/banner-top.rst


Shadcn Initialization in Next.js
--------------------------------

Before we can start generating components using Shadcn/ui, we have to initialize the generator. We initialize Shadcn with its ``npx`` ``init`` command:

..	code-block:: bash

		npx shadcn@latest init


The ``init`` command operates differently depending on one of the three scenarios:

- If you don't have a ``package.json`` file in the current directory, it prompts you to approve the CLI to initialize a Next.js app first and goes ahead on installing TailwindCSS upon confirmation. It then initializes the generator on top of TailwindCSS.
- If you are inside a Next.js app with TailwindCSS installed, directly initializes the Shadcn/ui generator in it.
- If you have a Next.js app without TailwindCSS installed, it halts initializing the generator and prompts you to come back after manually installing TailwindCSS.



Configuration
-------------

Shadcn's interactive ``init`` shell helps choose initial configurations with the following prompts:

..	code-block:: bash

		Which style would you like to use? › New York
		Which color would you like to use as base color? › Zinc
		Do you want to use CSS variables for colors? › no / yes


Upon config selection and completion of the process, a ``components.json`` file is placed in the root directory. It contains the picked configurations and any default settings:

..	code-block:: javascript
		:emphasize-lines: 8,11,13-19

		{
			"$schema": "https://ui.shadcn.com/schema.json",
			"style": "New York",
			"rsc": true,
			"tsx": true,
			"tailwind": {
				"config": "tailwind.config.ts",
				"css": "src/app/globals.css",
				"baseColor": "Zinc",
				"cssVariables": true,
				"prefix": ""
			},
			"aliases": {
				"components": "@nextjs-shadcn/components",
				"utils": "@nextjs-shadcn/lib/utils",
				"ui": "@nextjs-shadcn/components/ui",
				"lib": "@nextjs-shadcn/lib",
				"hooks": "@nextjs-shadcn/hooks"
			},
			"iconLibrary": "lucide"
		}


The ``tailwind.css`` property defines where Shadcn should place its default CSS variables for variants. The ``aliases.components`` property defines the path where Shadcn should place the generated component files. You can set their locations according to your app preferences.


Customizing Shadcn/ui configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Common config customizations involve changing the ``css`` styles file path and the Tailwind class ``prefix`` properties under the ``tailwind`` settings. You'd be interested in adjusting the directory aliases under ``aliases`` according to your app directory structure.

It is important that you finalize the config settings before running the generator for installing components. Otherwise their locations will be inconsistent.


Shadcn/ui Core Style Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initialization of Shadcn adds the following packages to ``package.json``:

..	code-block:: bash

		npm install tailwindcss-animate class-variance-authority clsx tailwind-merge lucide-react

These are the essential style packages Shadcn employs in generating Tailwind classes for the boilerplate code.


Why Shadcn/ui is Unpackaged ?
-----------------------------

You'll notice that no package relevant to Shadcn/ui is added to ``package.json``. This is because Shadcn/ui is a command line ``npx`` generator that leverages third party open source libraries for producing customizable React components. So, its role is to generate boilerplate code for the app's components. You have to remain connected to the Internet in order for Shadcn to execute the ``npx`` commands and install the components.

Shadcn/ui intentionally chooses to be a generator, and has no plans of delivering components as a framework. Instead, it incorporates third party open source libraries average developers already are using out in the wild.


Open Source Headless Paradigm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shadcn/ui accommodates the headless paradigm for implementing React based components. While it provides the UI skeleton and manages Tailwind variants, local state management and feature implementation is left to the developer.

This means you can embrace any headless library of your choice for implementing complex functionaities like forms with React Hook Form, tables with Tanstack React Table or client side data fetching using Tanstack React Query, SWR and so on.


Packages Incorporated by Shadcn/ui
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Tailwind related packages above are delegated mainly the tasks of generating, managing and delivering Tailwind variant classes. `Lucide React <https://lucide.dev/guide/packages/lucide-react>`__ is the default library used for icons.

Apart from these core packages, Shadcn automatically installs:

- `Radix UI <https://www.radix-ui.com/themes/docs/overview/getting-started>`__ packages relevant to a particular set of components.

	Radix UI is commonly used for generating components. From simple ``<Button />``, ``<Input />`` sets to more involved ones such as ``<Accordion />``, ``<Toast />``, ``<Tabs />``, ``<Sheet />`` and etc.
- `React Hook Form <https://react-hook-form.com/get-started>`__ for forms.
- `Recharts <https://recharts.org/en-US/guide>`__ for charts.
- `Embla Carousel React <https://www.embla-carousel.com/get-started/>`__ for carousels.
- `React Resizable Panels <https://github.com/bvaughn/react-resizable-panels>`__ for resizable layouts.
- `Sonner <https://sonner.emilkowal.ski/getting-started>`__ for toasts.
- `React Day Picker <https://daypicker.dev/start>`__ for date pickers.
- `Input OTP <https://input-otp.rodz.dev/>`__ for OTP input components.
- `Vault <https://vaul.emilkowal.ski/getting-started>`__ for drawers.
- `CMDK <https://github.com/pacocoursey/cmdk>`__ for command menu components.


Generating Components Using Shadcn/ui
-------------------------------------

With Shadcn/ui, we generate components using the ``npx shadcn@latest add`` command. For example, in order to add the ``<Button />`` set, run:

..	code-block:: bash

		npx shadcn@latest add button



Shadcn/ui Button Component
~~~~~~~~~~~~~~~~~~~~~~~~~~

Running the button generator installs a ``button.tsx`` file to the configured path for Shadcn/ui components.

Inside the generated file, you'll notice Tailwind classes for button variants are managed by ``cva()``. The file avails a ``<Button />`` component and the ``buttonVariants`` util to the app for use in pages:

..	code-block:: javascript

		export { Button, buttonVariants }


Shadcn Input / Label Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can generate multiple sets of components in one go. For example, to install ``<Input />`` and ``<Label />`` sets in one command run:

..	code-block:: bash

		npx shadcn@latest add input label


This will put respective components inside ``input.tsx`` and ``label.tsx`` files. Notice, the generated components make use of ``React.forwardRef()`` for forwarding refs to child components. Ref forwarding enables Shadcn generated components for building robust, scalable components and help easily integrate with other libraries.


Shadcn Pagination Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's generate the ``<Pagination />`` components with ``npx shadcn@latest add pagination``. This produces a ``pagination.tsx`` file inside the configured path and exports the following set:

..	code-block:: javascript

		export {
			Pagination,
			PaginationContent,
			PaginationEllipsis,
			PaginationItem,
			PaginationLink,
			PaginationNext,
			PaginationPrevious,
		}



Customizing Shadcn Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can customize the code generated by Shadcn according to your needs. For example, ``<PaginationPrevious />`` and ``<PaginationNext />`` in the ``<Pagination />`` set, initially do not accommodate child components. I'd like them to accept ``chidren``:

..	code-block::
		:emphasize-lines: 3,12

		const PaginationPrevious = ({
			className,
			children,
			...props
		}: React.ComponentProps<typeof PaginationLink>) => (
			<PaginationLink
				aria-label="Go to previous page"
				size="default"
				className={cn("gap-1 pl-2.5", className)}
				{...props}
			>
				{children}
			</PaginationLink>
		)
		PaginationPrevious.displayName = "PaginationPrevious"


The customized components can now be used in any component we want.


Shadcn Generated Form Components
--------------------------------

You can generate the form component set by running ``npx shadcn@latest add form``.

This generates a ``form.tsx`` with code for these components: ``useFormField()``, ``<Form />``, ``<FormItem />``, ``<FormLabel />``, ``<FormControl />``, ``<FormDescription />``, ``<FormMessage />`` and ``<FormField />``.


React Hook Form Out-of-the-box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Shadcn/ui generated form components integrate of React Hook Form out-of-the-box. In particular, the following React Hook Form APIs are used: ``<Controller />``, ``FormProvider`` and ``useFormContext()``.


Compose a Next.js Form
~~~~~~~~~~~~~~~~~~~~~~

We can integrate additional libraries like ``zod`` and Zod resolver from ``@hookform/resolvers`` in order to compose a Next.js form using the generated components. So, install these packages separately:

..	code-block:: bash

		npm install zod @hookform/resolvers


An example form that integrates ``zod`` with Shadcn/ui generated components:

..	code-block::
		:emphasize-lines: 1

		"use client"

		import { useForm } from "react-hook-form"
		import { zodResolver } from "@hookform/resolvers/zod"
		import { z } from "zod"
		import {
			Form,
			FormControl,
			FormField,
			FormItem,
			FormLabel,
			FormMessage,
		} from "@nextjs-shadcn/components/ui/form"
		import { Button } from "@nextjs-shadcn/components/ui/button"
		import { Input } from "@nextjs-shadcn/components/ui/input"

		const formSchema = z.object({
			username: z.string().min(3, {
				message: "Username must be at least 3 characters",
			}),
			email: z.string().email({
				message: "You must enter a valid email",
			})
		})

		export default function Home() {
			const form = useForm<z.infer<typeof formSchema>>({
				resolver: zodResolver(formSchema),
				defaultValues: {
					username: "",
					email: "",
				},
			})

			function onSubmit(values: z.infer<typeof formSchema>) {
				// Server action here
				console.log(values)
			}

			return (
				<div className="w-2/3 mx-auto my-6 border rounded bg-gray-50 box-shadow-sm">
					<h2 className="my-2 p-2 text-3xl text-center font-bold">Create New User</h2>
					<div className="my-2 px-8 py-2">
						<Form {...form}>
							<form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
								<FormField
									control={form.control}
									name="username"
									render={({ field }) => (
										<FormItem>
											<FormLabel>Username</FormLabel>
											<FormControl>
												<Input
													{...field}
													placeholder="Enter username here"
												/>
											</FormControl>
											<FormMessage />
										</FormItem>
									)}
								/>
								<FormField
									control={form.control}
									name="email"
									render={({ field }) => (
										<FormItem>
											<FormLabel>Email</FormLabel>
											<FormControl>
												<Input
													{...field}
													placeholder="Enter your email"
												/>
											</FormControl>
											<FormMessage />
										</FormItem>
									)}
								/>
								<Button type="submit">Create User</Button>
							</form>
						</Form>
					</div>
				</div>
			)
		}



Shadcn Generated Table Components
---------------------------------

You can generate the Shadcn table set by running ``npx shadcn@latest add table``.

Doing so generates code for these components:

``<Table />``,  ``<TableHeader />``, ``<TableBody />``, ``<TableFooter />``, ``<TableHead />``, ``<TableRow />``, ``<TableCell />`` and ``<TableCaption />``.


Integrate with Tanstack React Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can integrate Tanstack React Table with these components in order to build powerful Next.js tables with pagination, sorting, filter & search capabilities.

Unlike the case with React Hook Form, Tanstack React Table does not get installed by Shadcn/ui automatically. We have to install it ourselves:

..	code-block:: bash

		npm install @tanstack/react-table


Below is a simple table example with pagination and sorting:

..	code-block::
    :emphasize-lines: 1

		"use client"

		import * as React from "react"
		import { ColumnDef, SortingState, flexRender, getCoreRowModel, getPaginationRowModel, getSortedRowModel, useReactTable } from "@tanstack/react-table"
		import { Table, TableBody, TableCell, TableHead, TableHeader,TableRow } from "@nextjs-shadcn/components/ui/table"
		import { Button } from "@nextjs-shadcn/components/ui/button"
		import { ArrowUpDown, ChevronLeft, ChevronRight } from "lucide-react"
		import { Pagination, PaginationContent, PaginationNext, PaginationPrevious } from "@nextjs-shadcn/components/ui/pagination"

		type User = { id: number, username: string, email: string, firstName: string, lastName: string,	country: string }

		// You'd get this from a server action or a cient side data fetching ibrary
		const data: User[] = [
			{
				id: 1,
				username: "heo_haskell",
				email: "heo@haskell.org",
				firstName: "Heo",
				lastName: "Haskell",
				country: "United States",
			},
			{
				id: 2,
				username: "neon_serverless",
				email: "neon@serverless.org",
				firstName: "Neon",
				lastName: "Serverless",
				country: "United States",
			},
		]

		export default function UsersListPage() {
			const [sorting, setSorting] = React.useState<SortingState>([])

			const columns: ColumnDef<User>[] = [
				{
					accessorKey: "id",
					header: "ID"
				},
				{
					accessorKey: "username",
					header: "Username"
				},
				{
					accessorKey: "firstName",
					header: ({ column }) => {
						return (
							<div className="flex items-center justify-between">
								First Name
								<Button
									className="p-0"
									variant="ghost"
									onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
								>
									<ArrowUpDown />
								</Button>
							</div>
						)
					},
				},
				// Other fields omitted
			]

			const table = useReactTable({
				data,
				columns,
				onSortingChange: setSorting,
				getCoreRowModel: getCoreRowModel(),
				getPaginationRowModel: getPaginationRowModel(),
				getSortedRowModel: getSortedRowModel(),
				state: {
					sorting,
				},
			})

			return (
				<div className="w-full p-2">
					<div className="py-2 text-2xl font-bold">Users List</div>
					<div className="flex items-center justify-between space-x-2 py-4">
						<div className="flex-1 text-sm text-muted-foreground">
							Page {table.getFilteredSelectedRowModel().rows.length} of{" "}
							{table.getPageCount()}
						</div>
						<div className="space-x-2">
							<Pagination>
								<PaginationContent>
									<PaginationPrevious>
										<Button  variant="outline"
											size="sm"
											onClick={() => table.previousPage()}
											disabled={!table.getCanPreviousPage()}
										>
											<ChevronLeft className="h-4 w-4" />
											Previous
										</Button>
									</PaginationPrevious>
									<PaginationNext>
										<Button
											variant="outline"
											size="sm"
											onClick={() => table.nextPage()}
											disabled={!table.getCanNextPage()}
										>
											Next
											<ChevronRight className="h-4 w-4" />
										</Button>
									</PaginationNext>
								</PaginationContent>
							</Pagination>
						</div>
					</div>
					<Table>
						<TableHeader className="bg-gray-50">
							{table.getHeaderGroups().map((headerGroup) => (
								<TableRow key={headerGroup.id}>
									{headerGroup.headers.map((header) => {
										return (
											<TableHead key={header.id}>
												{header.isPlaceholder
													? null
													: flexRender(
															header.column.columnDef.header,
															header.getContext()
														)}
											</TableHead>
										)
									})}
								</TableRow>
							))}
						</TableHeader>
						<TableBody>
							{table.getRowModel().rows?.length ? (
								table.getRowModel().rows.map((row) => (
									<TableRow
										key={row.id}
										data-state={row.getIsSelected() && "selected"}
									>
										{row.getVisibleCells().map((cell) => (
											<TableCell key={cell.id}>
												{flexRender(
													cell.column.columnDef.cell,
													cell.getContext()
												)}
											</TableCell>
										))}
									</TableRow>
								))
							) : (
								<TableRow>
									<TableCell
										colSpan={columns.length}
										className="h-24 text-center"
									>
										No results.
									</TableCell>
								</TableRow>
							)}
						</TableBody>
					</Table>
				</div>
			)
		}


You can take inspiration from this `<DataTable /> <https://ui.shadcn.com/docs/components/data-table>`__ example for implementing more nuanced and feature rich tables.


Theming with Shadcn
-------------------

Shadcn places a ``theme`` config object inside the ``tailwind.config.ts`` file. It contains variant configurations for theme properties like ``colors``, ``borderRadius`` and others. Shadcn determines and generates actual CSS classes for variants according to their definitions declared here.

Given you choose to use CSS Variables for these variants, Shadcn generates a corresponding set of default variables for them. They can be found inside the default ``globals.css`` file or any custom location of your global stylesheet.

..	code-block:: css

		:root {
			--background: 0 0% 100%;
			--foreground: 222.2 47.4% 11.2%;
			--muted: 210 40% 96.1%;
			--muted-foreground: 215.4 16.3% 46.9%;
			--popover: 0 0% 100%;
			--popover-foreground: 222.2 47.4% 11.2%;
			--border: 214.3 31.8% 91.4%;
			--input: 214.3 31.8% 91.4%;
			--card: 0 0% 100%;
			--card-foreground: 222.2 47.4% 11.2%;
			--primary: 222.2 47.4% 11.2%;
			--primary-foreground: 210 40% 98%;
			--secondary: 210 40% 96.1%;
			--secondary-foreground: 222.2 47.4% 11.2%;
			--accent: 210 40% 96.1%;
			--accent-foreground: 222.2 47.4% 11.2%;
			--destructive: 0 100% 50%;
			--destructive-foreground: 210 40% 98%;
			--ring: 215 20.2% 65.1%;
			--radius: 0.5rem;
		}

		.dark {
			--background: 224 71% 4%;
			--foreground: 213 31% 91%;
			--muted: 223 47% 11%;
			--muted-foreground: 215.4 16.3% 56.9%;
			--accent: 216 34% 17%;
			--accent-foreground: 210 40% 98%;
			--popover: 224 71% 4%;
			--popover-foreground: 215 20.2% 65.1%;
			--border: 216 34% 17%;
			--input: 216 34% 17%;
			--card: 224 71% 4%;
			--card-foreground: 213 31% 91%;
			--primary: 210 40% 98%;
			--primary-foreground: 222.2 47.4% 1.2%;
			--secondary: 222.2 47.4% 11.2%;
			--secondary-foreground: 210 40% 98%;
			--destructive: 0 63% 31%;
			--destructive-foreground: 210 40% 98%;
			--ring: 216 34% 17%;
		}


Customizing Shadcn Theme
~~~~~~~~~~~~~~~~~~~~~~~~

You can customize the theme configurations generated by Shadcn by applying your preferences in the ``components.json`` and ``tailwind.config.ts`` files as well as your global stylesheet (such as the ``globals.css`` file).


Adding New Variants
###################

In order to add a new variant, first add the entry to ``tailwind.config.js``:

..	code-block:: javascript
		:emphasize-lines: 5,6

		module.exports = {
			theme: {
				extend: {
					colors: {
						success: "hsl(var(--success))",
						"success-foreground": "hsl(var(--success-foreground))",
					},
				},
			},
		}


And then define their CSS variables inside your global stylesheet for default theme in ``root`` and dark states in ``dark``:

..	code-block:: javascript
		:emphasize-lines: 2-3, 7-8

		:root {
			--success: 38 92% 50%;
			--success-foreground: 48 96% 89%;
		}

		.dark {
			--success: 48 96% 89%;
			--success-foreground: 38 92% 50%;
		}


Using Tailwind Utilities for Theming
####################################

For using Tailwind utilities for theming, first inside the ``components.json`` file, set ``"cssVariables": false``.

And then use regular Tailwind theming classes in your components:

..	code-block:: javascript

		<div className="bg-zinc-950 dark:bg-white" />



Shadcn/ui Next.js Example App
-----------------------------

You can find the working code for the above example snippets in the demo Next.js Shadcn app available in `this repository <https://github.com/app-generator/docs-nextjs-shadcn-components>`__.


.. include::  /_templates/components/footer-links.rst
