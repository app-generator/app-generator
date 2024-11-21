
:og:description: Next.js Charts with Recharts - A Useful Guide

.. title::  Next.js Charts with Recharts - A Useful Guide
.. meta::
    :description: Learn how to use Recharts in Next.Js by building a dashboard application
    :keywords: next.js charts, recharts in next.js, next.js charts tutorial, recharts tutorial


Next.js Charts with Recharts
============================

This is a useful guide on building Next.js charts with the Recharts library. We cover some common Recharts charts typical of dashboards and other React based data visualization applications and provide tips to address quirks particular to Next.js app router components.


Introduction
------------

`Recharts <https://recharts.org/en-US/guide/>`__ is a lightweight SVG based React charting library built on top of D3 submodules. Recharts offers composable React components for different kinds of charts and their sibling/sub components. As such, Recharts helps quickly build different types of charts typical of dashboards, admin panels and other data visualization applications.

In this guide, we consider building a Next.js dashboard with Recharts charts. While doing so, we explain the use of ``<PieChart />``, ``<LineChart />``, ``<AreaChart />`` and ``<BarChart />`` wrapper types and their necessary parent, sibling and child components. With examples of both server and client side data fetching, we explain a few ways how Recharts charts can be rendered in client rendered Next.js components.

.. include::  /_templates/components/banner-top.rst


Pre-requisites
--------------

This guide is intended for Next.js developers. So, we assume, you're building stuff with Next.js. We're using `TailwindCSS <https://tailwindcss.com/docs/installation>`__ and `daisyUI <https://daisyui.com/docs/install/>`__ for the UI, so we expect you're somewhat familiar with TailwindCSS classes.

We're also using TypeScript for the demo app. However, you can follow along without TypeScript.


A Next.js Dashboard with Recharts
---------------------------------

For the app, start a Next.js application with app router and TailwindCSS. You can name your app ``nextjs-recharts`` or similar.  So, in your terminal start with:

..	code-block:: bash

		npx create-next-app@latest

