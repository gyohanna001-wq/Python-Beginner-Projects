"""
1. The use for a single underscore is for public attributes in Python, and the dunder in Python is used for private attributes. Encapsulation means bundling data and methods and python uses conventions like a underscore, not strict protection.

2. The "IS-A" relationship is a fundamental concept of inheritance. It signifies that a subclass is a specialized version of its superclass.

The "HAS-A" relationship refers to composition, where a class contains one or more instances of other classes as its components or attributes rather than inheriting from them. This establishes a part-whole relationship.

3. Public (attribute): Can be accessed directly from outside the class.
Protected (_attribute): Intended for use within the class and its subclasses. The underscore is a convention, not strict protection.
Private (__attribute): Intended to prevent direct access from outside the class. Python uses name mangling to make the name harder to access accidentally.

Name mangling: If an attribute is named __value inside a class called MyClass, Python internally changes it to _MyClass__value. This helps avoid accidental access or conflicts with subclasses, but it is not true security.

4. A base class is a main class for the parents class, and the derived class a.k.a child class, is used to inherit the methods, from the parent class.

Example;
"""
class Speaker:
    def __init__(self):
        print('Speaker is created.')

    def turn_on(self):
        print("Speaker is turned on.")

    def is_it_working(self):
        return "Speaker is working."


class SamsungSpeaker(Speaker):
    def __init__(self):
          super().__init__()
         
    def turn_on(self):
          print("Samsung Speaker has been turned on.")

    def is_it_working(self):
          return "Samsung Speaker is working."

"""
5. Method overriding vs. method overloading

Method overriding happens when a child class provides its own version of a method that already exists in the parent class.
"""
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


d = Dog()
d.speak()   # Dog barks
"""
Method overloading means having multiple methods with the same name but different parameters. Python does not support traditional method overloading because defining a method again replaces the previous definition.
"""
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()
print(calc.add(2, 3))       # 5
print(calc.add(2, 3, 4))    # 9
"""
Python usually achieves overloading-like behavior with default arguments, *args, **kwargs, or type checking.

6. Difference between overriding and overloading
Overriding    Overloading
Happens between parent and child classes    Usually means multiple methods with the same name
Child replaces/inherits a parent's method behavior    Different parameter lists provide different behaviors
Fully supported by Python    Traditional form is not supported
Uses inheritance    Does not require inheritance

Overriding example:
"""

class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        print("Child")


Child().show()   # Child
"""
Overloading-like behavior:
"""
class Calculator:
    def add(self, *numbers):
        return sum(numbers)


c = Calculator()
print(c.add(2, 3))       # 5
print(c.add(2, 3, 4, 5)) # 14
"""
7. Constructors and inheritance

A constructor in Python is usually the __init__() method.

When a child class has its own __init__(), Python does not automatically call the parent's __init__(). You can explicitly call it using super().
"""

class Parent:
    def __init__(self):
        print("Parent constructor")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")


Child()
"""
Output:

Parent constructor
Child constructor

So the order is:

Child constructor starts.
super().__init__() calls the parent constructor.
Parent initialization runs.
Control returns to the child constructor.
Child initialization continues.

If the child doesn't define __init__(), it can inherit the parent's constructor.

8. What is super()?

super() returns a proxy that lets you access methods or attributes from a parent class according to Python's Method Resolution Order (MRO).

Use case 1: Calling the parent's constructor
"""
class Parent:
    def __init__(self, name):
        self.name = name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


c = Child("Alex", 15)
"""

Use case 2: Extending a parent's method
"""
class Parent:
    def greet(self):
        print("Hello")


class Child(Parent):
    def greet(self):
        super().greet()
        print("Welcome!")


Child().greet()

"""
Output:

Hello
Welcome!
9. Preventing inheritance and method overriding

Python does not have a traditional final class or final method mechanism that is enforced at runtime.

However, Python provides final in the typing module to tell type checkers that a class or method should not be inherited/overridden.
"""

from typing import final


@final
class Parent:
    pass


class Child(Parent):   # Type checker reports an error
    pass
"""
For a method:
"""
from typing import final


class Parent:
    @final
    def important(self):
        print("Do not override")


class Child(Parent):
    def important(self):  # Type checker reports an error
        pass
