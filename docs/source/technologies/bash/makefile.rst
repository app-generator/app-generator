Makefile
========

A Makefile is a special file that defines a set of tasks (rules) to be executed by the `make` utility. Originally designed for compiling programs, 
Makefiles are now used for many automation tasks beyond compilation.

.. include::  /_templates/components/banner-top.rst

Key features of Makefiles
-------------------------

1. **Dependency Management**: Makefiles define relationships between files and the commands needed to update them when dependencies change.

2. **Target-Based Execution**: Each rule has a target (output), dependencies (inputs), and commands to run.

3. **Incremental Building**: Make only rebuilds what's necessary based on which files have changed since the last build.

4. **Variables and Pattern Rules**: Makefiles support variables and pattern matching to create reusable rules.

Basic Makefile structure:

.. code-block:: makefile

    target: dependencies
        commands


Example of a simple Makefile:

.. code-block:: makefile

    CC = gcc
    CFLAGS = -Wall -g

    program: main.o utils.o
        $(CC) $(CFLAGS) -o program main.o utils.o

    main.o: main.c
        $(CC) $(CFLAGS) -c main.c

    utils.o: utils.c
        $(CC) $(CFLAGS) -c utils.c

    clean:
        rm -f *.o program

Common usage:

- `make` - Runs the default (first) target
- `make target` - Runs a specific target
- `make -j4` - Runs with 4 parallel jobs
- `make clean` - Typically removes build artifacts

Makefiles are used for:

- Building software projects
- Running tests
- Generating documentation
- Deployment operations
- Any repeatable development workflow

While they originated in C/C++ development, Makefiles are now used across many programming languages and for general task automation in software projects.

.. include::  /_templates/components/footer-links.rst
