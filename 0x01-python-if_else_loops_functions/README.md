# 0x01. Python - if/else, loops, functions

This project explores fundamental Python programming concepts including conditional statements, loops, and function definitions. It covers control flow, iteration patterns, and basic function implementation.

## Learning Objectives

At the end of this project, you should be able to explain:

* Why Python programming is awesome
* How to use if, if...else statements
* How to use comments in Python
* How to assign values to variables
* How to use while and for loops
* How to use break and continue statements
* How to use else clauses on loops
* What the pass statement does and when to use it
* How to use range
* What functions are and how to use them
* What a function returns if it does not use any return statement
* Scope of variables
* What a traceback is
* What arithmetic operators are and how to use them

## Project Structure

**Header File:**
* `lists.h` - Contains definitions for singly linked list operations

**Helper Files:**
* `linked_lists.c` - Helper functions for linked list operations
* `13-main.c` - Main file for testing C function

## Project Tasks

### 0. Positive anything is better than negative nothing
**File:** `0-positive_or_negative.py`

**Description:** Assign a random signed number to the variable `number` each time it is executed. Print whether the number is positive, negative, or zero.

**Concept:** Using if/elif/else statements to determine the sign of a number. Random number generation in Python.

---

### 1. The last digit
**File:** `1-last_digit.py`

**Description:** Print the last digit of a randomly generated number. The output must follow specific conditions based on whether the last digit is greater than 5, is 0, or is less than 6 and not 0.

**Concept:** Using the modulo operator to extract digits. String formatting with f-strings.

---

### 2. I sometimes suffer from insomnia
**File:** `2-print_alphabet.py`

**Description:** Print the ASCII alphabet in lowercase, not followed by a new line.

**Concept:** Using for loops with range. ASCII character manipulation and print formatting.

---

### 3. When I was having that alphabet soup
**File:** `3-print_alphabt.py`

**Description:** Print the ASCII alphabet in lowercase except for the letters q and e.

**Concept:** Loop iteration with conditional filtering. The continue statement.

---

### 4. Hexadecimal printing
**File:** `4-print_hexa.py`

**Description:** Print numbers from 0 to 98 in decimal and hexadecimal format.

**Concept:** Number base conversion. Using format strings for hexadecimal output.

---

### 5. 00...99
**File:** `5-print_comb2.py`

**Description:** Print numbers from 0 to 99 with two digits, separated by commas and space.

**Concept:** String formatting with zero padding. Conditional output formatting for the last element.

---

### 6. Inventing is a combination of brains and materials
**File:** `6-print_comb3.py`

**Description:** Print all possible different combinations of two digits where the first digit is less than the second.

**Concept:** Nested loops. Generating combinations without repetition.

---

### 7. islower
**File:** `7-islower.py`

**Prototype:** `def islower(c):`

**Description:** Function that checks if a character is lowercase. Returns True if c is lowercase, False otherwise.

**Concept:** Function definition. Using ASCII values or string methods to check character case.

---

### 8. To uppercase
**File:** `8-uppercase.py`

**Prototype:** `def uppercase(str):`

**Description:** Function that prints a string in uppercase followed by a new line. Only use two print functions and one loop. Cannot use string methods like upper() or str.upper().

**Concept:** ASCII manipulation. Converting lowercase to uppercase using ord() and chr().

---

### 9. There are only 3 colors, 10 digits, and 7 notes
**File:** `9-print_last_digit.py`

**Prototype:** `def print_last_digit(number):`

**Description:** Function that prints the last digit of a number. Returns the value of the last digit.

**Concept:** Using modulo operator with negative numbers. Absolute values and return statements.

---

### 10. a + b
**File:** `10-add.py`

**Prototype:** `def add(a, b):`

**Description:** Function that adds two integers and returns the result.

**Concept:** Simple function definition with parameters and return values.

---

### 11. a ^ b
**File:** `11-pow.py`

**Prototype:** `def pow(a, b):`

**Description:** Function that computes a to the power of b and returns the value.

**Concept:** Using the power operator in Python. Mathematical operations in functions.

---

### 12. Fizz Buzz
**File:** `12-fizzbuzz.py`

**Prototype:** `def fizzbuzz():`

**Description:** Function that prints numbers from 1 to 100 separated by space. For multiples of 3, print Fizz. For multiples of 5, print Buzz. For multiples of both, print FizzBuzz.

**Concept:** Classic programming interview problem. Using modulo to check divisibility. Multiple conditions.

---

### 13. Insert in sorted linked list
**File:** `13-insert_number.c`

**Prototype:** `listint_t *insert_node(listint_t **head, int number);`

**Description:** C function that inserts a number into a sorted singly linked list. Returns the address of the new node, or NULL if it failed.

**Concept:** Linked list manipulation in C. Memory allocation. Pointer operations. Maintaining sorted order during insertion.

---

## Compilation

**Python Scripts:**
All Python files are interpreted/compiled using python3 (version 3.8.5):
```bash
./0-positive_or_negative.py
python3 0-positive_or_negative.py
```

**C Programs:**
All C files are compiled using gcc with specific flags:
```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
./insert
```

## Resources

* [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (if, for, while, pass, range)
* [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
* [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [PEP 8 – Style Guide for Python Code](https://pep8.org/)

## Key Concepts Summary

**Control Flow:**
* `if`, `elif`, `else` - conditional execution
* `while` - loop while condition is true
* `for` - iterate over sequences
* `break` - exit loop early
* `continue` - skip to next iteration
* `pass` - placeholder for empty blocks

**Functions:**
* Defined with `def` keyword
* Parameters and return values
* Scope and variable lifetime

**Operators:**
* Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
* Comparison: `<`, `>`, `<=`, `>=`, `==`, `!=`
* Logical: `and`, `or`, `not`

**Data Types:**
* Integers (positive, negative, zero)
* Strings and character operations
* Boolean values (True/False)

## Author
@zolldic

## Note
This project is part of the ALX Higher Level Programming curriculum. The focus is on understanding fundamental Python programming concepts through hands-on practice. Take time to understand each concept rather than rushing through solutions.