"""
Important: @final is mainly a static type-checking restriction; Python itself does not prevent someone from doing this at runtime.

10. Abstract Base Class (ABC)

An Abstract Base Class is a class designed to define a common interface for its subclasses. It can contain abstract methods that subclasses are required to implement.

Python provides the abc module for this.
"""
from abc import ABC, abstractmethod


class Animal(ABC):


    @abstractmethod
    def speak(self):
        pass
"""
You cannot normally create an instance of this class:

a = Animal()  # TypeError

A subclass must implement the abstract method:
"""
class Dog(Animal):
    def speak(self):
        print("Woof")


d = Dog()
d.speak()
"""
Why ABCs are useful:

They define a required interface.
They ensure subclasses implement important methods.
They make large programs easier to organize and maintain.

A regular class can generally be instantiated even if its methods aren't implemented.

11. Multiple inheritance, Diamond Problem, and MRO

Multiple inheritance means a class inherits from more than one parent.
"""
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
"""
Here, D inherits from both B and C.

The Diamond Problem occurs when two parent classes inherit from the same class:

       A
      / \
     B   C
      / \
       D

Python solves this using Method Resolution Order (MRO).

You can see the MRO with:
"""
print(D.mro())
"""
Python uses the C3 linearization algorithm to determine the order in which classes are searched for methods.

For the example above, the order is approximately:

D → B → C → A → object

super() follows this MRO, which helps make cooperative multiple inheritance work correctly.

12. Encapsulation vs. Data Hiding

They are related, but they are not exactly the same.

Encapsulation means combining data and the methods that operate on that data inside a class and controlling how that data is accessed.
"""
class BankAccount:
    def __init__(self, balance):
        self._balance = balance


    def deposit(self, amount):
        self._balance += amount


    def get_balance(self):
        return self._balance
"""
Data hiding specifically refers to restricting or discouraging direct access to internal implementation details.
Data hiding means to hide protected data.
But encapsulation is combining data together and the methods that operate on the data in a class and controlling how the data is accesed.
In conclusion, data hiding is important in encapsulation, and encapsulation is a great topic for data hiding.

Python uses naming conventions:
"""
class Person:
    def __init__(self):
        self._age = 15      # protected-by-convention
        self.__password = "secret"  # name-mangled
"""
_age means "internal/protected; don't access directly" by convention.
__password triggers name mangling, making accidental direct access harder.
Python does not provide the same strict private-access system found in languages such as Java or C++.

In short:
Encapsulation = putting data and behavior together and controlling access.
Data hiding = restricting or discouraging access to internal data. 
"""
"""
15. Vehicle → Car
python
"""
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.__number_of_doors = number_of_doors
"""
super().__init__(make, model) calls Vehicle's constructor to set up the inherited attributes, then Car adds its own attribute (__number_of_doors is name-mangled to _Car__number_of_doors).

16. Output analysis
Child constructor
Parent constructor
Child display

Why: obj = Child() calls Child.__init__, which prints "Child constructor" first, then calls super().__init__() — which runs Parent.__init__ and prints "Parent constructor". Then obj.display() uses normal method resolution order (MRO): since Child defines its own display(), that one runs (overriding Parent.display), printing "Child display". Parent.display is never called because Child overrides it and nothing calls super().display().

17. Encapsulation with Student
python
"""
class Student:
    def __init__(self, name, id, grade):
        self.__name = name
        self.__id = id
        self.__grade = grade

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            raise ValueError("Grade must be between 0 and 100")


# Example usage
s = Student("Alice", 101, 85)
print(s.name, s.id, s.grade)   # Alice 101 85

s.grade = 95        # valid, works fine
print(s.grade)       # 95

try:
    s.grade = 150    # invalid
except ValueError as e:
    print(e)          # Grade must be between 0 and 100