And choose a configuration similar to the following: ::

	✔ What is your project named? … nextjs-recharts
	✔ Would you like to use TypeScript? … Yes
	✔ Would you like to use ESLint? … Yes
	✔ Would you like to use Tailwind CSS? … Yes
	✔ Would you like your code inside a `src/` directory? … Yes
	✔ Would you like to use App Router? (recommended) … Yes
	✔ Would you like to use Turbopack for next dev? … No
	✔ Would you like to customize the import alias (@/* by default)? … Yes
	✔ What import alias would you like configured? … @nextjs-recharts/*

Once initialization completes, run the application with:

..	code-block:: bash

		npm run dev

This should have the app running on: ``http://localhost:3000/``


Set Up A Demo Database with JSON Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We need to set up a demo database that emulates REST endpoints to serve data for our dashboard. For that, we'll use `JSON Server <https://github.com/typicode/json-server>`__.

Follow these steps in order to set up a db with JSON Server:

1. Install ``json-server`` with the following ``npm`` command:

..	code-block:: bash

		npm i json-server

2. Set up ``npm`` script to run the ``json-server`` at ``--port 3210``. So, add this script under ``"scripts": {}``:

..	code-block::

		"scripts": {
			"db:json-server": "npx json-server db.json --port 3210"
		}

3. Seed the JSON Server database with data.

Create a ``db.json`` file at the root of the application. Then just copy over the content of `this file over here <https://github.com/app-generator/docs-nextjs-and-recharts/blob/main/db.json>__`.

4. Run the JSON Server to serve dashboard data at ``http://localhost:3210``:

..	code-block:: bash

		npm run db:json-server


Install Recharts
~~~~~~~~~~~~~~~~

Recharts comes in a single package, without any dependency and configuration. Pretty easy to get started.

So, install Recharts with the following ``npm`` command:

..	code-block:: bash

    npm i recharts


Additional Packages
""""""""""""""""""""

We're using `Heroicons <https://github.com/tailwindlabs/heroicons?tab=readme-ov-file>`__ for icons and `date-fns <https://date-fns.org/docs/Getting-Started>`__ for some utlity functions. You would need them if you need to build your dashboard exactly like in the demo. So, go ahead and install them if you would. Refer to their docs if you need to.

These additional packages are not Recharts dependencies. You are free to use alternative solutions, and won't need these while following this guide. So, they are not covered here.


A Permanently Responsive Pie Chart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For our dashboard, we want to build a reusable responsive Pie chart with Recharts components. We need to use the ``<ResponsiveContainer />`` component as a container, and the ``<PieChart />`` wrapper to specify the chart type. And then pass data to pies inside one or more ``<Pie />`` components. As in the following ``<ResponsivePieChart />`` host component:

..  code-block::
    :emphasize-lines: 1,5,27-29,40-42

    "use client"

		import React, { useState } from "react";
		import { random255Max } from "@nextjs-recharts/app/utils";
		import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from "recharts";

		type TUserCountries = { country: string; count: number; };

		type TResponsivePieChartProps = { data: TUserCountries[]; total: number; };

		export const ResponsivePieChart = ({ data, total }: TResponsivePieChartProps) => {
			const [rad, setRad] = useState({ outerRad1: 70, innerRad: 74, outerRad2: 79, });

			return (
				<ResponsiveContainer
					className="w-full" aspect={1}
					onResize={(width) => setRad({
						outerRad1: 3 * width / 10,
						innerRad: 3 * width / 10 + 4,
						outerRad2: 3 * width / 10 + 8,
					})}
				>
					<PieChart
						className="w-full"
					>
						<Pie
							data={data} dataKey={"count"} nameKey={"country"}
							cx="50%" cy="50%"
							outerRadius={rad?.outerRad1}
							fill="#8884d8" label={{ fontSize: "12px", fontStyle: "bold" }}
						>
							{data?.map((entry: TUserCountries, index: number) => (
								<Cell
									key={`cell-${index}`}
									fill={`rgb(${random255Max()}, ${random255Max()}, ${random255Max()})`}
								/>
							))}
						</Pie>
						<Pie
							data={[{ total }]} dataKey={"total"}
							cx="50%" cy="50%"
							innerRadius={rad?.innerRad} outerRadius={rad?.outerRad2}
							fill="orange"
						/>
						<Tooltip
							itemStyle={{ padding: "2px 4px", fontStyle: "bold" }}
							wrapperStyle={{ padding: "2px 4px" }}
							contentStyle={{ padding: "2px 4px", fontSize: "12px" }}
						/>
					</PieChart>
				</ResponsiveContainer>
			);
		};

Let's break down what Rechart is doing in the above component.


Recharts ``<ResponsiveContainer />`` Component
""""""""""""""""""""""""""""""""""""""""""""""

``<ResponsiveContainer />`` is the parent of all Rechart charts. We have to use it to house any charts such as ``<PieChart />``, ``<LineChart />``, ``<AreaChart />`` and ``<BarChart />``.

It adds necessary spatial flexibility and Rechart's CSS responsiveness to otherwise rigid D3 charts. We can set ``width`` and ``height`` of the container with fixed or percentage values. We can also use CSS classes, such as a TailwindCSS class, to set the width of the container.

..	code-block::

		<ResponsiveContainer
			className="w-full"
			aspect={1}
			onResize={(width) => setRad({
				// do something responsive
			})}
		>
		...
		</ResponsiveContainer>


Feel free to checkout `the <ResponsiveContainer /> docs here <https://recharts.org/en-US/api/ResponsiveContainer>`__.

``aspect`` and ``onResize`` props are what makes ``<ResponsiveContainer />`` a worthy component. We can use these two props to make pie chart permanently responsive. More on this in `this later section <#making-the-pie-chart-permanently-responsive>`__.


Recharts ``<PieChart />`` Component
"""""""""""""""""""""""""""""""""""

In the case of a pie chart, have to wrap chart contents with the ``<PieChart />`` component. A ``Pie />`` component won't work without the ``<PieChart />`` wrapper. This is because, it contains the necessary logic for conveying pie chart data to feed tooltips and labels. Wrappers like ``<PieChart />`` are also useful for adding interactions on mouse events. In our case, we are just passing the width inherited by ``<PieChart />`` to its contents:

..	code-block::
		:emphasize-lines: 2

		<PieChart
			className="w-full"
		>
		...
		</PieChart>


Recharts ``<Pie />`` Component
""""""""""""""""""""""""""""""

In order to draw a pie, we have to place a ``<Pie />`` component inside a ``<PieChart />`` component. ``<Pie />`` accepts the chart data with the ``data`` prop. And we have to pass the ``dataKey`` for Recharts to draw slices from the data:

..	code-block::
		:emphasize-lines: 2

		<Pie
			data={data} dataKey={"count"} nameKey={"country"}
			cx="50%" cy="50%"
			outerRadius={rad?.outerRad1}
			fill="#8884d8" label={{ fontSize: "12px", fontStyle: "bold" }}
		>
			{data?.map((entry: TUserCountries, index: number) => (
				<Cell
					key={`cell-${index}`}
					fill={`rgb(${random255Max()}, ${random255Max()}, ${random255Max()})`}
				/>
			))}
		</Pie>

We can add a ``nameKey`` which is used by ``<Pie />`` internally for generating tooltip texts and section labels. ``cx`` and ``cy`` are SVG values, which use to set the position of the pie.
We can customize the pie radius with ``outerRadius``. In our case, we have a responsive value ``rad?.outerRad1``, which is generatd based on the screen width.

Recharts ``<Cell />`` Component
"""""""""""""""""""""""""""""""

We can use the ``<Cell />`` component to apply deep customizations to the pie. For example, with the following, we are applying a random color to each slice of the pie:

..	code-block::
		:emphasize-lines: 4

		{data?.map((entry: TUserCountries, index: number) => (
			<Cell
				key={`cell-${index}`}
				fill={`rgb(${random255Max()}, ${random255Max()}, ${random255Max()})`}
			/>
		))}

We can build the pie without using the ``<Cell />`` component. In that case, a default pie is built.


Recharts ``<Tooltip />`` Component
""""""""""""""""""""""""""""""""""

We can use the ``<Tooltip />`` component in order to display interactive tooltips to the chart. The ``<Tooltip />`` component automatically infers data passed to a sibling ``<Pie />`` thanks to the chart type wrapper: the parent ``<PieChart />``. It then displays relevant data when a section is hovered over.

The ``<Tooltip />`` component must be a sibling to the chart component and child to the chart type wrapper:

..	code-block::
		:emphasize-lines: 3-7

		<PieChart>
			<Pie></Pie>
			<Tooltip
				itemStyle={{ padding: "2px 4px", fontStyle: "bold" }}
				wrapperStyle={{ padding: "2px 4px" }}
				contentStyle={{ padding: "2px 4px", fontSize: "12px" }}
			/>
		</PieChart>


We can customize the ``<Tooltip />`` with style props, animation behavior, and even build our own. Please check the detailed docs `here <https://recharts.org/en-US/api/Tooltip>`__.


Making the Pie Chart Permanently Responsive
""""""""""""""""""""""""""""""""""""""""""""""""""

The ``outerRadius`` and ``innerRadius`` props on ``<Pie />`` are D3 props, which makes them fixed to a value. In order to make a pie permanently flexible, we can reset these radiuses when the browser changes it's width. For that, we can use ``onResize`` prop on ``<ResponsiveContainer />`` to track the screen width with a React state and then update the ``outerRadius``, ``innerRadius`` of ``<Pie />``. For example:

..	code-block::
		:emphasize-lines: 1,4,9,10-14,22

		import React, { useState } from "react";

		export const ResponsivePieChart = ({ data, total }: TResponsivePieChartProps) => {
			const [rad, setRad] = useState({ outerRad1: 70, innerRad: 74, outerRad2: 79, });

			return (
				<ResponsiveContainer
					className="w-full"
					aspect={1}
					onResize={(width) => setRad({
						outerRad1: 3 * width / 10,
						innerRad: 3 * width / 10 + 4,
						outerRad2: 3 * width / 10 + 8,
					})}
				>
					<PieChart
						className="w-full"
					>
						<Pie
							data={[{ total }]} dataKey={"total"}
							cx="50%" cy="50%"
							innerRadius={rad?.innerRad} outerRadius={rad?.outerRad2}
							fill="orange"
						/>
					</PieChart>
				</ResponsiveContainer>
			);
		};


The ``onResize`` prop on ``<ResponsiveContainer />`` gives us access to its ``width`` and ``height`` via a callback. So, here, we access them to set a local ``rad`` state and then use the value to update the ``innerRadius`` and ``outerRadius`` values on ``<Pie />``.

One caveat of ``onResize`` is we have to set/inherit both the ``width`` and ``height`` values: either to fixed values or be evaluated with the ``aspect`` prop. Otherwise, the dimensions break. Here, we are using a combination of width set by TailwindCSS ``w-full`` class and ``aspect``.


Rechart Charts Must Be Client Rendered
""""""""""""""""""""""""""""""""""""""

Notice, we have used the ``"use client"`` directive at the top. We have to make Rechart chart components render client side for obvious reasons. We need charts to be interactive and for many cases dynamic. And Recharts charts are dynamic with customizable interactions and animations.

If we don't make the host component render client side explicitly with the ``"use client"`` directive, we get this typical client TypeError:

..	code-block::

	TypeError: Super expression must either be null or a function


Recharts: Commonly Used Chart Types
-----------------------------------

Recharts has wrappers for different types of charts. We already covered ``<PieChart />``. Other types are the ``<LineChart />`` for facilitating line charts, ``<AreaChart />`` to house area charts and ``<BarChart />`` to build bars. Chart type wrappers are crucial for conveying and optimizing data to applicable sibling components such as ``<Tooltip />``, ``<XAxis />``, ``<YAxis />``, ``<Legend />``, etc.

In the following sections, we focus on commonly used chart types, with their type wrappers and sibling components.


Recharts Line Charts
~~~~~~~~~~~~~~~~~~~~

We plot a line chart with the ``<Line />`` component housed inside the ``<LineChart />`` wrapper. For the grid, we use the ``<CartesianGrid />``, ``<XAxis />``, ``<YAxis />`` components. We use the general purpose ``<Tooltip />`` and ``<Legend />`` components for providing data tips. We can also use a ``<ReferenceLine />`` to plot fixed lines of reference.

For our dashboard, we have a ``<ResponsiveLineChart />`` host component that looks like below:

..	code-block::
		:emphasize-lines: 5-6,17-20,30,31-35

		"use client"

		import React from "react";
		import {
			Line, LineChart, CartesianGrid, Legend, ResponsiveContainer,
			Tooltip, XAxis, YAxis, Label, ReferenceLine
		} from "recharts";

		type TDailyData = { date: string; count: string; };
		type TResponsiveLineChartProps = { data: TDailyData[]; };

		export const ResponsiveLineChart = ({ data }: TResponsiveLineChartProps) => {
			const tooltipStyle = { padding: "2px", fontSize: "10px" }

			return (
				<ResponsiveContainer className="w-full" height={335} >
					<LineChart
						className="w-full" height={200}
						data={data}
					>
						<CartesianGrid strokeDasharray="4,2"/>
						<XAxis
							height={49} dataKey="date" style={{ fontSize: "12px" }}
							label={{value: "Date", position: "insideBottom", fontSize: "14px"}}
						/>
						<YAxis
							width={49} dataKey="count" style={{ fontSize: "12px" }}
							label={{ value: "Prospects count", position: "insideLeft", fontSize: "14px", angle: "-90" }}
						/>
						<Line type="monotone" dataKey="count" stroke="#164e63" strokeWidth={2} opacity={0.6} />
						<ReferenceLine y="15" stroke="orange" strokeWidth={2} strokeDasharray="4,3" >
							<Label className="text-sm" position="insideBottomRight">
								Daily target
							</Label>
						</ReferenceLine>
						<Tooltip itemStyle={tooltipStyle} contentStyle={tooltipStyle} />
						<Legend verticalAlign="top" color="#164e63" />
					</LineChart>
				</ResponsiveContainer>
			);
		};


The most relevant components involved in a line chart are the ``<LineChart />`` and ``<Line />`` components.


Recharts ``<LineChart />`` Component
""""""""""""""""""""""""""""""""""""

The ``<LineChart />`` component is the Recharts wrapper for a line chart. Unlike the ``<PieChart />`` wrapper, ``<LineChart />`` accepts the ``data`` props, alongside a few other props such as ``width`` and ``height``:

..	code-block::
		:emphasize-lines: 3

		<LineChart
			className="w-full" height={200}
			data={data}
		>
		...
		</LineChart>

``<LineChart />`` avails the data to the ``<Line />`` component.


Recharts ``<Line />`` Component
"""""""""""""""""""""""""""""""

The ``<Line />`` component, unlike the ``<Pie />`` component we saw before, does not accept ``data``. It is used purely for plotting and decorating the chart line based on the ``data`` the availed to it by ``<LineChart />``:

..	code-block::
		:emphasize-lines: 3

		<Line
			type="monotone"
			dataKey="count"
			stroke="#164e63"
			strokeWidth={2}
			opacity={0.6}
		/>

Notice we have to set the ``dataKey`` prop to the name of the property on our data object, which we wish to plot our line with. In this case, the ``count`` property from the data object.


Recharts ``<ReferenceLine />`` Component
""""""""""""""""""""""""""""""""""""""""

An important sibling component to ``<Line />`` is the Recharts ``<ReferenceLine />`` component. ``<ReferenceLine />`` is handy for plotting reference lines in either axes of the chart. In our case, we have a reference line on the y-axis that shows the ``Daily target`` of prospects:

..	code-block::

		<ReferenceLine y="15" stroke="orange" strokeWidth={2} strokeDasharray="4,3" >
			<Label className="text-sm" position="insideBottomRight">
				Daily target
			</Label>
		</ReferenceLine>


Recharts General Purpose Components
"""""""""""""""""""""""""""""""""""

Recharts' essential general purpose chart area components are `<CartesianGrid /> <https://recharts.org/en-US/api/CartesianGrid>`__, `<XAxis /> <https://recharts.org/en-US/api/XAxis>`__, `<YAxis /> <https://recharts.org/en-US/api/YAxis>`__ and `<Legend /> <https://recharts.org/en-US/api/Legend>`__. They are pretty intuitive to use, and feel free to visit their respective documentations in case you need to.


Recharts Labels
"""""""""""""""

Recharts offers labels on different parts of the chart. We can apply a label on ``<Pie />``, ``<XAxis />``, ``<YAxis />``, ``<ReferenceLine />``, ``<ReferenceArea />`` and others. There are different ways of setting labels where needed. We can use a ``Boolean`` value to the ``label`` prop on an applicable component, we can use an object syntax, or we can use the ``<Label />`` component for finer customizations.

In our ``<ResponsiveLineChart />``, we used the object syntax to label ``<XAxis />`` and ``<YAxis />``:

..	code-block::

		<XAxis
			label={{value: "Date", position: "insideBottom", fontSize: "14px"}}
		>

And also the component form to label ``<ReferenceLine />``:

..	code-block::

		<Label className="text-sm" position="insideBottomRight">
			Daily target
		</Label>

You'd be especially interested in how different label ``position`` s are relevant, be it along an axis or inside the chart grid.


Recharts Area Charts
~~~~~~~~~~~~~~~~~~~~

We have to use the ``<AreaChart />`` wrapper in order to build an area chart with Recharts. The ``<AreaChart />`` component uses the ``<Area />`` child component to plot the area. It also uses general purpose components such as the ``<CartesianGrid />``, ``<XAxis />`` and ``<YAxis />``, etc. as siblings to ``<Area />``.

In our dashboard, we have a host area chart named ``<ResponsiveAreaChart />`` implemented like this:

..	code-block::
		:emphasize-lines: 5-6,18-22,32-35,38

		"use client"

		import React from "react";
		import {
			Area, AreaChart, CartesianGrid, Legend, ResponsiveContainer,
			Tooltip, XAxis, YAxis,
		} from "recharts";

		import { TDailyData } from "./ResponsiveLineChart";

		type TResponsiveAreaChartProps = { data: TDailyData[]; };

		export const ResponsiveAreaChart = ({ data }: TResponsiveAreaChartProps) => {
			const tooltipStyle = { padding: "2px", fontSize: "10px" }

			return (
				<ResponsiveContainer className="w-full" height={335} >
					<AreaChart
						data={data}
						className="w-full"
						height={200}
					>
						<CartesianGrid strokeDasharray="4,2"/>
						<XAxis
							height={49} dataKey="date" style={{ fontSize: "12px" }}
							label={{ value: "Date", position: "insideBottom", fontSize: "14px" }}
						/>
						<YAxis
							width={49} dataKey="count" style={{ fontSize: "12px" }}
							label={{ value: "Customers count", position: "insideLeft", fontSize: "14px", angle: "-90" }}
						/>
						<Area
							dataKey="count"
							type="monotone" stroke="#134e4a" fill="#a7f3d0" strokeWidth={2} opacity={0.6}
						/>
						<Tooltip itemStyle={tooltipStyle} contentStyle={tooltipStyle}/>
						<Legend verticalAlign="top" color="#134e4a"/>
					</AreaChart>
				</ResponsiveContainer>
			);
		};


As with the ``<LineChart />`` wrapper, ``<AreaChart />`` accepts the chart ``data`` for plotting. ``<Area />`` has to specify the ``dataKey`` with the property name from the data object, whose value should be plotted. Other props on ``<Area />`` such as ``type: "monotone"``, ``fill`` and ``stroke`` are used for configuration and decoration.



Data Fetching and Recharts in Next.js
-------------------------------------

Recharts charts have to remain strictly rendered in the client side. We have already seen that we need to make all Recharts chart host components render client side with the ``"use client"`` directive.

As such, the data needed to feed Recharts charts can be availed to them in two ways:

1. By fetching data server side and then passing to a host client component that houses the chart.
2. Fetching data client side from the chart host component.


Feeding Recharts Charts with Server Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can fetch data server side with Next.js server actions and then pass it to the chart host component. For example, in our dashboard app, we have a ``getUserCountriesData()`` server action that fetches data from a ``/userCountries`` endpoint:

..	code-block::
		:emphasize-lines: 1

		"use server"

		export const getUserCountriesData = async () => {
			const response = await fetch("http://localhost:3210/userCountries");
			if (response.status === 200) return response.json();
		};


We can use similar server actions to pass data to other chart host components in order to feed Recharts charts.


Fetching Recharts Data Client Side From Host Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, we can fetch and memoize data from inside a client component that hosts the chart. As an example, we have a bar chart named ``<ResponsiveBarChart />`` that uses the ``<BarChart />`` component to plot ``leads`` data. It fetches data from inside the chart host using the JavaScript ``fetch()`` API, stores it an a local state, memoizes it and passes it on to ``BarChart />``:

..	code-block::
		:emphasize-lines: 6-7,13-14,16-25,29,39-44,46

		"use client"

		import { useMemoizedChartData } from "@nextjs-recharts/app/utils";
		import React, { useEffect, useState } from "react";
		import {
			Bar, BarChart, CartesianGrid, Legend,
			ResponsiveContainer, XAxis, YAxis,
		} from "recharts";

		type TLeads = { date: string; count: number; };

		export const ResponsiveBarChart = () => {
			const [leadsData, setLeadsData] = useState([]);
			const memoizedLeadsData = useMemoizedChartData(leadsData);

			useEffect(() => {
				fetch("http://localhost:3210/dailyData")
					.then(async (response) => {
						if (response.status === 200) {
							const data = await response.json();
							setLeadsData(data?.leads?.data);
						}
					}
				);
			}, []);

			return (
				<ResponsiveContainer height={335}>
					<BarChart width={200} height={200} data={memoizedLeadsData as TLeads[]} >
						<CartesianGrid strokeDasharray="4,2" />
						<XAxis
							height={49} dataKey="date" style={{ fontSize: "12px" }}
							label={{ value: "Date", position: "insideBottom", fontSize: "14px" }}
						/>
						<YAxis
							width={49} dataKey="count" style={{ fontSize: "12px" }}
							label={{ value: "Leads count", position: "insideLeft", fontSize: "14px", angle: "-90" }}
						/>
						<Bar
							dataKey="count"
							fill="#7c2d12" opacity={0.6}
							label={{ position: "top", fill: "orange", fontSize: "12px", fontStyle: "bold" }}
							barSize={30} maxBarSize={39}
						/>
						<Legend verticalAlign="top" color="#7c2d12"/>
					</BarChart>
				</ResponsiveContainer>
			);
		};


We can use any client side library like ``axios``, ``RTK Query`` or ``SWR`` for fetching data client side for Recharts.

Client side data fetching is specially useful when the chart or the host component is interactive, and in particular the interaction dynamically impacts the data being plotted.


Recharts Demo Dashboard App
--------------------------------------

For details on the above code snippets, examine the demo dashboard app available in `this repository <https://github.com/app-generator/docs-nextjs-and-recharts>`__. Feel free to clone and run a local copy to see the demo dashboard app in action. Further instructions on the `README.md <https://github.com/app-generator/docs-nextjs-and-recharts/blob/main/README.md>`__ file.


.. include::  /_templates/components/footer-links.rst
