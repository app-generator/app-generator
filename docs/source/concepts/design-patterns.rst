:og:description: Design Patterns - Programming Concept

Design Patterns
===============

.. title:: Design Patterns - Programming Concept
.. meta::
    :description: Design patterns are reusable solutions to common problems in software design

Design patterns are reusable solutions to common problems in software design. They provide templates for solving issues that occur repeatedly in software development. 
Categories include creational patterns (like Singleton, Factory), structural patterns (like Adapter, Decorator), and behavioral patterns (like Observer, Strategy). 
Understanding design patterns helps in creating more flexible, reusable, and maintainable software architectures.

.. include::  /_templates/components/signin-invite.rst

These patterns deal with object creation mechanisms, making systems independent of how their objects are created, composed, and represented.

Singleton Pattern
-----------------

Ensures a class has only one instance and provides a global point of access to it. Think of it like a shared resource, such as a connection to a printer.

.. code-block:: java

    public class PrinterManager {
        private static PrinterManager instance;
        private Printer printer;
        
        private PrinterManager() {
            printer = new Printer();
        }
        
        public static PrinterManager getInstance() {
            if (instance == null) {
                instance = new PrinterManager();
            }
            return instance;
        }
        
        public void print(Document document) {
            printer.printDocument(document);
        }
    }

Factory Method Pattern
----------------------

Defines an interface for creating objects but lets subclasses decide which class to instantiate. It's like a restaurant kitchen that can create different types of dishes based on orders.

.. code-block:: java

    // Abstract creator
    public abstract class DocumentCreator {
        public abstract Document createDocument();
        
        public void processDocument() {
            Document doc = createDocument();
            doc.process();
        }
    }

    // Concrete creators
    public class PDFDocumentCreator extends DocumentCreator {
        @Override
        public Document createDocument() {
            return new PDFDocument();
        }
    }

    public class WordDocumentCreator extends DocumentCreator {
        @Override
        public Document createDocument() {
            return new WordDocument();
        }
    }


Builder Pattern
---------------

Separates the construction of a complex object from its representation. Think of it like customizing a car with different options.

.. code-block:: java

    public class Computer {
        private String cpu;
        private String ram;
        private String storage;
        
        public static class Builder {
            private Computer computer = new Computer();
            
            public Builder setCPU(String cpu) {
                computer.cpu = cpu;
                return this;
            }
            
            public Builder setRAM(String ram) {
                computer.ram = ram;
                return this;
            }
            
            public Builder setStorage(String storage) {
                computer.storage = storage;
                return this;
            }
            
            public Computer build() {
                return computer;
            }
        }
    }

    // Usage
    Computer computer = new Computer.Builder()
        .setCPU("Intel i7")
        .setRAM("16GB")
        .setStorage("512GB SSD")
        .build();

Structural Patterns
-------------------

These patterns deal with object composition and typically identify simple ways to realize relationships between different objects.

Adapter Pattern
****************

Allows incompatible interfaces to work together by wrapping an object in an adapter to make it compatible with another class. It's like using a power adapter when traveling abroad.

.. code-block:: java

    // Legacy interface
    public class LegacyPrinter {
        public void printDocument(String text) {
            System.out.println("Printing: " + text);
        }
    }

    // Modern interface
    public interface ModernPrinter {
        void print(Document document);
    }

    // Adapter
    public class PrinterAdapter implements ModernPrinter {
        private LegacyPrinter legacyPrinter;
        
        public PrinterAdapter(LegacyPrinter printer) {
            this.legacyPrinter = printer;
        }
        
        @Override
        public void print(Document document) {
            legacyPrinter.printDocument(document.getText());
        }
    }

Decorator Pattern
*****************

Attaches additional responsibilities to objects dynamically. Think of it like adding toppings to an ice cream cone.

.. code-block:: java

    // Base component
    public interface Coffee {
        double getCost();
        String getDescription();
    }

    // Concrete component
    public class SimpleCoffee implements Coffee {
        @Override
        public double getCost() {
            return 2.0;
        }
        
        @Override
        public String getDescription() {
            return "Simple Coffee";
        }
    }

    // Decorator
    public abstract class CoffeeDecorator implements Coffee {
        protected Coffee decoratedCoffee;
        
        public CoffeeDecorator(Coffee coffee) {
            this.decoratedCoffee = coffee;
        }
        
        public double getCost() {
            return decoratedCoffee.getCost();
        }
        
        public String getDescription() {
            return decoratedCoffee.getDescription();
        }
    }

    // Concrete decorator
    public class MilkDecorator extends CoffeeDecorator {
        public MilkDecorator(Coffee coffee) {
            super(coffee);
        }
        
        @Override
        public double getCost() {
            return super.getCost() + 0.5;
        }
        
        @Override
        public String getDescription() {
            return super.getDescription() + ", with milk";
        }
    }

Behavioral Patterns
-------------------

These patterns are concerned with communication between objects, how objects interact and distribute responsibility.

Observer Pattern
****************

Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified automatically. 
Like subscribers getting notifications when a YouTube channel posts a new video.

.. code-block:: java

    // Subject interface
    public interface Subject {
        void attach(Observer observer);
        void detach(Observer observer);
        void notifyObservers();
    }

    // Observer interface
    public interface Observer {
        void update(String message);
    }

    // Concrete subject
    public class NewsAgency implements Subject {
        private List<Observer> observers = new ArrayList<>();
        private String news;
        
        @Override
        public void attach(Observer observer) {
            observers.add(observer);
        }
        
        @Override
        public void detach(Observer observer) {
            observers.remove(observer);
        }
        
        @Override
        public void notifyObservers() {
            for (Observer observer : observers) {
                observer.update(news);
            }
        }
        
        public void setNews(String news) {
            this.news = news;
            notifyObservers();
        }
    }

Strategy Pattern
****************

Defines a family of algorithms, encapsulates each one, and makes them interchangeable. It's like choosing different routes to reach a destination based on current traffic conditions.

.. code-block:: java

    // Strategy interface
    public interface PaymentStrategy {
        void pay(int amount);
    }

    // Concrete strategies
    public class CreditCardPayment implements PaymentStrategy {
        private String cardNumber;
        
        public CreditCardPayment(String cardNumber) {
            this.cardNumber = cardNumber;
        }
        
        @Override
        public void pay(int amount) {
            System.out.println("Paid " + amount + " using credit card: " + cardNumber);
        }
    }

    public class PayPalPayment implements PaymentStrategy {
        private String email;
        
        public PayPalPayment(String email) {
            this.email = email;
        }
        
        @Override
        public void pay(int amount) {
            System.out.println("Paid " + amount + " using PayPal account: " + email);
        }
    }

    // Context
    public class ShoppingCart {
        private PaymentStrategy paymentStrategy;
        
        public void setPaymentStrategy(PaymentStrategy strategy) {
            this.paymentStrategy = strategy;
        }
        
        public void checkout(int amount) {
            paymentStrategy.pay(amount);
        }
    }

Conclusion
----------

Design patterns are valuable tools in a developer's toolkit, but they should be used judiciously. 
The key is understanding not just how to implement them, but when and why to use them. Remember that patterns are guidelines, not rules, and should be adapted to fit your specific needs.

When you're faced with a design decision, consider:
- The problem you're trying to solve
- The maintainability of your solution
- The flexibility needed for future changes
- The complexity trade-offs of using a pattern

The best use of design patterns comes from understanding their principles and adapting them to your specific context, rather than trying to force your code to fit a particular pattern.

.. include::  /_templates/components/footer-links.rst
