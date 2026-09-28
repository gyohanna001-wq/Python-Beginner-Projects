🐍 Python OOP Practice — Polymorphism & Abstraction

This project is a collection of Python exercises and examples for practicing Object-Oriented Programming (OOP) concepts.

The files focus mainly on:

Polymorphism

Inheritance

Method overriding

Parent and child classes

Abstract classes

Abstract methods

Common functions working with different objects

📚 What I Practiced

🔹 Polymorphism

Polymorphism means "many forms."

In these exercises, the same method or function can behave differently depending on which object is passed to it.

For example, the project uses a common function such as:

def can_it_fly(bird):
    bird.fly()

The function can receive different objects, and each object's fly() method can produce a different result.

The Bird, Owl, and Penguin example demonstrates this idea: can_it_fly() is called with all three objects, and each object uses its own version of fly().

🔹 Method Overriding

Child classes can provide their own version of a method inherited from a parent class.

For example, the Bird class has methods such as:

def whoAmI(self):
    print('I am a Bird.')

def fly(self):
    print('Birds can fly.')

The Owl and Penguin classes override methods from Bird to provide their own behavior.

The project also demonstrates overriding with Animal, Dog, Cat, and Cow, where each child class provides its own make_sound() method.

🦉 Polymorphism Examples

1. Bird, Owl, and Penguin

The Bird class is the parent class.

Owl and Penguin inherit from Bird and override some of its methods.

The common function:

def can_it_fly(bird):
    bird.fly()

works with different objects.

Bird → Birds can fly.
Owl → Some owls can not fly.
Penguin → Penguins can not fly.

This demonstrates polymorphism because the same function produces different behavior depending on the object passed to it.

2. Mosquito, Pupae, and Larvae

Another example uses:

Mosquito

Pupae

Larvae

The child classes override methods such as whoAmI(), fly(), and swim().

The function:

def can_it_fly(a):
    a.fly()

is used with all three objects.

This shows how the same function can call a different implementation of fly() depending on the object.

3. Animals and Sounds

The project includes an Animal parent class and three child classes:

Dog

Cat

Cow

Each child class has its own make_sound() method:

Dog  → Woof!
Cat  → Meow!
Cow  → Moo!

The common function is:

def animal_sound(animal):
    animal.make_sound()

This is another example of polymorphism.

4. Shapes and Areas

The project also demonstrates polymorphism using:

Shape

Rectangle

Circle

Triangle

Each shape overrides the area() method.

The common function:

def what_is_the_area(shape):
    shape.area()

can work with each shape object.

The examples calculate the areas using the dimensions provided in the practice code.

5. Vehicles

The vehicle example contains:

Vehicle

Car

Bike

Truck

The child classes override:

info()
max_speed()

For example:

Car   → 4 wheels, 200 km/h
Bike  → 2 wheels, 120 km/h
Truck → 8 wheels, 140 km/h

The classes demonstrate how different child objects can provide their own implementations of the same methods.

6. Employees and Payroll

The employee example contains:

Employee

Manager

Developer

Intern

Each employee type provides its own versions of:

calculate_salary()
get_role()

The common function:

def show_payroll(employees):
    employees.calculate_salary()
    employees.get_role()

can be used with different employee objects.

This demonstrates polymorphism through different implementations of salary and role behavior.

7. Media Players

The media player example contains:

MediaPlayer

MusicPlayer

VideoPlayer

PodcastPlayer

Each player implements:

play()
pause()
stop()

A common function:

def media_controls(media):
    media.play()
    media.pause()
    media.stop()

can operate on different media-player objects.

For example:

Music Player  → plays, pauses, and stops a song
Video Player  → plays, pauses, and stops a video
Podcast Player → starts, pauses, and stops a podcast

This is another practical example of polymorphism.

🏗️ Abstraction

One of the files demonstrates abstraction using Python's abc module.

The project imports:

from abc import ABC, abstractmethod

An abstract base class called Vehicle is created:

class Vehicle(ABC):

The class defines abstract methods:

@abstractmethod
def start_engine(self):
    pass

and:

@abstractmethod
def stop_engine(self):
    pass

These methods establish a common interface that subclasses must implement.

🚗 Vehicle Abstraction Example

The Car class inherits from Vehicle:

