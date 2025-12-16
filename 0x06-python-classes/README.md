# 0x06. Python - Classes and Objects

This project focuses on understanding and implementing Object-Oriented Programming (OOP) concepts in Python. It covers the fundamentals of classes, objects, attributes, methods, encapsulation, and properties, as well as more advanced topics like operator overloading and bytecode analysis. The goal is to gain hands-on experience in defining and manipulating custom data types in Python.

## Learning Objectives
*   Why Python programming is awesome
*   What is OOP
*   “first-class everything”
*   What is a class
*   What is an object and an instance
*   What is the difference between a class and an object or instance
*   What is an attribute
*   What are and how to use public, protected and private attributes
*   What is `self`
*   What is a method
*   What is the special `__init__` method and how to use it
*   What is Data Abstraction, Data Encapsulation, and Information Hiding
*   What is a property
*   What is the difference between an attribute and a property in Python
*   What is the Pythonic way to write getters and setters in Python
*   How to dynamically create arbitrary new attributes for existing instances of a class
*   How to bind attributes to object and classes
*   What is the `__dict__` of a class and/or instance of a class and what does it contain
*   How does Python find the attributes of an object or class
*   How to use the `getattr` function

## Project Structure
```
.
├── 0-square.py
├── 1-square.py
├── 2-square.py
├── 3-square.py
├── 4-square.py
├── 5-square.py
├── 6-square.py
└── README.md
```

## Project Tasks
### 0. My first square
*   **File:** `0-square.py`
*   **Prototype:** `class Square:`
*   **Concept:** This task introduces the fundamental concept of defining a class in Python, demonstrating the creation of an empty class `Square` and its instantiation.
*   **Description:** Write an empty class `Square` that defines a square. You are not allowed to import any module.

### 1. Square with size
*   **File:** `1-square.py`
*   **Prototype:** `def __init__(self, size)` (implied)
*   **Concept:** This task delves into object instantiation and the use of private instance attributes (`__size`) to encapsulate data within a class. It highlights the importance of controlling attribute access.
*   **Description:** Write a class `Square` that defines a square by: (based on `0-square.py`)
    *   Private instance attribute: `size`
    *   Instantiation with `size` (no type/value verification)
    *   You are not allowed to import any module.

### 2. Size validation
*   **File:** `2-square.py`
*   **Prototype:** `def __init__(self, size=0):`
*   **Concept:** This task focuses on input validation and error handling within a class's `__init__` method. It demonstrates how to enforce type and value constraints for private attributes by raising `TypeError` and `ValueError` exceptions.
*   **Description:** Write a class `Square` that defines a square by: (based on `1-square.py`)
    *   Private instance attribute: `size`
    *   Instantiation with optional `size`: `def __init__(self, size=0):`
        *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
    *   You are not allowed to import any module.

### 3. Area of a square
*   **File:** `3-square.py`
*   **Prototype:** `def area(self):`
*   **Concept:** This task introduces public instance methods and how they can operate on private instance attributes. It demonstrates calculating and returning the area of a square based on its `size`.
*   **Description:** Write a class `Square` that defines a square by: (based on `2-square.py`)
    *   Private instance attribute: `size`
    *   Instantiation with optional `size`: `def __init__(self, size=0):`
        *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
    *   Public instance method: `def area(self):` that returns the current square area
    *   You are not allowed to import any module.

### 4. Access and update private attribute
*   **File:** `4-square.py`
*   **Prototype:**
    ```python
    @property
    def size(self):
        pass

    @size.setter
    def size(self, value):
        pass
    ```
*   **Concept:** This task introduces properties (getters and setters) as a Pythonic way to control access to private instance attributes. It reinforces input validation logic in the setter for `size`.
*   **Description:** Write a class `Square` that defines a square by: (based on `3-square.py`)
    *   Private instance attribute: `size`:
        *   property `def size(self):` to retrieve it
        *   property setter `def size(self, value):` to set it:
            *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
            *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
    *   Instantiation with optional `size`: `def __init__(self, size=0):`
    *   Public instance method: `def area(self):` that returns the current square area
    *   You are not allowed to import any module.

