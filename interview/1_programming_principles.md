(San, Hirako. Cracking the Full Stack Developer Interview: The Complete Handbook to Land the Job (p. 13~). Hirako Publishing. Kindle Edition.)

## What is Object Oriented Programming?
Object Oriented Programmig(OOP) is programming paradigm where the complete
software operates as a series of objects talking to each other.
An object is a collection of data and methods that operate on its data.

## What are the advantages of OOP?
The main advantage of OOP is better manageable code that covers followings:
1. The overall understanding of the software increases as the distance between the language
spoken by developers and that spoken by users
2. Object orientation eases maintenance by the use of encapsulation.
One can easily change the underlying representation by keeping the methods same.
OOP paradigm is mainly useful for relatively big software.

## What are the main features of OOP?
- Encapsulation
- Polymorphism
- Inheritance

## What is a class?
A class is a representation of a type of object.
It is the blueprint/plan/template that describes the details of an object.

## What is an object?
An object is an instance of a class.
It has its own state, behavior, and identity.

## What is a constructor?
A constructor is a method used to initialize the state of an object, 
and it gets invoked at the time of object creation.
Rules for a constructor are
 - Constructor name should be the same as its class name.
 - A constructor must have no return type.

## What are the various types of constructors?
There are three various types of constructors, and they are as follows
 - Default constructor - has no parameters.
 - Parametric constructor - has a one more parameters. creates a new isntances of a class given passed parameters.
 - Copy constructor - creates a new objet as a copy of an existing object.

## What is this?
this refers to the current object of a class.
this keyword is used as a pointer which defferentiates between the given object and the global object.
Basically, it refers to the current object.

## What is method overloading?
Method overloading tis the concept of creating several methods having the same name
but differ from each other by the type and/ or numbers of input parameters taken.

## Difference between overloading and overriding?
Overloading is static binding whereas overriding is dynamic binding.
Overloading is nothing but the same method with different arguments,
and it may or may not return the same value in the same class itself.

Overriding is the same method names with same arguments associated with the class 
and its child class.

## What are access modifiers? 
Access modifiers determine the scope of the method or variables 
that can be accessed from other various objects or classes.

## What is exception handling?
An exception is an event that occurs during the execution of a program.
Many exceptions types exist - runtime exception, error exceptions, etc.
those exceptions are adequately handled through exception handling mechanism using the
try catch and throw keywords.

## what is encapsulation?
Encapsulation refeters to one of the following two notions.
 - Data hiding: A language feature to restrict access to members of an object.
 For example, private and protected mebers in C++
 - Bundling of data and methods together: Data and methods that operate on that data are bundled together.

## What is Polymorphism?
Polymorphism means that some code or operations or objects behave
differently in different context.

## What is Inheritance? What is its purpose?
The idea of inheritance is that a class(called child or sub class) is based on
another class(parent or super class) and uses data and implementation of that other class.
The purpose of inheritance is code/login reuse.

## What is the difference between an interface and an abstract class?
Abstract
 - For an abstract class, a method must be declared as abstract.An abstract method doesn't have an implementation.
 - The Abstract methods can be declared with Access modifiers like public, internal, protected, etc. When implementing these methods in a subclass, you must define them with the same (or a less restricted) visibility.
 - Abstract classes can contain variables and concrete methods.
 - A class can Inherit only one Abstract class. Hence multiple inheritance is not possible for an Abstract class.
 - Abstract is object-oriented. It offers the basic data an 'object' should have and/or functions it should be able to do. It is concerned with the object's basic characteristics: what it has and what it can do. Hence objects which inherit from the same abstract class share the basic characteristics(generalization).
 - Abstract class establishes "is a" relation with concrete classes.

Interface
 - For an interface, all the methods are abstract by default. So one can not declare variables or concrete methods in interfaces.
 - All methods declared in an interface must be public.
 - Interfaces cannot contain variables and concrete methods except constatnts.
 - A class can implement many interfaces. Hence mltiple interface inheritance is possible.
 - Interface is functionality-oriented. It defines functionalities an object should have. Regardless what object it is, as long as it can do these funtionalities, which are defined in the interface, it's fine. It ignores everything else. An object/class can contin several (groups of) functionalities; hence it is possible for a class to implement multiple interfaces.
 - Interface provides "has a" capability for classes.


