:og:description: Python - Resources for students and developers | App-Generator.dev

Python
======

.. title:: Python - Resources for students and developers | App-Generator.dev
.. meta::
    :description: Unified index for Python resources: tutorials, templates and full-stack starters

Python is a high-level, interpreted programming language known for its readability and simplicity. 
Created by Guido van Rossum and first released in 1991, Python has become one of the most popular programming languages in the world for beginners and professionals alike.

.. include::  /_templates/components/banner-top.rst

Why Learn Python?
-----------------

- **Easy to learn**: Clear, readable syntax with minimal punctuation
- **Versatile**: Used in web development, data science, AI, automation, and more
- **Huge community**: Extensive libraries, frameworks, and support resources
- **In-demand skill**: Highly sought after in the job market

Your First Python Program
-------------------------

After installing Python from `python.org <https://python.org>`__, open a text editor and write:

.. code-block:: python

    print("Hello, World!")

Save this as `hello.py` and run it from your command line with:

.. code-block:: bash 

    python hello.py

Congratulations! You've written your first Python program.

Python Basics
-------------

Variables
*********

.. code-block:: python

    name = "Alex"
    age = 25
    is_student = True


Data Types
**********

- **Strings**: Text (`"Hello"`)
- **Integers**: Whole numbers (`42`)
- **Floats**: Decimal numbers (`3.14`)
- **Booleans**: True/False values
- **Lists**: Ordered collections (`[1, 2, 3]`)
- **Dictionaries**: Key-value pairs (`{"name": "Alex", "age": 25}`)

Control Flow
************

.. code-block:: python

    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

Loops
*****

.. code-block:: python

    # Print numbers 0-4
    for i in range(5):
        print(i)

    # Loop while a condition is true
    count = 0
    while count < 5:
        print(count)
        count += 1


Functions
*********

.. code-block:: python

    def greet(name):
        return f"Hello, {name}!"

    message = greet("Alex")
    print(message)  # Prints: Hello, Alex!


Next Steps
----------

- Practice with simple projects like calculators or text games
- Explore Python libraries for your interests (web, data, games)
- Join online communities (Reddit's r/learnpython, Stack Overflow)
- Work through tutorials on platforms like Codecademy, freeCodeCamp
   
Resources
---------

.. toctree::
   :maxdepth: 1
   
   python/index
   python/cheatsheet