"""
The double-underscore prefix triggers name mangling, making the fields effectively private (_Student__name, etc.), and the @property/@x.setter pattern lets you control read/write access — the setter enforces the 0–100 validation rule.

18. GrandParent → Parent → Child (MRO)

Output:

C
P
GP

Explanation: Child() calls Child.__init__, printing "C", then super().__init__() moves up the MRO to Parent.__init__, printing "P", which itself calls super().__init__(), moving to GrandParent.__init__, printing "GP". The MRO for Child is Child → Parent → GrandParent → object, and each class's super() call cooperatively passes the call to the next class in that chain, so all three constructors run in order from most-derived to least-derived.

19. Shape → Circle, Rectangle
python
"""
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Example usage
shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(f"{s.__class__.__name__} area: {s.area()}")
"""
This demonstrates polymorphism: each subclass overrides area() with its own formula, so calling s.area() in the loop invokes the correct version depending on the actual object type, even though they're all treated as Shape in the list.

25. Inheritance vs Composition

Inheritance models an "is-a" relationship — a subclass is a specialized version of its parent and inherits its interface/behavior.

Composition models a "has-a" relationship — a class contains instances of other classes as attributes and delegates work to them.

python
"""
# Inheritance: a Car IS a Vehicle
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

# Composition: a Car HAS an Engine
class Engine:
    def start(self):
        print("Engine starting")

class Car:
    def __init__(self):
        self.engine = Engine()  # composition

    def start(self):
        self.engine.start()
"""
Prefer composition when:

The relationship isn't a true "is-a" (a Car is not an Engine)
You want to swap behavior at runtime (different engine types)
You want to avoid deep, fragile inheritance hierarchies
You need to combine behaviors from multiple sources without multiple-inheritance complexity

Rule of thumb: "favor composition over inheritance" — inheritance tightly couples classes and can break when the parent changes; composition is more flexible and easier to maintain.

26. Encapsulation in large codebases

Encapsulation hides internal implementation details behind a controlled interface (getters/setters, methods), so the internal representation can change without breaking code elsewhere that depends on the class.

python
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # internally renamed from __amount

    @property
    def balance(self):
        return self.__balance
"""
If you rename the private attribute from self.__amount to self.__balance internally, no external code breaks, because outside code only ever interacts through the balance property — never directly with the attribute name. This lets large codebases evolve internal logic (validation, storage format, caching) safely, since encapsulation limits the "blast radius" of internal changes to a single class.

27. Indirect access to private members

A subclass cannot directly access __private (double-underscore) attributes of the parent due to name mangling (__attr becomes _ClassName__attr). But it can access it indirectly through public/protected methods the parent provides.

python
"""
class Parent:
    def __init__(self):
        self.__secret = 42

    def get_secret(self):   # public method provides indirect access
        return self.__secret

class Child(Parent):
    def show(self):
        # print(self.__secret)  # AttributeError - not accessible directly
        print(self.get_secret())  # works - indirect access via inherited method

c = Child()
c.show()  # 42
"""
28. Sealed classes / preventing inheritance

Some languages (Java's final, C#'s sealed) let you mark a class so it cannot be subclassed. Python has no built-in keyword for this, but you can simulate it.

Approach 1 — using __init_subclass__:

python
"""
class Sealed:
    def __init_subclass__(cls, **kwargs):
        return f"Cannot inherit from sealed class {Sealed.__name__}"

class Attempt(Sealed):  # raises TypeError
    pass
"""
Approach 2 — using a metaclass:
python
"""
class SealedMeta(type):
    def __new__(mcs, name, bases, namespace):
        for base in bases:
            if isinstance(base, SealedMeta):
                print(f"Cannot inherit from sealed class '{base.__name__}' — returning base instead.")
                return base   # no exception, just hand back the original sealed class
        return super().__new__(mcs, name, bases, namespace)


class Sealed(metaclass=SealedMeta):
    pass

class Attempt(Sealed):   # no error — Attempt just IS Sealed
    pass

print(Attempt)          # <class '__main__.Sealed'>
print(Attempt is Sealed)  # True
"""
Both work by intercepting subclass creation and raising an error before the new class is defined.

