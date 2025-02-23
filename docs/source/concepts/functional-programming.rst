:og:description: Functional Programming - Programming Concept 

Functional Programming
======================

.. title:: Functional Programming - Programming Concept  
.. meta::
    :description: Paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data

Functional programming is a paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. 
It emphasizes immutability, pure functions, and higher-order functions. Key concepts include first-class and higher-order functions, recursion, and lazy evaluation. 
Functional programming can lead to more predictable and testable code, especially in concurrent and parallel processing scenarios.

.. include::  /_templates/components/signin-invite.rst

Core Concepts
-------------

Pure Functions
**************

Think of pure functions as vending machines. Given the same input (money and selection), they always return the same output (snack), and they don't affect anything else in the world. They don't:
- Keep track of how many snacks they've dispensed
- Change the temperature of the room
- Send emails to the vendor

Here's an example of a pure function:

.. code-block:: javascript

    // Pure function
    function add(a, b) {
        return a + b;
    }

    // Compare with an impure function
    let total = 0;
    function addToTotal(value) {
        total += value;  // Modifies external state
        return total;
    }

Immutability
************

Immutability is like working with stone sculptures. Once carved, a stone sculpture can't be modified – to make changes, you need to create a new sculpture. 
Similarly, in functional programming, we don't modify existing data; we create new data with the desired changes.

.. code-block:: javascript

    // Immutable approach
    const numbers = [1, 2, 3, 4, 5];
    const doubled = numbers.map(n => n * 2);  // Creates new array
    console.log(numbers);  // Still [1, 2, 3, 4, 5]
    console.log(doubled);  // [2, 4, 6, 8, 10]

    // Compare with mutable approach
    const mutableNumbers = [1, 2, 3, 4, 5];
    for(let i = 0; i < mutableNumbers.length; i++) {
        mutableNumbers[i] *= 2;  // Modifies original array
    }

First-Class Functions
*********************

In functional programming, functions are treated like any other value – they can be:
- Assigned to variables
- Passed as arguments
- Returned from other functions
- Stored in data structures

This is like having recipe cards that you can:
- Store in different boxes
- Pass to other cooks
- Use to create new recipe collections

.. code-block:: javascript

    // Function as a value
    const greet = name => `Hello, ${name}!`;

    // Function as an argument
    const applyOperation = (x, operation) => operation(x);
    const double = x => x * 2;
    console.log(applyOperation(5, double));  // 10

    // Function returning a function
    const multiply = x => y => x * y;
    const triple = multiply(3);
    console.log(triple(4));  // 12


Common Patterns
---------------

Map, Filter, and Reduce
***********************

These are the Swiss Army knives of functional programming. They provide elegant ways to transform data:

**Map**: Transforms each element in a collection

.. code-block:: javascript

    const fruits = ['apple', 'banana', 'orange'];
    const upperFruits = fruits.map(fruit => fruit.toUpperCase());
    // ['APPLE', 'BANANA', 'ORANGE']

**Filter**: Selects elements that meet a condition

.. code-block:: javascript

    const numbers = [1, 2, 3, 4, 5, 6];
    const evenNumbers = numbers.filter(n => n % 2 === 0);
    // [2, 4, 6]

**Reduce**: Combines elements into a single value

.. code-block:: javascript

    const orders = [
        { amount: 20 },
        { amount: 30 },
        { amount: 40 }
    ];
    const total = orders.reduce((sum, order) => sum + order.amount, 0);
    // 90

Function Composition
********************

Function composition is like building a pipeline where data flows through multiple transformations. Each function takes the output of the previous function as its input.

.. code-block:: javascript

    // Helper to compose functions
    const compose = (...fns) => x => fns.reduceRight((y, f) => f(y), x);

    const addOne = x => x + 1;
    const double = x => x * 2;
    const square = x => x * x;

    const transform = compose(square, double, addOne);
    console.log(transform(3));  // ((3 + 1) * 2)² = 64

Practical Examples
------------------

Data Processing Pipeline
************************

Here's a real-world example of processing user data:

.. code-block:: javascript

    const processUsers = users => {
        const isAdult = user => user.age >= 18;
        const formatName = user => ({
            ...user,
            fullName: `${user.firstName} ${user.lastName}`
        });
        const calculateDiscount = user => ({
            ...user,
            discount: user.isPremium ? 0.2 : 0.1
        });

        return users
            .filter(isAdult)
            .map(formatName)
            .map(calculateDiscount);
    };

    const users = [
        { firstName: 'John', lastName: 'Doe', age: 25, isPremium: true },
        { firstName: 'Jane', lastName: 'Smith', age: 17, isPremium: false },
        { firstName: 'Bob', lastName: 'Johnson', age: 35, isPremium: true }
    ];

    const processedUsers = processUsers(users);

Event Handling
**************

Functional programming can make event handling more manageable:

.. code-block:: javascript

    const handleSubmit = event => {
        const preventDefault = e => {
            e.preventDefault();
            return e;
        };

        const extractFormData = e => 
            new FormData(e.target);

        const convertToObject = formData =>
            Object.fromEntries(formData);

        const validate = data => {
            if (!data.email || !data.password) {
                throw new Error('Missing required fields');
            }
            return data;
        };

        const submit = data =>
            fetch('/api/login', {
                method: 'POST',
                body: JSON.stringify(data)
            });

        return Promise.resolve(event)
            .then(preventDefault)
            .then(extractFormData)
            .then(convertToObject)
            .then(validate)
            .then(submit)
            .catch(console.error);
    };

Benefits and Challenges
-----------------------

- **Predictability**: Pure functions and immutable data make code behavior more predictable and easier to test.

- **Concurrency**: The absence of shared state makes concurrent programming safer and more straightforward.

- **Testing**: Pure functions are naturally unit-testable since they have no side effects and depend only on their inputs.

Best Practices
--------------

1. Start Small
**************

Begin by incorporating functional concepts gradually:
- Write pure functions where possible
- Use map, filter, and reduce instead of loops
- Avoid mutating state

2. Handle Side Effects Carefully
********************************

Keep side effects at the edges of your system:
- Separate pure business logic from I/O operations
- Use functional patterns to manage side effects
- Consider using functional effect systems

3. Use Type Systems
*******************

When available, leverage type systems to make your functional code more robust:

.. code-block:: javascript

    type User = {
        id: number;
        name: string;
        age: number;
    };

    const filterAdults = (users: User[]): User[] =>
        users.filter(user => user.age >= 18);

Conclusion
----------

Functional programming isn't just a set of rules about how to write code – it's a way of thinking about program construction that emphasizes clarity, predictability, and maintainability. 
While it may require some adjustment in thinking, the benefits of reduced bugs, easier testing, and more maintainable code make it a valuable addition to any programmer's toolkit.

Remember that you don't need to write everything in a purely functional style. 
Often, the most practical approach is to combine functional programming concepts with other paradigms, choosing the right tool for each specific task.

.. include::  /_templates/components/footer-links.rst
