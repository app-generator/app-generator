Livewire
==========

Livewire is a full-stack framework for `Laravel <./index.html>`__ that makes building dynamic interfaces simple without leaving the comfort of `PHP <../php/index.html>`__. 
It was created by Caleb Porzio and enables developers to create reactive, real-time user interfaces with minimal JavaScript.

.. include::  /_templates/components/banner-top.rst


Key features of Livewire
------------------------

1. **PHP-First Approach**: Instead of writing JavaScript, you build interactive UI components using PHP classes.

2. **Real-Time Updates**: Components automatically update when data changes without page reloads.

3. **Two-Way Data Binding**: Changes in the UI automatically update the server-side state and vice versa.

4. **AJAX Without JavaScript**: Handles AJAX requests, DOM updates, and events behind the scenes.

5. **Form Validation**: Integrates with Laravel's validation system for real-time validation feedback.

6. **Events & Actions**: Components can emit events and listen for them from other components.

7. **Lifecycle Hooks**: Provides hooks for different stages of a component's lifecycle.


Basic Livewire component
------------------------

.. code-block:: php
    
    // Component class
    class SearchUsers extends Component
    {
        public $search = '';
        
        public function render()
        {
            return view('livewire.search-users', [
                'users' => User::where('name', 'like', "%{$this->search}%")->get()
            ]);
        }
    }

    // Corresponding Blade view
    <div>
        <input wire:model="search" type="text" placeholder="Search users...">
        
        <ul>
            @foreach($users as $user)
                <li>{{ $user->name }}</li>
            @endforeach
        </ul>
    </div>

Livewire has become extremely popular in the Laravel ecosystem because it allows developers to create rich, 
interactive applications without requiring extensive JavaScript knowledge or building a separate frontend with a JavaScript framework like Vue or React.


.. include::  /_templates/components/footer-links.rst
    