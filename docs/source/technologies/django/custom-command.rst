Custom Commands
===============

`Django <https://www.djangoproject.com/>`__'s management command system provides a powerful way to create custom command-line utilities for your project. 

- 👉 Get `Support <https://app-generator.dev/ticket/create/>`__ via email and Discord 

This page will guide you through the process of adding a custom command to your Django application, demonstrating with a simple "Hello World" example.

.. include::  /_templates/components/banner-top.rst

**Command Structure**

Django looks for management commands in a `management/commands` directory within your app. Here's the typical structure:

.. code-block:: bash

    your_app/
        __init__.py
        models.py
        views.py
        management/
            __init__.py
            commands/
                __init__.py
                your_command.py

**Creating the Command**

Let's create a command called `hello_world`. Create a file named `hello_world.py` in the `management/commands/` directory of your app.

**Implementing the Command**

Here's the implementation of our `hello_world` command:

.. code-block:: python

    from django.core.management.base import BaseCommand
    from django.utils import timezone

    class Command(BaseCommand):
        help = 'Prints "Hello World" along with the current timestamp'

        def handle(self, *args, **kwargs):
            time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            self.stdout.write(
                self.style.SUCCESS(f'Hello World! Current time: {time}')
            )

The break down for this simple management command is this:

- We import `BaseCommand` from `django.core.management.base`. All custom commands should subclass BaseCommand.
- We import `timezone` from `django.utils` to get the current time.
- Our Command class `defines a help attribute`, which provides a brief description of the command.
- The `handle` method is where the command's logic is implemented. This method is called when the command is executed.
- We use `timezone.now()` to get the current time and format it as a string.
- `self.stdout.write()` is used to output text. We wrap our output in self.style.SUCCESS() to color it green in the console.

**Using the Command**

.. code-block:: bash

    python manage.py hello_world

This will output something like:

.. code-block:: bash

    Hello World! Current time: 2024-08-25 14:30:45

**Conclusion**

`Custom Management Commands` in **Django** provide a powerful way to extend your project's functionality and automate tasks. 
By following the structure outlined in this article and leveraging Django's BaseCommand class, you can create robust, reusable command-line utilities tailored to your project's needs.

.. include::  /_templates/components/footer-links.rst