class Car(Vehicle):

It provides implementations for:

start_engine()
stop_engine()

The example also contains internal methods such as:

_check_battery()
_prime_fuel_pump()
_engage_starter_motor()
_cut_fuel_supply()
_stop_ignition()

These represent internal implementation details.

The Vehicle class also includes shared methods such as:

get_info()
get_status()

The example demonstrates that an abstract class can contain both abstract methods and implemented methods.

🧠 OOP Concepts

Concept

What the project demonstrates

Inheritance

Child classes inherit from parent classes

Polymorphism

The same function or method call can behave differently for different objects

Method Overriding

Child classes replace inherited methods with their own implementations

Abstraction

Abstract classes define a common interface

Abstract Methods

Subclasses are required to implement specific methods

Encapsulation

Internal vehicle behavior is kept inside the class

📁 Project Files

Python-OOP-Practice/
│
├── Fix The Error.py
├── from abc import ABC, abstractmethod.py
├── Polmorphism Codes.py
├── Polymorphism Practice.py
├── Polymorphism Practice 2.py
└── Polymorphism Question Answers.py

Fix The Error.py

A practice exercise involving an Animal class, an overridden swim() method, and a make_animal_swim() function.

The file contains code that is intended to be fixed as part of the exercise.

from abc import ABC, abstractmethod.py

Demonstrates abstraction with:

ABC

abstractmethod

Vehicle

Car

Abstract engine methods

Shared vehicle methods

Polmorphism Codes.py

Demonstrates polymorphism using:

Mosquito

Pupae

Larvae

fly()

swim()

whoAmI()

Polymorphism Practice.py

Contains a basic polymorphism example using:

Bird

Owl

Penguin

It includes the can_it_fly() function.

Polymorphism Practice 2.py

Contains several larger polymorphism exercises involving:

Animals and sounds

Shapes and areas

Vehicles

Employees

Media players

Polymorphism Question Answers.py

Contains another set of polymorphism examples and practice answers using different classes and methods.

🎯 Project Goals

The goal of this project is to practice how Python classes and objects can work together.

By completing these exercises, I practiced how to:

Create classes and objects

Create parent and child classes

Use inheritance

Override methods

Pass different objects into the same function

Understand polymorphism

Create abstract base classes

Use @abstractmethod

Separate an interface from implementation details

💻 Technologies

Python 3

Python Object-Oriented Programming

abc module

🚀 Future Improvements

Possible improvements for this project include:

Add more polymorphism exercises

Add more abstract classes

Create interactive examples

Add user input

Add comments explaining each exercise

Fix and document the error-practice example

Combine the examples into a single OOP learning program

Add tests for each class and function

📖 Key Takeaway

The main idea practiced in this project is that different objects can share the same interface while behaving differently.

For example:

def can_it_fly(bird):
    bird.fly()

The function does not need to know exactly what kind of object it received. Each class can provide its own implementation of fly().

The project also shows how abstraction can define what subclasses must do while allowing each subclass to decide how it does it.

⭐ Practice Project

This repository is part of my Python learning journey and focuses on understanding Object-Oriented Programming, especially polymorphism and abstraction.

🆕 Additional OOP & API Practice

The project was expanded with four additional files. This brings the collection to 10 Python files total.

📺 Abstraction 2

Abstraction 2(1).py demonstrates abstraction with an abstract TV class.

The TV class uses ABC and an abstract turn_on property:

class TV(ABC):
    @property
    @abstractmethod
    def turn_on(self):
        pass

SamsungTV inherits from TV and implements the required behavior.

It also provides its own work() method.

This exercise demonstrates:

Abstract base classes

Abstract properties

Inheritance

Implementing abstract members in a child class

🎮 PlayStation Abstraction

Abstraction(1).py demonstrates abstraction using a PlayStation abstract base class.

The class defines:

@abstractmethod
def start_console(self):
    pass

@abstractmethod
def stop_console(self):
    pass

PlayStation4 implements those methods and also contains internal methods for the console's simulated startup and shutdown process.

The example also includes:

get_info()

get_status()

Battery state

Starting and stopping the console

Refueling/recharging the simulated battery

This is similar to the earlier Vehicle abstraction example, but uses a game console as the example.

🧠 Abstraction Questions

