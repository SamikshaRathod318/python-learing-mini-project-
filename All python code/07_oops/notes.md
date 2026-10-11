*Python OOP Theory*
 
1. Basic Class and Object

Class: A class is a blueprint or template used to create objects. It defines the properties and behaviors that objects can have.

Object: An object is an instance of a class. It represents a specific entity and can have its own data and use the methods defined in its class.

Key points:

A class is defined using the class keyword.

Objects are created from classes.

A class can have multiple objects.

Classes help organize code and represent real-world entities.

2. Class Method and self

Method: A method is a function defined inside a class. It describes an action that an object or class can perform.

self: self refers to the current instance of a class. It allows instance methods to access the attributes and other methods belonging to that object.

Class method: A class method works with the class itself rather than a particular object. It is defined using the @classmethod decorator and takes cls as its first parameter.

Key points:

self refers to the current object.

cls refers to the class.

Instance methods normally use self.

Class methods use cls.

Python passes the instance or class automatically when the corresponding method is called.

3. Inheritance

Inheritance is an object-oriented programming concept in which one class acquires properties and methods from another class.

The class whose features are inherited is called the parent class or base class. The class that inherits those features is called the child class or derived class.

Types of inheritance:

Single inheritance: One child class inherits from one parent class.

Multiple inheritance: One child class inherits from multiple parent classes.

Multilevel inheritance: A class inherits from a child class, creating multiple levels.

Hierarchical inheritance: Multiple child classes inherit from one parent class.

Hybrid inheritance: A combination of different inheritance types.

Advantages:

Promotes code reuse.

Reduces code duplication.

Makes programs easier to maintain.

Allows child classes to extend or override inherited behavior.

4. Encapsulation

Encapsulation is the concept of combining data and the methods that operate on that data within a single class while controlling how the data is accessed or modified.

It helps protect data from accidental changes and keeps related functionality organized.

Access conventions in Python:

Public: Accessible throughout the program wherever the object or class is available.

Protected (_name): Indicates that an attribute is intended for internal use or use by subclasses.

Private (__name): Uses name mangling to reduce accidental access from outside the class.

Python does not enforce strict private access. These naming conventions help developers manage access and organize code.

Advantages:

Improves data management.

Supports controlled modification of values.

Reduces accidental misuse of data.

Makes code easier to maintain.

5. Class Variables

A class variable is a variable defined inside a class but outside its instance methods. It is associated with the class and is shared by its instances unless an instance overrides it with its own attribute.

An instance variable belongs to an individual object and stores data specific to that object.

Key points:

Class variables are useful for storing common information shared across objects.

Instance variables store individual object data.

Class variables can be accessed through the class or its instances.

Changing the class variable affects instances that access the shared class attribute, but an instance-level assignment can override it for that object.

6. Static Method

A static method is a function defined inside a class that does not automatically receive the current instance or the class as its first argument.

It is declared using the @staticmethod decorator.

Static methods are useful for utility operations that are logically related to a class but do not need to access instance-specific or class-specific data.

Key points:

A static method does not require self or cls.

It can be called through the class or an instance.

It helps organize related utility functions.

It does not automatically access instance or class state.

7. Property Decorators

A property decorator allows a method to be accessed like an attribute. It is commonly used to provide controlled access to data without changing the way the attribute is accessed.

The @property decorator defines a getter. The @name.setter decorator defines how a value can be assigned, while @name.deleter can define deletion behavior.

Advantages:

Provides controlled access to attributes.

Supports validation when values are assigned.

Allows values to be calculated when accessed.

Helps maintain a simple interface while changing internal implementation.

Supports encapsulation without requiring method-call syntax for reading a property.

8. Class Inheritance and isinstance() Function

The built-in isinstance() function checks whether an object is an instance of a specified class or one of its subclasses.

It is particularly useful when inheritance is involved because an object can be considered an instance of both its own class and its parent classes.

Key points:

Returns True when the object matches the specified type or class hierarchy.

Returns False when it does not match.

Supports checking against a tuple of types.

Helps verify object types before performing operations.

Is often preferred over direct type comparisons when inheritance matters.

9. Multiple Inheritance

Multiple inheritance is an OOP feature in which a single child class inherits from two or more parent classes.

It allows a class to combine functionality from multiple sources without duplicating the same code.

Key points:

A child class can inherit methods and attributes from multiple parent classes.

It supports code reuse and combining behaviors.

Conflicts can occur when parent classes define methods with the same name.

Python uses the Method Resolution Order (MRO) to determine the order in which classes are searched for attributes and methods.

Python calculates MRO using the C3 linearization algorithm.

Advantages:

Reuses functionality from different classes.

Supports flexible class design.

Helps combine related behaviors.

Limitation: Multiple inheritance can make code more complex, particularly when parent classes have overlapping methods or complicated inheritance relationships.

