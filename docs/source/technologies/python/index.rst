:og:description: Getting Started with Python - Learn the Python basics, the practical way

Getting Started
===============

.. title:: Getting Started with Python - Learn the Python basics, the practical way
.. meta::
    :description: Complete Python tutorial that includes code samples, patterns and exteernal references
    :keywords: Python guide, getting started, python intro, Python tutorial, Python strings, loops in Python

Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It emphasizes code readability with its notable use of significant whitespace.

Python's design philosophy emphasizes code readability and a syntax that allows programmers to express concepts in fewer lines of code. 
This philosophy is summarized in "The Zen of Python" (accessible by typing `import this` in the Python interpreter).

.. include::  /_templates/components/banner-top.rst

Why Python?
-----------

- **Readability**: Clean syntax that's easy to learn and understand
- **Versatility**: Used in web development, data science, AI, automation, game development, and more
- **Large Community**: Extensive documentation, libraries, and support
- **Cross-platform**: Runs on Windows, macOS, Linux, and more
- **Free and Open Source**: Available to everyone at no cost

Setting Up Your Environment
---------------------------

Installing Python
*****************

Windows
^^^^^^^

1. Download the installer from [python.org](https://www.python.org/downloads/)
2. Run the installer (important: check "Add Python to PATH")
3. Verify installation by opening Command Prompt and typing:

.. code-block:: bash 

   python --version

MacOS
^^^^^

1. Install Homebrew (if not already installed) by following instructions at [brew.sh](https://brew.sh/)
2. Install Python using Homebrew:

.. code-block:: bash 

   brew install python
   python3 --version

Linux
^^^^^

Most Linux distributions come with Python pre-installed. If not:

.. code-block:: bash 

    sudo apt update
    sudo apt install python3 python3-pip

Setting Up a Code Editor
************************

Choose one of these popular options:

- **Visual Studio Code**: Free, lightweight, extensible
- **PyCharm**: Powerful IDE with free Community Edition
- **Jupyter Notebooks**: Great for data science and interactive coding
- **IDLE**: Comes bundled with Python, simple for beginners

Virtual Environments
********************

Virtual environments allow you to have isolated Python setups for different projects:

.. code-block:: bash 

    # Create a virtual environment
    python -m venv myenv

    # Activate it (Windows)
    myenv\Scripts\activate

    # Activate it (macOS/Linux)
    source myenv/bin/activate

    # Install packages within the environment
    pip install package_name


Python Basics
-------------

Hello, World!
*************

Create a file named `hello.py` with this content:

.. code-block:: python 

    print("Hello, World!")

Run it from the command line:

.. code-block:: bash

    python hello.py

Variables and Data Types
************************


Variable Assignment
^^^^^^^^^^^^^^^^^^^

.. code-block:: python 

    name = "John"
    age = 30
    height = 5.11
    is_student = False

Python is dynamically typed, meaning you don't declare the type explicitly.

Basic Data Types
^^^^^^^^^^^^^^^^

- **int**: Integer numbers (`42`, `-7`)
- **float**: Decimal numbers (`3.14`, `-0.001`)
- **str**: Text strings (`"Hello"`, `'Python'`)
- **bool**: Boolean values (`True`, `False`)
- **NoneType**: The `None` value representing absence of value

Type Conversion
^^^^^^^^^^^^^^^

.. code-block:: python 

    # String to integer
    age_str = "30"
    age = int(age_str)

    # Integer to string
    count = 42
    count_str = str(count)

    # String to float
    pi_str = "3.14159"
    pi = float(pi_str)

Basic Operations
****************

Arithmetic Operations
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python 

    # Addition
    sum = 5 + 3  # 8

    # Subtraction
    difference = 10 - 4  # 6

    # Multiplication
    product = 3 * 7  # 21

    # Division (returns float)
    quotient = 20 / 4  # 5.0

    # Floor Division (returns int)
    integer_quotient = 20 // 6  # 3

    # Modulus (remainder)
    remainder = 20 % 6  # 2

    # Exponentiation
    power = 2 ** 3  # 8

String Operations
^^^^^^^^^^^^^^^^^

.. code-block:: python 

    # Concatenation
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name  # "John Doe"

    # Repetition
    echo = "Echo " * 3  # "Echo Echo Echo "

    # Formatting
    message = f"Hello, {first_name}! You are {age} years old."

Comparison Operations
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python 

    x = 5
    y = 10

    x == y  # Equal to (False)
    x != y  # Not equal to (True)
    x < y   # Less than (True)
    x > y   # Greater than (False)
    x <= y  # Less than or equal to (True)
    x >= y  # Greater than or equal to (False)

Logical Operations
^^^^^^^^^^^^^^^^^^

.. code-block:: python 

    a = True
    b = False

    a and b  # Logical AND (False)
    a or b   # Logical OR (True)
    not a    # Logical NOT (False)

Data Structures
---------------

Lists
*****

Ordered, mutable collections of items:

.. code-block:: python 

    # Creating lists
    fruits = ["apple", "banana", "cherry"]
    mixed = [1, "hello", True, 3.14]

    # Accessing elements (zero-indexed)
    first_fruit = fruits[0]  # "apple"
    last_fruit = fruits[-1]  # "cherry"

    # Slicing
    subset = fruits[0:2]  # ["apple", "banana"]

    # Modifying
    fruits[1] = "orange"  # Replace "banana" with "orange"
    fruits.append("kiwi")  # Add to the end
    fruits.insert(1, "blueberry")  # Insert at index 1
    fruits.remove("cherry")  # Remove by value
    popped = fruits.pop()  # Remove and return the last item
    del fruits[0]  # Delete by index

    # List operations
    combined = fruits + ["mango", "pineapple"]  # Concatenation
    length = len(fruits)  # Get length
    sorted_fruits = sorted(fruits)  # Return sorted copy
    fruits.sort()  # Sort in place
    fruits.reverse()  # Reverse in place

Tuples
*******

Immutable ordered collections:

.. code-block:: python 

    # Creating tuples
    coordinates = (10.5, 20.8)
    person = ("John", 30, "Developer")

    # Accessing elements
    x_coord = coordinates[0]
    y_coord = coordinates[1]

    # Unpacking
    name, age, occupation = person

    # Single-element tuple (note the comma)
    singleton = (42,)

Dictionaries
************

Key-value pairs, unordered and mutable:

.. code-block:: python 

    # Creating dictionaries
    person = {
        "name": "John",
        "age": 30,
        "occupation": "Developer"
    }

    # Accessing values
    name = person["name"]  # Using key
    age = person.get("age")  # Using get() method (safer)

    # Adding/modifying
    person["email"] = "john@example.com"  # Add new key-value pair
    person["age"] = 31  # Modify existing value

    # Removing
    del person["occupation"]  # Remove by key
    email = person.pop("email")  # Remove and return value

    # Operations
    keys = person.keys()  # Get all keys
    values = person.values()  # Get all values
    items = person.items()  # Get all key-value pairs as tuples

Sets
*****

Unordered collections of unique elements:

.. code-block:: python 

    # Creating sets
    fruits = {"apple", "banana", "cherry"}
    numbers = set([1, 2, 3, 2, 1])  # Creates {1, 2, 3}

    # Operations
    fruits.add("orange")  # Add an element
    fruits.remove("banana")  # Remove an element
    fruits.discard("kiwi")  # Remove if present (no error if absent)

    # Set operations
    a = {1, 2, 3}
    b = {3, 4, 5}
    union = a | b  # {1, 2, 3, 4, 5}
    intersection = a & b  # {3}
    difference = a - b  # {1, 2}
    symmetric_difference = a ^ b  # {1, 2, 4, 5}

Control Flow
-------------

Conditional Statements
**********************

.. code-block:: python 

    # Simple if statement
    age = 20
    if age >= 18:
        print("You are an adult")

    # if-else statement
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

    # if-elif-else statement
    if age < 13:
        print("Child")
    elif age < 18:
        print("Teenager")
    elif age < 65:
        print("Adult")
    else:
        print("Senior")

    # Ternary operator (conditional expression)
    status = "adult" if age >= 18 else "minor"

Loops
*****

For Loops
^^^^^^^^^

.. code-block:: python 

    # Iterating over a sequence
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    # Using range
    for i in range(5):  # 0 to 4
        print(i)

    for i in range(2, 8):  # 2 to 7
        print(i)

    for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
        print(i)

    # Iterating over a dictionary
    person = {"name": "John", "age": 30}
    for key in person:
        print(f"{key}: {person[key]}")

    # Using items()
    for key, value in person.items():
        print(f"{key}: {value}")

    # Enumerate (get index and value)
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")

While Loops
^^^^^^^^^^^

.. code-block:: python 

    # Basic while loop
    count = 0
    while count < 5:
        print(count)
        count += 1

    # Breaking out of loops
    while True:
        user_input = input("Enter 'quit' to exit: ")
        if user_input == "quit":
            break
        print(f"You entered: {user_input}")

    # Continuing to next iteration
    for i in range(10):
        if i % 2 == 0:  # Skip even numbers
            continue
        print(i)  # Print odd numbers only

List Comprehensions
^^^^^^^^^^^^^^^^^^^

Concise way to create lists:

.. code-block:: python 

    # Create a list of squares
    squares = [x**2 for x in range(1, 11)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # With a condition
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]  # [4, 16, 36, 64, 100]

Functions
---------

Defining and Calling Functions
******************************

.. code-block:: python 

    # Basic function
    def greet(name):
        return f"Hello, {name}!"

    # Calling the function
    message = greet("John")
    print(message)  # Hello, John!

    # Function with multiple parameters
    def calculate_total(price, tax_rate, discount=0):
        tax = price * tax_rate
        discounted_price = price - discount
        return discounted_price + tax

    total = calculate_total(100, 0.08, 10)  # 98.0

Parameters
**********

.. code-block:: python 

    # Default parameters
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    print(greet("John"))  # Hello, John!
    print(greet("John", "Hi"))  # Hi, John!

    # Keyword arguments
    def create_profile(name, age, occupation):
        return f"{name} is {age} years old and works as a {occupation}."

    profile = create_profile(age=30, name="John", occupation="developer")

    # Variable number of arguments
    def sum_all(*numbers):
        total = 0
        for num in numbers:
            total += num
        return total

    result = sum_all(1, 2, 3, 4, 5)  # 15

    # Variable number of keyword arguments
    def build_person(**attributes):
        return attributes

    person = build_person(name="John", age=30, occupation="developer")


Lambda Functions
****************

Anonymous, single-expression functions:

.. code-block:: python 

    # Regular function
    def square(x):
        return x**2

    # Equivalent lambda function
    square_lambda = lambda x: x**2

    # Using with map
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

    # Using with filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]


Modules and Packages
--------------------

Importing Modules
*****************

.. code-block:: python 

    # Import an entire module
    import math
    radius = 5
    area = math.pi * math.pow(radius, 2)

    # Import specific items
    from math import pi, sqrt
    area = pi * radius**2
    diagonal = sqrt(2)

    # Import with alias
    import math as m
    area = m.pi * m.pow(radius, 2)

    # Import all (not recommended for large modules)
    from math import *
    area = pi * pow(radius, 2)


Creating Your Own Modules
**************************

1. Create a file `my_module.py`:

.. code-block:: python 

    # my_module.py
    def greet(name):
        return f"Hello, {name}!"

    PI = 3.14159

2. Import and use it:

.. code-block:: python 

    import my_module

    message = my_module.greet("John")
    area = my_module.PI * radius**2

Packages
********

Packages are directories containing multiple modules.

1. Create a directory structure:

.. code-block:: bash

    my_package/
    ├── __init__.py
    ├── module1.py
    └── module2.py

2. Import from the package:

.. code-block:: python 

    import my_package.module1
    from my_package import module2
    from my_package.module1 import some_function

Virtual Environments and pip
****************************

.. code-block:: python 

    # Create a virtual environment
    python -m venv myenv

    # Activate it
    # Windows:
    myenv\Scripts\activate
    # macOS/Linux:
    source myenv/bin/activate

    # Install packages
    pip install numpy pandas matplotlib

    # List installed packages
    pip list

    # Create requirements file
    pip freeze > requirements.txt

    # Install from requirements
    pip install -r requirements.txt

File Handling
-------------

Reading and Writing Text Files
******************************

.. code-block:: python 

    # Writing to a file
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.")

    # Reading from a file
    with open("example.txt", "r") as file:
        content = file.read()  # Read entire file
        print(content)

    # Reading line by line
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() removes trailing newline

    # Appending to a file
    with open("example.txt", "a") as file:
        file.write("\nThis line is appended.")


Working with CSV Files
**********************

.. code-block:: python 

    import csv

    # Writing CSV
    data = [
        ["Name", "Age", "Occupation"],
        ["John", 30, "Developer"],
        ["Alice", 25, "Designer"]
    ]

    with open("people.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    # Reading CSV
    with open("people.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    # Using DictReader and DictWriter
    people = [
        {"Name": "John", "Age": 30, "Occupation": "Developer"},
        {"Name": "Alice", "Age": 25, "Occupation": "Designer"}
    ]

    with open("people_dict.csv", "w", newline="") as file:
        fieldnames = ["Name", "Age", "Occupation"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(people)

    with open("people_dict.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Name']} is {row['Age']} years old.")

Working with JSON
*****************

.. code-block:: python 

    import json

    # Python object to JSON string
    person = {
        "name": "John",
        "age": 30,
        "occupation": "Developer",
        "languages": ["Python", "JavaScript", "SQL"]
    }

    json_string = json.dumps(person, indent=4)
    print(json_string)

    # Writing JSON to a file
    with open("person.json", "w") as file:
        json.dump(person, file, indent=4)

    # Reading JSON from a file
    with open("person.json", "r") as file:
        loaded_person = json.load(file)
        print(loaded_person["name"])  # John

    # JSON string to Python object
    json_string = '{"name": "Alice", "age": 25}'
    parsed_person = json.loads(json_string)
    print(parsed_person["name"])  # Alice

Error Handling
--------------

Try-Except Blocks
*****************

.. code-block:: python 

    # Basic try-except
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"Result: {result}")
    except ValueError:
        print("That's not a valid number!")
    except ZeroDivisionError:
        print("You can't divide by zero!")

    # Handling multiple exceptions with one block
    try:
        # Code that might raise an exception
        pass
    except (ValueError, TypeError) as error:
        print(f"An error occurred: {error}")

    # Using else and finally
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ValueError:
        print("Invalid input!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        # Runs if no exceptions were raised
        print(f"Result: {result}")
    finally:
        # Always runs, regardless of exceptions
        print("Operation completed.")

Raising Exceptions
******************

.. code-block:: python 

    def calculate_total(price, quantity):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        return price * quantity

    try:
        total = calculate_total(-10, 5)
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")

Custom Exceptions
*****************

.. code-block:: python 

    class InsufficientFundsError(Exception):
        """Raised when a withdrawal would result in a negative balance."""
        pass

    class BankAccount:
        def __init__(self, balance=0):
            self.balance = balance
            
        def withdraw(self, amount):
            if amount > self.balance:
                raise InsufficientFundsError(f"Not enough funds: balance is {self.balance}, tried to withdraw {amount}")
            self.balance -= amount
            return self.balance

    try:
        account = BankAccount(100)
        account.withdraw(150)
    except InsufficientFundsError as error:
        print(f"Transaction failed: {error}")


Object-Oriented Programming
---------------------------

Classes and Objects
*******************

.. code-block:: python 

    class Person:
        # Class attribute
        species = "Homo sapiens"
        
        # Constructor
        def __init__(self, name, age):
            # Instance attributes
            self.name = name
            self.age = age
        
        # Instance method
        def greet(self):
            return f"Hello, my name is {self.name}"
        
        def celebrate_birthday(self):
            self.age += 1
            return f"{self.name} is now {self.age} years old"

    # Creating objects
    john = Person("John", 30)
    alice = Person("Alice", 25)

    # Accessing attributes
    print(john.name)  # John
    print(john.species)  # Homo sapiens

    # Calling methods
    print(john.greet())  # Hello, my name is John
    print(john.celebrate_birthday())  # John is now 31 years old

Inheritance
***********

.. code-block:: python 

    class Employee(Person):
        def __init__(self, name, age, employee_id, salary):
            # Call the parent class constructor
            super().__init__(name, age)
            self.employee_id = employee_id
            self.salary = salary
        
        def calculate_yearly_salary(self):
            return self.salary * 12
        
        # Override the greet method
        def greet(self):
            return f"Hello, I'm {self.name}, employee #{self.employee_id}"

    # Create an Employee object
    employee = Employee("Jane", 28, "E12345", 5000)
    print(employee.greet())  # Hello, I'm Jane, employee #E12345
    print(employee.calculate_yearly_salary())  # 60000

Encapsulation
*************

.. code-block:: python 

    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.__balance = balance  # Private attribute
        
        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                return True
            return False
        
        def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                return True
            return False
        
        def get_balance(self):
            return self.__balance

    account = BankAccount("John", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(account.get_balance())  # 1300
    # print(account.__balance)  # Would raise AttributeError

Polymorphism
************

.. code-block:: python 

    class Animal:
        def make_sound(self):
            pass

    class Dog(Animal):
        def make_sound(self):
            return "Woof!"

    class Cat(Animal):
        def make_sound(self):
            return "Meow!"

    class Duck(Animal):
        def make_sound(self):
            return "Quack!"

    def animal_sound(animal):
        return animal.make_sound()

    dog = Dog()
    cat = Cat()
    duck = Duck()

    print(animal_sound(dog))  # Woof!
    print(animal_sound(cat))  # Meow!
    print(animal_sound(duck))  # Quack!


Magic Methods (Dunder Methods)
******************************

.. code-block:: python 

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def area(self):
            return self.width * self.height
        
        def __str__(self):
            return f"Rectangle({self.width}x{self.height})"
        
        def __repr__(self):
            return f"Rectangle(width={self.width}, height={self.height})"
        
        def __eq__(self, other):
            if not isinstance(other, Rectangle):
                return False
            return self.width == other.width and self.height == other.height
        
        def __add__(self, other):
            if isinstance(other, Rectangle):
                return Rectangle(self.width + other.width, self.height + other.height)
            return NotImplemented

    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)

    print(rect1)  # Rectangle(5x10)
    print(rect1 == Rectangle(5, 10))  # True
    rect3 = rect1 + rect2
    print(rect3)  # Rectangle(8x17)


Python Standard Library
-----------------------

The Python Standard Library contains a wide range of modules for various tasks. Here are some key ones:

os and sys
**********

.. code-block:: python 

    import os
    import sys

    # Current working directory
    print(os.getcwd())

    # List directory contents
    print(os.listdir())

    # Create and remove directories
    os.mkdir("new_directory")
    os.rmdir("new_directory")

    # Path manipulation
    filepath = os.path.join("data", "file.txt")

    # Environment variables
    home = os.environ.get("HOME")

    # Command line arguments
    arguments = sys.argv

    # Python version
    print(sys.version)

datetime
********

.. code-block:: python 

    from datetime import datetime, date, timedelta

    # Current date and time
    now = datetime.now()
    print(now)

    # Specific date
    birthday = date(1990, 5, 15)
    print(birthday)

    # Date operations
    tomorrow = date.today() + timedelta(days=1)
    print(tomorrow)

    # Formatting
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)

    # Parsing
    date_string = "2023-05-15 14:30:00"
    parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print(parsed_date)

random
******

.. code-block:: python 

    import random

    # Random integer
    num = random.randint(1, 100)

    # Random choice from a sequence
    colors = ["red", "green", "blue", "yellow"]
    color = random.choice(colors)

    # Random sample without replacement
    sample = random.sample(range(1, 50), 6)  # Lottery numbers

    # Shuffle a list in place
    random.shuffle(colors)

    # Random float in [0.0, 1.0)
    float_num = random.random()

collections
***********

.. code-block:: python 

    from collections import Counter, defaultdict, deque, namedtuple

    # Counter
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_counts = Counter(words)
    print(word_counts)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})
    print(word_counts.most_common(2))  # [('apple', 3), ('banana', 2)]

    # defaultdict
    fruit_colors = defaultdict(list)
    fruit_colors["red"].append("apple")
    fruit_colors["yellow"].append("banana")
    print(fruit_colors)  # defaultdict(<class 'list'>, {'red': ['apple'], 'yellow': ['banana']})

    # deque (efficient stack/queue)
    queue = deque()
    queue.append("first")
    queue.append("second")
    print(queue.popleft())  # first

    # namedtuple
    Point = namedtuple("Point", ["x", "y"])
    p = Point(1, 2)
    print(p.x, p.y)  # 1 2


re (Regular Expressions)
*************************

.. code-block:: python 

    import re

    text = "Contact us at info@example.com or support@company.org"

    # Find all email addresses
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    print(emails)  # ['info@example.com', 'support@company.org']

    # Replace
    new_text = re.sub(r'example\.com', 'example.net', text)
    print(new_text)  # Contact us at info@example.net or support@company.org

    # Match
    phone = "123-456-7890"
    if re.match(r'\d{3}-\d{3}-\d{4}', phone):
        print("Valid phone number format")

A Final Word
------------

Remember: The best way to learn programming is by writing code. 
Start with small projects and gradually tackle more complex ones. Don't be afraid to make mistakes—they're an essential part of the learning process!

Programming is a journey, not a destination. Every experienced developer was once a beginner, struggling with the same concepts you might find challenging today. 
What sets successful programmers apart isn't innate talent, but persistence and curiosity.

As you continue with Python, you'll discover that it's more than just a programming language—it's a vibrant community of people helping each other grow. 
When you face obstacles (and you will!), remember that millions of others have walked this path before you and are willing to help.

Your first programs might be simple, perhaps even clumsy, but they represent important steps in your development. Celebrate these small victories. 
With each line of code you write, you're building not just programs, but problem-solving skills that will serve you in countless ways.

The world needs more people who can code thoughtfully and ethically. 
As you learn Python, you're gaining the power to create, to solve problems, and to make a difference. Use this power wisely, and enjoy the endless possibilities it opens up.

.. include::  /_templates/components/footer-links.rst