Abstraction Questions(1).py contains a larger collection of OOP questions, explanations, and examples.

Topics covered include:

Encapsulation

The file explains public, protected, and private attributes:

public_attribute
_protected_attribute
__private_attribute

It also explains Python's name mangling, where a private attribute such as:

__value

is internally represented using the class name.

IS-A and HAS-A Relationships

IS-A represents inheritance.

Example:

Car IS-A Vehicle

HAS-A represents composition.

Example:

Car HAS-A Engine

The file also explains why composition can be useful when classes need to contain other objects.

Method Overriding

A child class can replace a method inherited from its parent:

class Dog(Animal):
    def speak(self):
        print("Dog barks")

Method Overloading

The material explains that Python does not support traditional method overloading in the same way as some other languages.

Instead, Python can achieve overloading-like behavior with:

Default arguments

*args

**kwargs

Type checking

Constructors and super()

The file explains how __init__() works with inheritance and how:

super().__init__()

can call the parent constructor.

It also explains that super() follows Python's Method Resolution Order (MRO).

Abstract Base Classes

The material covers:

from abc import ABC, abstractmethod

and explains that subclasses must implement required abstract methods.

Multiple Inheritance and MRO

The file covers multiple inheritance and the Diamond Problem.

Python uses the C3 linearization algorithm to determine Method Resolution Order.

Encapsulation and Data Hiding

The material explains the difference between:

Encapsulation

Data hiding

Protected-by-convention attributes

Private/name-mangled attributes

It also includes a Student example using properties and setters to validate grades.

Composition vs. Inheritance

The file compares:

Inheritance → IS-A
Composition → HAS-A

It also presents the rule of thumb to favor composition when it provides a more flexible design.

Library User System

A larger example uses:

User

Student

Teacher

Guest

The example combines inheritance, polymorphism, encapsulation, properties, and different borrowing rules.

Bird/Penguin Design

The material discusses a design problem where putting fly() directly on a general Bird class can cause problems for birds such as penguins.

It presents an approach using separate abstractions for flying and swimming behavior.

Multiple Inheritance and Mixins

The file also demonstrates:

Multiple inheritance

MRO

A LoggerMixin

Reusable behavior through mixins

🔐 API Keys & API Practice

API Keys(1).py is a reference list for API projects.

It contains API-related entries for projects involving:

OpenWeather

Dog CEO

API Ninjas

JokeAPI

TheMealDB

Google Books

Other API services

⚠️ API Key Security

Do not publish real API keys, tokens, or credentials in a GitHub README.

The API Keys practice file contains credential-like values, so those values should not be copied into this public README.

Instead, store keys locally, for example:

API_KEY = "YOUR_API_KEY_HERE"

A better approach for larger projects is to use environment variables:

import os

API_KEY = os.getenv("API_KEY")

This keeps secrets out of the source code that gets uploaded to GitHub.

📁 Complete Project Structure

After adding the four new files, the collection contains 10 Python files:

Python-OOP-Practice/
│
├── Fix The Error.py
├── from abc import ABC, abstractmethod.py
├── Polmorphism Codes.py
├── Polymorphism Practice 2.py
├── Polymorphism Practice.py
├── Polymorphism Question Answers.py
│
├── Abstraction 2(1).py
├── Abstraction Questions(1).py
├── Abstraction(1).py
└── API Keys(1).py

📊 What the 10 Files Cover

Topic

Included

Classes & Objects

✅

Inheritance

✅

Polymorphism

✅

Method Overriding

✅

Method Overloading Concepts

✅

Abstraction

✅

Abstract Base Classes

✅

Abstract Methods

✅

Encapsulation

✅

Data Hiding

✅

Properties & Setters

✅

super()

✅

Constructors

✅

Multiple Inheritance

✅

Method Resolution Order (MRO)

✅

Composition

✅

Mixins

✅

API Practice

✅

API Key Security

✅

🎯 Overall Learning Goal

This collection is a Python OOP practice project covering several important programming concepts.

The exercises move from basic inheritance and polymorphism into more advanced topics such as abstraction, encapsulation, composition, multiple inheritance, MRO, mixins, and API usage.

The project is designed as a growing collection of practice exercises that can be expanded with additional Python programs over time.
