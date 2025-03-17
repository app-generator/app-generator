:og:description: Don't Repeat Yourself (DRY) - Core software development concept

DRY Principle 
=============

.. title:: Don't Repeat Yourself (DRY) - Core software development concept 
.. meta::
    :description: Development concept that states: Every piece of knowledge or logic must have a single, unambiguous representation within a system

The DRY principle is a core software development concept that states: "Every piece of knowledge or logic must have a single, unambiguous representation within a system.".

.. include::  /_templates/components/signin-invite.rst

Key aspects of DRY
------------------

- **Core concept**: Knowledge should exist in one place and be referenced elsewhere rather than duplicated
- **Purpose**: Reduces redundancy and simplifies maintenance
- **Implementation**: Uses abstraction, inheritance, and composition to reuse code
- **Benefits**: Easier maintenance, fewer bugs, smaller codebase, and improved consistency

DRY in practice
---------------

When applied to programming, DRY encourages:

- Creating reusable functions/methods instead of copying code blocks
- Using inheritance to share behavior between similar classes
- Applying templates or partials for repeated UI elements
- Centralizing configuration values rather than hardcoding them multiple places
- Using constants and enums for values used throughout the codebase

Django's DRY approach
---------------------

Django exemplifies DRY through:

- Models that define data structure once, then generate database schemas and form validation
- Template inheritance that allows common elements (headers, footers) to be defined once
- Class-based views that encapsulate common patterns
- URL routing that centralizes path definitions
- Middleware that handles cross-cutting concerns in one place

The opposite of DRY is WET ("Write Everything Twice" or "We Enjoy Typing"), which leads to maintenance challenges and inconsistencies when changes are needed.

.. include::  /_templates/components/footer-links.rst