29. Library user system
python
"""
class User:
    def __init__(self, user_id, password):
        self.__user_id = user_id
        self.__password = password

    @property
    def user_id(self):
        return self.__user_id

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters")
        self.__password = value

    def check_password(self, value):
        return self.__password == value


class Student(User):
    def __init__(self, user_id, password, student_id):
        super().__init__(user_id, password)
        self.__student_id = student_id
        self.__borrowed_books = 0

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self):
        if self.__borrowed_books >= 5:   # student borrowing limit
            print("Borrow limit reached")
        else:
            self.__borrowed_books += 1

    def return_book(self):
        if self.__borrowed_books > 0:
            self.__borrowed_books -= 1


class Teacher(User):
    def __init__(self, user_id, password, department):
        super().__init__(user_id, password)
        self.department = department
        self.__borrowed_books = 0

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self):
        if self.__borrowed_books >= 10:  # teachers get a higher limit
            print("Borrow limit reached")
        else:
            self.__borrowed_books += 1


class Guest(User):
    def __init__(self, user_id, password):
        super().__init__(user_id, password)
        self.__borrowed_books = 0

    def borrow_book(self):
        print("Guests cannot borrow books")  # no borrowing privileges


# Example usage
s = Student("s01", "secret1", "STU100")
s.borrow_book()
print(s.borrowed_books)  # 1
"""
Design notes:

User is the base class encapsulating shared private data (__user_id, __password) via properties.
Student, Teacher, Guest inherit from User and each define their own borrowing rules (different limits, or none at all for guests) — a nice illustration of inheritance + polymorphism.
Sensitive fields (ID, password, borrowed count) stay private, accessed only through controlled methods/properties, protecting internal state from being changed arbitrarily.
30. Bird/Penguin design flaw

The flaw: This is a classic violation of the Liskov Substitution Principle. Bird defines fly() as if all birds can fly, but Penguin (a legitimate subclass of Bird) cannot fly. Forcing Penguin to inherit fly() means either:

It has to override fly() with something nonsensical (e.g., raise an error or do nothing), which breaks the expectation that any Bird can safely call fly()
Code that treats all birds polymorphically (for bird in birds: bird.fly()) will crash or misbehave on a Penguin

The fix: Don't put fly() on the base class at all. Instead, factor flying ability into a separate interface/abstract base class that only flying birds implement.

python
"""
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        self.fly()

    def fly(self):
        print("Flying")

class SwimmingBird(Bird):
    def move(self):
        self.swim()

    def swim(self):
        print("Swimming")

class Sparrow(FlyingBird):
    pass

class Penguin(SwimmingBird):
    pass


birds = [Sparrow(), Penguin()]
for b in birds:
    b.move()  # works correctly for both — no broken fly() call
"""
This uses abstraction (an ABC defining a common move() interface) so each subclass implements movement in a way that's actually valid for it, rather than inheriting behavior that doesn't apply.

Bonus Challenges
B1. Name mangling demonstration
python
"""
class MyClass:
    def __init__(self):
        self.__attribute = 100

obj = MyClass()

# print(obj.__attribute)          # AttributeError - doesn't exist under this name
print(obj._MyClass__attribute)    # 100 - accessing via the mangled name
"""
Python renames __attribute to _MyClass__attribute internally to avoid accidental name clashes in subclasses. It's not true security — just a naming convention enforced automatically — so it can still be accessed if you know the mangled form.

B2. Multiple inheritance and MRO
python
"""
class A:
    def method(self):
        print("Method from A")

class B:
    def method(self):
        print("Method from B")

    def method_b(self):
        print("Only in B")

class C(A, B):
    pass

c = C()
c.method()      # Method from A  (A comes first in C's bases)
c.method_b()    # Only in B      (inherited from B)

print(C.__mro__)
# (<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>)
"""
Python uses the C3 linearization algorithm to compute MRO. Since C(A, B) lists A before B, the MRO is C → A → B → object, so A.method() takes priority over B.method() when both define the same method name.

B3. Logger mixin
python
"""
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {self.__class__.__name__}: {message}")


class Database(LoggerMixin):
    def __init__(self, name):
        self.name = name

    def connect(self):
        self.log(f"Connecting to database '{self.name}'")
        # connection logic here
        self.log("Connected successfully")

    def query(self, sql):
        self.log(f"Executing query: {sql}")
        # query logic here


db = Database("UsersDB")
db.connect()
# [LOG] Database: Connecting to database 'UsersDB'
# [LOG] Database: Connected successfully

db.query("SELECT * FROM users")
# [LOG] Database: Executing query: SELECT * FROM users
"""
A mixin is a class not meant to stand alone — it provides a focused set of reusable methods (here, log()) that get "mixed in" to other classes via inheritance, without implying an "is-a" relationship in the traditional sense. Database gains logging for free just by inheriting from LoggerMixin, and the same mixin could be reused across many unrelated classes.
"""
