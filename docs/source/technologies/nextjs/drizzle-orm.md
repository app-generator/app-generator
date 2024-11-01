
# Drizzle ORM with Server Components in Next.js - A Useful Guide

## Introduction

This quick guide demonstrates the use of [Drizzle](https://orm.drizzle.team/docs/get-started) with server components in Next.js. We breeze past the initial steps for spinning up a local PostgreSQL server and starting a Next.js app. And follow through with the process of installing Drizzle ORM and configuring it to connect to a running Postgres instance, setting up schemas, generating migration files as well as performing migrations and seeding. Towards the end, we focus on the important aspects of performing queries and mutations in Next.js with Drizzle methods.


## Pre-requisites

### PostgreSQL Setup

This guide requires prior knowledge of PostgreSQL. The developer should come hands on about how to spin up a local Postgres instance using either `psql` or GUI applications like [pgAdmin](https://www.pgadmin.org/download/). If you need a hand, please feel free to follow [this tutorial on Youtube](https://www.youtube.com/watch?v=KuQUNHCeKCk), and have your local Postgres instance prepared.

### Next.js with TypeScript

Drizzle is designed to be type-safe with TypeScript. So, we assume you are already building stuff with TypeScript in Next.js. The use of app router, forms and server actions with TypeScript are most relevant for the code in this guide.


### Additional Packages

The demo app in this guide uses React Hook Form and Zod alongside Drizzle. Their usage in the app is pretty easy to grasp and is not the scope of this post. We expect you come familiar with the basics of form validation using [React Hook Form](https://www.react-hook-form.com/get-started/), [Zod](https://zod.dev/) and their [resolver](https://github.com/react-hook-form/resolvers/tree/master/zod) from respective documentations.

We also use [TailwindCSS](https://tailwindcss.com/docs/installation/framework-guides) with [DaisyUI](https://daisyui.com/docs/install/). Feel free to refer to their docs in case you need to dive into their setup.


## Spinning Up a Local Postgres Instance

First, have PostgreSQL installed locally and start a running database instance named `drizzle_nextjs` using either `psql` or [pgAdmin](https://www.pgadmin.org/docs/). Please refer to this [Youtube tutorial](https://www.youtube.com/watch?v=KuQUNHCeKCk) if you need a fresher.


### PostgreSQL Credentials

Have the credentials of your Postgres instance ready, preferably in a `.env` file stored at the root. They'll be used to set up a Postgres client. More on this [here](#setting-up-a-pg-client-for-drizzle).


## Initializing and Running the Next.js App

Initialize a Next.js app named `drizzle-nextjs` with app router, TypeScript and TailwindCSS by starting with:

```bash
npx create-next-app@latest
```

At the end, you should have a configuration similar to the following:

```bash
✔ What is your project named? … drizzle-nextjs
✔ Would you like to use TypeScript? … Yes
✔ Would you like to use ESLint? … Yes
✔ Would you like to use Tailwind CSS? … Yes
✔ Would you like your code inside a `src/` directory? … Yes
✔ Would you like to use App Router? (recommended) … Yes
✔ Would you like to use Turbopack for next dev? … No
✔ Would you like to customize the import alias (@/* by default)? … Yes
✔ What import alias would you like configured? … @/*
```

Once initialized, run the application with:

```bash
npm run dev
```

This should have the app running on: `http://localhost:3000/`

## Setting Up Drizzle ORM in Next.js

Now it's time to install and configure Drizzle with the core and related modules. And then create a `pg` client for setting up connections to the local instance.

### Installing Drizzle ORM and Related Modules

We want the [`drizzle-orm`](https://github.com/drizzle-team/drizzle-orm) package, the JavaScript [`pg`](https://github.com/brianc/node-postgres) module and [Drizzle Kit](https://orm.drizzle.team/docs/kit-overview). In development, we need TS support package for `pg`. So, run the following to have them all installed:

```npm
npm i drizzle-orm pg drizzle-kit
npm i -D @types/pg
```

The `drizzle-orm` package houses core dialect modules and we are going to have [`drizzle-orm/pg-core`](https://orm.drizzle.team/docs/get-started-postgresql) interact with the Postgres tables. We want to connect to Postgres in a Node.js environment with the [`drizzle-orm/node-postgres`](https://orm.drizzle.team/docs/get-started-postgresql#node-postgres) adapter.

Drizzle supports Zod schema derivation and manipulation with the [`drizzle-zod`](https://orm.drizzle.team/docs/zod) optional module. In the demo, we use Zod with React Hook Form and Zod resolver. So, go ahead and install them as main deps:

```npm
npm i zod drizzle-zod react-hook-form @hookform/resolvers
````

Additionally, we need to store environemnt variables with `dotenv` and run migrations/seeding with `tsx`:

```npm
npm i tsx dotenv
```


### Configuring Drizzle

Create a `drizzle.config.ts` file in the application root. Use [`defineConfig()`](https://orm.drizzle.team/docs/drizzle-config-file) function from `drizzle-kit` to set Drizzle configurations. It should specify the source `schema` path, an `out` directory for storing generated Drizzle migration files, the database dialect and the Postgres server `url` with credentials:

```ts title="./drizzle.config.ts"
import "dotenv";
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/drizzle/schema",
  out: "./src/drizzle/migrations",
  dialect: 'postgresql',
  dbCredentials: {
    // highlight-next-line
    url: `S{process.env.DB_URL}`,
  },
  verbose: true,
  strict: true,
});
```

With the above setup, we declare that we want to manually create our Drizzle schema files inside `./src/drizzle/schema/` and have Drizzle Kit output migration files from them to `./src/drizzle/migrations/`. Clearly, we are planning to store all Drizzle stuff inside a `./src/drizzle/` directory of the Next.js app.

The `dbCredentials.url` property to should evaluate to this pattern: `"postgres://db_username:db_password@db_host:db_port_no/db_name"`


### Setting Up a `pg` Client for Drizzle

We need to then define a client to connect Postgres to Drizzle in Node.js environment. We can create a client with the `pg` `Pool()` constructor. So, create a `./src/drizzle/` directory. And then have a `client.ts` file like this:

```ts title="./src/drizzle/client.ts"
import 'dotenv/config';
// highlight-next-line
import { Pool } from "pg";

export const client = new Pool({
	host: process.env.DB_HOST,
	port: parseInt(process.env.DB_PORT_NO as string),
	user: process.env.DB_USERNAME,
	password: process.env.DB_PASSWORD,
	database: process.env.DB_NAME
});
```

In a `.env` file, we need to set the above environment variables using credentials from the running Postgres instance.

We can now use this `client` to connect to the server for migrations, seeding and performing queries and mutations.


## Migrations and Seeding in Drizzle

Drizzle migrations involve first defining schemas or table definitions along with necessary entity relations. Schema definitions are used for generating migration files by Drizzle Kit CLI with the `npx drizzle-kit generate` command. We then invoke migrations on the database based on the produced migration files,.


### Drizzle Schema Definitions

For Drizzle Kit to generate migration files for us, we have to set up Drizzle schemas in the path we specified in the `drizzle.config.ts` file: `./src/drizzle/schema/`. So, go ahead create the `schema` folder and place definitions for `todos` and `categories`.

A typical schema file for an entity should have its table definition, relations with other database entities, Drizzle/Zod schemas and TypeScript types derived from these schemas. Please refer to the [Drizzle docs](https://orm.drizzle.team/docs/overview) for more information.

For `todos` in our demo app, it looks like this:

<details>

<summary>Show `todos` schema</summary>

```ts title="./src/drizzle/schema/todos.ts"
import { integer, pgTable, serial, timestamp, varchar } from "drizzle-orm/pg-core"
import { relations } from "drizzle-orm";
import { createInsertSchema, createSelectSchema } from "drizzle-zod";
import * as zod from "zod";
import { categories } from "@/drizzle/schema";

export const todos = pgTable("todos", {
	id: serial("id").primaryKey().unique(),
	title: varchar("title", { length: 255, }).notNull(),
	description: varchar("subtitle", { length: 500, }),
	categoryId: integer("category_id").references(() => categories.id, { onDelete: "cascade" }),

	createdAt: timestamp("created_at", { mode: "string"}).notNull().defaultNow(),
	updatedAt: timestamp("updated_at", { mode: "string" }).notNull().defaultNow(),
});

export const todosRelations = relations(todos, ({ one }) => ({
	category: one(categories, {
		fields: [todos.categoryId],
		references: [categories.id],
	}),
}));

export const TodoSchema = createSelectSchema(todos);
export const TodosListSchema = zod.array(TodoSchema);
export const NewTodoSchema = createInsertSchema(todos).pick({
	title: true,
	description: true,
	categoryId: true,
});

export type TTodo = zod.infer<typeof TodoSchema>;
export type TNewTodo = zod.infer<typeof NewTodoSchema>;
```

</details>


Likewise, the `categories` schema file should also have its table definitions, relations, Drizzle/Zod schema definitions and derived TypeScript types for use in the frontend:

<details>

<summary>Show `categories` schema</summary>

```ts title="./src/drizzle/schema/categories.ts"
import { relations } from "drizzle-orm";
import { pgTable, serial, text, timestamp, varchar } from "drizzle-orm/pg-core"
import { createInsertSchema, createSelectSchema } from "drizzle-zod";
import * as zod from "zod";
import { todos } from "@/drizzle/schema";
import { TTodo } from "@/drizzle/schema/todos";

export const categories = pgTable("categories", {
	id: serial("id").primaryKey().notNull().unique(),
	name: varchar("name", { length: 90, }).notNull().unique(),
	description: text("description"),
	
	createdAt: timestamp("created_at", { mode: "string"}).notNull().defaultNow(),
	updatedAt: timestamp("updated_at", { mode: "string" }).notNull().defaultNow(),
});

export const categoriesRelations = relations(categories, ({ many }) => ({
	todos: many(todos),
}));

export const CategorySchema = createSelectSchema(categories);

export const NewCategorySchema = createInsertSchema(categories).pick({
	name: true,
	description: true,
});

type TTodosArray = {
	todos: TTodo[];
};

export type TCategory = zod.infer<typeof CategorySchema>;
export type TCategoryWithTodos = TCategory & TTodosArray;
export type TNewCategory = zod.infer<typeof NewCategorySchema>;
```

</details>


And then export the table and relations definitions from an `index.ts` file:

```ts title="./src/drizzle/schema/index.ts"
export { categories, categoriesRelations } from "./categories";
export { todos, todosRelations  } from "./todos";
```


### Generating Migration Files with Drizzle Kit CLI

With the schemas defined, we have to now use Drizzle Kit CLI for generating migration files from them. The command for generating Drizzle migration files is: `npx drizzle-kit generate`. We can create an `npm` script from this in `package.json` under `scripts`:

```json
"scripts: {
	"db:generate": "npx drizzle-kit generate",
}
```

Now, in order to generate the migration files and place them inside `./src/drizzle/migrations/`, just run:

```bash
npm run db:generate
```

### Running Drizzle Migrations

For running migrations from the generated files, we need to first create a Drizzle connection with the running PostgreSQL server. In order to initialize a connection, we can use the `pg` `client` we defined [earlier](#setting-up-a-pg-client-for-drizzle) and pass it to the `drizzle()` function provided by `drizzle-orm/node-postgres`. Then in order to invoke migration, we have to pass this connection to the `migrate()` function availed by `drizzle-orm/node-postgres/migrator`.

So, create a `migrate.ts` file under `src/drizzle/` and define a `runMigrations()` function using this code:

```ts title="./src/drizzle/migrate.ts"
import { drizzle } from "drizzle-orm/node-postgres";
// highlight-next-line
import { migrate } from "drizzle-orm/node-postgres/migrator";
import { client } from "@/drizzle/db";

async function runMigrations() {
	// highlight-start
	await migrate(drizzle(client), {
		migrationsFolder: "./src/drizzle/migrations",
	});
	// highlight-end
	await client.end();
};

runMigrations();
```

With `migrationsFolder`, we have to explicitly specify where our migration files are located. We have to also close the connection because we want the migration operation to be one off.

We can now invoke `runMigrations()` in order to perform the migrations on the connected database.

For this, we should use `tsx` to run `migrate.ts` file with this command on the terminal: `tsx ./src/drizzle/migrate.ts`. We can also create an `npm` script for `db:migrate`:

```json
"scripts: {
	"db:migrate": "tsx ./src/drizzle/migrate.ts",
}
```

So, now run the migrations with the following command:

```bash
npm run db:migrate
```

At this point, if you check pgAdmin, you should see the tables placed inside the `drizzle_nextjs` database.


### Seeding PostgreSQL Database with Drizzle

It's now time to seed the database. We can fill the tables with mock entries using another connection.

Create a `db.ts` file under `./src/drizzle/`. It should contain a `drizzle()` connection that is made from the `pg` `client` and table schemas. `db.ts` will be used just for performing queries and mutations. So, it is important that we pass table definitions and relations from the schema files we defined above:

```ts title="./src/drizzle/db.ts"
import { drizzle } from 'drizzle-orm/node-postgres';
import { client } from './client';
import * as schema from "@/drizzle/schema";

export const db = drizzle(client, { schema });
```

Here, we prefer to import all the table definitions and relations as `schema` -- as indicated by the `* as schema` import, and pass them to `drizzle()` all at once. We can use this `db` instance for seeding as well as queries and mutations from Next.js.

For seeding, we can now use this `db` connection to define a `seed()` function, as below:

<details>

<summary>Show `seed.ts` file</summary>

```ts title="./src/drizzle/seed.ts"
import { db } from "@/drizzle/db";
import { categories, todos } from "@/drizzle/schema";

async function seed() {
	await db.insert(categories).values([
		{ name: "Chores", description: "Household activities. Inlcudes cleaning, rearranging, plumbing, etc." },
		{ name: "Exercise", description: "Perform physical health activities." },
		{ name: "Shopping", description: "Buy stuff for self, family members, gifts for others." },
		{ name: "Build", description: "Build stuff with React." },
		{ name: "Study", description: "Read, educate self, share knowledge with others." },
	]);
	
	await db.insert(todos).values([
		{ title: "Do Drizzle with Next.js", description: "The rain has a database. It's Drizzle. Build with Drizzle", categoryId: 4 },
		{ title: "Go jogging", description: "Start with a walk. Then jog across the park. No sprinting today.", categoryId: 2 },
		{ title: "Buy grocery", description: "See list for details.", categoryId: 3 },
		{ title: "Do the laundry", description: "Have all clothes washed, dried and ironed." },
		{ title: "Write about Drizzle", description: "Drizzle goes on. To the 1000th day we're flooded. The roads are clogged. Murky. Muddy. Slippery", categoryId: 2 },
		{ title: "Rearrange furniture", description: "Rearrange couch, tables and bookshelf in living room. Do cleanups." }
	]);
};

seed();
```

</details>


`seed()` aims to insert mock entries to `categories` and `todos` tables thanks to Drizzle's SQL-like `db.insert()` method.

We can now set the following `npm` `db:seed` command for invoking seeding:

```json
"scripts": {
	"db:seed": "tsx ./src/drizzle/seed.ts"
},
```

And then call it for the first seeding or whenever we need to:

```bash
npm run db:seed
```

And, when we use the pgAdmin Query Tool, we can see these entries in `todos` and `categories` tables.

With all the Drizzle setup aspects completed, we can now go ahead and work on queries and mutations from the Next.js application.


## Drizzle ORM in Next.js: Performing Queries and Mutations

In Next.js, server side data fetching is more performant for static pages. And in the app router, we are limited to implementing client side data fetching only using the JS `fetch()` API and dependent libraries. This is mainly because for a given route, Next.js only exposes the `page.tsx` file to the client and restricts all other files and directories to the serverside. This means that, our `./src/drizzle/` directory is permanently inaccessible from the client, and so the only option to perform Drizzle queries and mutations in Next.js is to do them in the server side.

Next.js app router, by default, renders all pages serverside. This means, we can readily invoke Drizzle `db` queries to feed app router pages. In cases of forms, we have to create server actions that wrap `db.insert()` and `db.delete()` operations explicitly with the `"use server"` directive. At the same time, we need to make Drizzle mutation forms and/or buttons render client side explicitly with `"use client"`. This is especially necessary in cases where forms are handled dynamically with libraries like React Hook Form.

In the below sections, the working examples from the demo app are meant to clarify fundamental cases.


### Drizzle Queries in Next.js: Default Server Rendered Pages

For default rendered Next.js > 14 pages with app router, we can directly perform **queries**. This is possible because by default app router renders pages serverside.

For example, in our demo DrizzleNextjsTodoApp, we are able to query `todos` directly from the component with `db.query.todos.findMany()`:

<details>

<summary>Show default rendered page with Drizzle query</summary>

```tsx title="./src/app/todos/page.tsx"
import React from "react";
import Link from "next/link";
import { desc } from "drizzle-orm";
import { db } from "@/drizzle/db";
import TodoListDeck from "./TodosListDeck";
import { todos } from "@/drizzle/schema";

const Todos = async () => {
	// highlight-start
	const todosList = await db.query.todos.findMany({
		with: {
			category: true,
		},
		orderBy: [desc(todos.id),]
	});
	// highlight-end
  
  return (
    <div className="page">
			<div className="mt-12 mb-6 flex justify-between items-center">
				<h2 className="text-6xl mb-4">All Todos</h2>
				<Link href="/todos/new" className="btn btn-primary btn-md">Create A Todo</Link>
			</div>
				// highlight-next-line
				<TodoListDeck todosList={todosList} />
		</div>
  );
};

export default Todos;
```

</details>


Since the page is already being rendered serverside, we don't need to explicitly invoke the `"use server"` directive. Notice also, we have to make the page an `async` component in order to accommodate receival of a query response.


### Drizzle Mutations in Next.js

Drizzle mutations in Next.js must also happen in the server side. This is so since the `db` connection placed inside `./src/drizzle/db.ts` is not availed to the client side. So, all Drizzle mutations should be wrapped as **server actions** with the `"use server"` directive.


#### Implement Drizzle Mutations with Server Actions

For example, in the demo todos app, we have a `createCategory()` function that wraps `db.insert()` as an server action:

```ts title="./src/app/categories/new/actions.ts"
// highlight-next-line
"use server"

import { db } from "@/drizzle/db";
import { categories, TNewCategory } from "@/drizzle/schema/categories";
import { revalidatePath } from "next/cache";

export const createCategory = async (data: TNewCategory) => {
	await db.insert(categories).values(data);
	revalidatePath("/categories");
};
```

Similarly, we have a `deleteCategory()` action that wraps `db.delete()` with `"use server"`:

```ts title="./src/app/categories/actions.ts"
// highlight-next-line
"use server"

import { eq } from "drizzle-orm"
import { categories } from "@/drizzle/schema"
import { db } from "@/drizzle/db";
import { revalidatePath } from "next/cache";

export const deleteCategory = async (id: number) => {
	await db.delete(categories).where(eq(categories.id, id));
	revalidatePath("/categories");
};
```

This is halfway done. Since server rendered static components are unable to access these actions, we have to make their forms and buttons dynamic in the client side.


#### Drizzle in Next.js: Forms Must be Client Rendered

In order to access and invoke Drizzle mutations via server actions, we have to make Next.js forms, fields and buttons render client side -- explicitly with the `"use client"` directive.

For example, at the `/todos/new` page, a form data is handled dynamically using React Hook Form and Zod inside `<CreateTodoForm />`:

<details>
<summary>Show explicitly client rendered form</summary>

```tsx title="./src/app/todos/new/CreateTodoForm.tsx"
// highlight-next-line
"use client"

import React, { ReactNode } from "react";
import { SubmitHandler, useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { NewTodoSchema, TNewTodo } from "@/drizzle/schema/todos";
import { TCategory } from "@/drizzle/schema/categories";
import { createTodo } from "./actions";
import { useRouter } from "next/navigation";

type TCreateTodoFormProps = {
	categories?: TCategory[];
};

const CreateTodoForm = ({ categories }: TCreateTodoFormProps) => {
	const router = useRouter();
	
	const { reset, register, handleSubmit, formState: { errors } } = useForm<TNewTodo>({
    resolver: zodResolver(NewTodoSchema),
    mode: "onChange",
    criteriaMode: "all",
    shouldFocusError: true,
    reValidateMode: "onSubmit",
  });  
  
  // highlight-start
	const createNewTodo: SubmitHandler<TNewTodo> = async (data: TNewTodo) => {
		await createTodo(data);
		reset({});
		router.push("/");
	};
	// highlight-end

	return (
		<form 
			// highlight-next-line
			onSubmit={handleSubmit(createNewTodo)}
		>
			<div className="mb-4">
				<label
					className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
				>
					Title
				</label>
			<input
				type="text"
				{...register("title")}
				className="text-field"
				placeholder="Todo title"
			/>
			{
				errors?.title && (
					<span className="text-sm text-red-700">{errors?.title?.message as ReactNode}</span>
				)
			}
			</div>
			
			<div className="mb-4">
				<label
					className="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-2"
				>
					Description
				</label>
				<textarea
					{...register("description")}
					className="text-field"
					rows={6}
					placeholder="Add todo description"
				>
				</textarea>
				{
				errors?.description && (
					<span className="text-xs text-red-700">{errors?.description?.message as ReactNode}</span>
				)
			}
			</div>
			<div className="flex justify-between">
				<button
					type="submit"
					className="w-40 btn btn-primary"
				>
					Create Todo
				</button>
			</div>
		</form>
  );
};

export default CreateTodoForm;
```

</details>


Since this form is rendered dynamically in the client side, invoking `createNewTodo()` from the form gives access to the `createTodo()` server action -- which in turn invokes `db.insert()` in the serverside.

In a similar manner, `deleteTodo()` must be invoked from a button in a component that is rendered explicitly with the `"use client"` directive.


## The Demo DrizzleNext.jsTodoApp

Please feel free to examine the demo app code [here](https://github.com/app-generator/docs-nextjs-drizzle-orm). For all things Drizzle, explore the docs [here](https://orm.drizzle.team/docs/overview).