### 5. Printing a square
*   **File:** `5-square.py`
*   **Prototype:** `def my_print(self):`
*   **Concept:** This task focuses on object representation through a custom print method (`my_print`). It demonstrates how to visualize the square using the `#` character based on its `size`.
*   **Description:** Write a class `Square` that defines a square by: (based on `4-square.py`)
    *   Private instance attribute: `size`:
        *   property `def size(self):` to retrieve it
        *   property setter `def size(self, value):` to set it:
            *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
            *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
    *   Instantiation with optional `size`: `def __init__(self, size=0):`
    *   Public instance method: `def area(self):` that returns the current square area
    *   Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
        *   if `size` is equal to 0, print an empty line
    *   You are not allowed to import any module.

### 6. Coordinates of a square
*   **File:** `6-square.py`
*   **Prototype:**
    ```python
    def __init__(self, size=0, position=(0, 0)):
        pass

    @property
    def position(self):
        pass

    @position.setter
    def position(self, value):
        pass
    ```
*   **Concept:** This task extends the `Square` class by introducing another private instance attribute, `position`, which is a tuple. It demonstrates how to validate tuple input and use it to control the printed output of the square, adding complexity to object representation.
*   **Description:** Write a class `Square` that defines a square by: (based on `5-square.py`)
    *   Private instance attribute: `size`:
        *   property `def size(self):` to retrieve it
        *   property setter `def size(self, value):` to set it:
            *   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
            *   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
    *   Private instance attribute: `position`:
        *   property `def position(self):` to retrieve it
        *   property setter `def position(self, value):` to set it:
            *   `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
    *   Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
    *   Public instance method: `def area(self):` that returns the current square area
    *   Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
        *   if `size` is equal to 0, print an empty line
        *   `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
    *   You are not allowed to import any module.

## Compilation
*   Files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
*   All your files should end with a new line.
*   The first line of all your files should be exactly `#!/usr/bin/python3`.
*   All your files must be executable.
*   Your code should use the `pycodestyle` (version `2.8.*`).
*   All your modules, classes, and functions should have a documentation (`docstring`).

Example:
```bash
python3 0-main.py
pycodestyle 0-square.py
```

## Resources
*   [Object Oriented Programming](https://savanna.alxafrica.com/rltoken/i49z6HxrBGRNnixo7ZWbEQ)
*   [Object-Oriented Programming](https://savanna.alxafrica.com/rltoken/qz3KSn154ia4H2DPaabOzg)
*   [Properties vs. Getters and Setters](https://savanna.alxafrica.com/rltoken/Wy2djWXK5b4rnnYlAq_wlA)
*   [Learn to Program 9 : Object Oriented Programming](https://savanna.alxafrica.com/rltoken/MxIOanLf5vG5QeCWek2nqQ)
*   [Python Classes and Objects](https://savanna.alxafrica.com/rltoken/AoLH4xp5StrQST-Cu0Fg8w)
*   [Object Oriented Programming](https://savanna.alxafrica.com/rltoken/-vVnWzwR3a3X0H8Oia78Ug)
*   [Python bytecode](https://savanna.alxafrica.com/rltoken/l0hEn4L06ZhFg5HzGPbEhQ)
*   [Example Google Style Python Docstrings](https://savanna.alxafrica.com/rltoken/dOO785g5EQYkRU2E1wri0g)

## Key Concepts Summary
This project focuses on Object-Oriented Programming (OOP) in Python. Key concepts covered include:
*   Defining classes, objects, and instances.
*   Understanding attributes (public, private, protected) and methods.
*   The role of the `__init__` method and `self`.
*   Data Abstraction, Encapsulation, and Information Hiding.
*   Properties, getters, and setters for controlled attribute access.
*   Dynamic attribute creation and attribute binding.
*   Understanding `__dict__` and attribute lookup.
*   Introduction to data structures (singly linked lists) and their implementation.
*   Overloading comparison operators for custom object behavior.
*   Reverse engineering Python bytecode.

## Author
@zolldic
