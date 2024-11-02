Cheatsheet
==========

This page contains Python Beginner's Cheatsheet, a short list with some hidden Gems

.. include::  /_templates/components/banner-top.rst

**String Operations You Might Not Know**

.. code-block:: python

    # Remove whitespace from both ends
    text = "  hello  "
    text.strip()  # "hello"

    # Center text in a fixed width
    "Python".center(10, "*")  # "**Python**"

    # Split string into fixed-width chunks
    chunks = [text[i:i+3] for i in range(0, len(text), 3)]    


**List Tricks**

.. code-block:: python

    # Create a list of numbers easily
    numbers = list(range(1, 11))  # [1, 2, 3, ..., 10]

    # Get last n items
    my_list = [1, 2, 3, 4, 5]
    last_three = my_list[-3:]  # [3, 4, 5]

    # Remove duplicates while maintaining order
    my_list = list(dict.fromkeys(my_list))


**Dictionary Magic**

.. code-block:: python

    # Get value with fallback if key doesn't exist
    my_dict = {'a': 1}
    value = my_dict.get('b', 'not found')  # 'not found'

    # Merge dictionaries
    dict1 = {'a': 1}
    dict2 = {'b': 2}
    merged = {**dict1, **dict2}  # {'a': 1, 'b': 2}


**Loop Enhancements**

.. code-block:: python

    # Enumerate with custom start index
    for i, item in enumerate(['a', 'b', 'c'], start=1):
        print(f"{i}: {item}")  # 1: a, 2: b, 3: c

    # Loop over multiple lists simultaneously
    for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
        print(f"{x}-{y}")  # 1-a, 2-b, 3-c


**File Operations**

.. code-block:: python

    # Read file directly into a list of lines
    with open('file.txt') as f:
        lines = f.read().splitlines()

    # Write multiple lines at once
    lines = ['line1', 'line2', 'line3']
    with open('file.txt', 'w') as f:
        f.write('\n'.join(lines))


**Built-in Functions You Should Know**

.. code-block:: python

    # Convert multiple inputs to integers
    x, y, z = map(int, input().split())

    # Find largest/smallest n items
    import heapq
    numbers = [10, 5, 8, 3, 1]
    largest_three = heapq.nlargest(3, numbers)  # [10, 8, 5]    


**String Formatting**

.. code-block:: python

    # f-strings with formatting
    name = "Alice"
    age = 25.5
    print(f"{name:>10}")  # Right align with width 10
    print(f"{age:.1f}")   # One decimal place

    # Format numbers with commas
    number = 1000000
    print(f"{number:,}")  # 1,000,000    


**Collection Operations**

.. code-block:: python

    from collections import Counter, defaultdict

    # Count occurrences
    text = "hello world"
    letter_count = Counter(text)  # {'l': 3, 'o': 2, ...}

    # Dictionary with default value
    d = defaultdict(list)
    d['new_key'].append(1)  # No KeyError if key doesn't exist    


**Conditional Assignments**

.. code-block:: python

    # Ternary operator
    x = 5
    status = "even" if x % 2 == 0 else "odd"

    # Multiple conditions
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"    


**Error Handling**

.. code-block:: python    

    # Multiple exception types
    try:
        # some code
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    # Else clause in try-except
    try:
        result = perform_operation()
    except Exception:
        print("Error occurred")
    else:
        print("Operation successful!")
    finally:
        print("Cleanup code")    


**Context Managers**

.. code-block:: python    

    # Custom context manager
    from contextlib import contextmanager

    @contextmanager
    def timer():
        from time import time
        start = time()
        yield
        print(f"Elapsed: {time() - start:.2f} seconds")

    with timer():
        # Your code here
        pass    

**PRO Tips**

- Use `help()` function to get documentation
- Try `dir()` to see all attributes of an object
- The interactive interpreter can be cleared with ctrl + l
- Use `_`` to access the last printed expression in interactive mode
- IPython's ? and ?? for quick help and source code

.. include::  /_templates/components/footer-links.rst
