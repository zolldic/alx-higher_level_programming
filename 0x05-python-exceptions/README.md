# Project Title
0x05. Python - Exceptions

## Brief Description
This project focuses on understanding and implementing exception handling in Python. It covers the fundamental concepts of errors and exceptions, how to catch and raise them, and the importance of proper error management in Python programming.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* Why Python programming is awesome
* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception

## Project Structure
The project is organized into several Python files, each addressing a specific aspect of exception handling. Each task typically involves a `.py` file containing the function implementation and a corresponding `main.py` file for testing.

```
.
├── 0-main.py
├── 0-safe_print_list.py
├── 1-main.py
├── 1-safe_print_integer.py
├── 2-main.py
├── 2-safe_print_list_integers.py
├── 3-main.py
├── 3-safe_print_division.py
├── 4-list_division.py
├── 4-main.py
├── 5-main.py
├── 5-raise_exception.py
├── 6-main.py
└── 6-raise_exception_msg.py
```

## Project Tasks

### 0. Safe list printing
*   **File**: `0-safe_print_list.py`
*   **Prototype**: `def safe_print_list(my_list=[], x=0):`
*   **Description**: Write a function that prints `x` elements of a list. `my_list` can contain any type. All elements must be printed on the same line followed by a new line. `x` can be bigger than the length of `my_list`. Returns the real number of elements printed. You have to use `try: / except:`. You are not allowed to import any module or use `len()`.
*   **Concept**: This task introduces basic exception handling using `try-except` blocks to gracefully manage `IndexError` when attempting to access list elements beyond its bounds, ensuring the program doesn't crash and returns a meaningful result.

### 1. Safe printing of an integers list
*   **File**: `1-safe_print_integer.py`
*   **Prototype**: `def safe_print_integer(value):`
*   **Description**: Write a function that prints an integer with `"{:d}".format()`. `value` can be any type. The integer should be printed followed by a new line. Returns `True` if `value` has been correctly printed (it means the `value` is an integer), otherwise, returns `False`. You have to use `try: / except:`. You have to use `"{:d}".format()` to print as integer. You are not allowed to import any module or use `type()`.
*   **Concept**: This task reinforces `try-except` usage for `ValueError` specifically, when trying to format a non-integer value as an integer, demonstrating how to validate input types without explicit type checking.

### 2. Print and count integers
*   **File**: `2-safe_print_list_integers.py`
*   **Prototype**: `def safe_print_list_integers(my_list=[], x=0):`
*   **Description**: Write a function that prints the first `x` elements of a list and only integers. `my_list` can contain any type. All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence). `x` represents the number of elements to access in `my_list`. `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur. Returns the real number of integers printed. You have to use `try: / except:`. You have to use `"{:d}".format()` to print an integer. You are not allowed to import any module or use `len()`.
*   **Concept**: This task combines handling `IndexError` and `ValueError` within a loop. It demonstrates selective processing of list elements, printing only valid integers while gracefully skipping others and handling out-of-bounds access.

### 3. Integers division with debug
*   **File**: `3-safe_print_division.py`
*   **Prototype**: `def safe_print_division(a, b):`
*   **Description**: Write a function that divides 2 integers and prints the result. You can assume that `a` and `b` are integers. The result of the division should print on the `finally:` section preceded by `Inside result:`. Returns the value of the division, otherwise: `None`. You have to use `try: / except: / finally:`. You have to use `"{:d}".format()` to print the result. You are not allowed to import any module.
*   **Concept**: This task introduces the `finally` block, demonstrating its use for cleanup actions or guaranteed execution regardless of whether an exception occurred or was handled, specifically for division by zero (`ZeroDivisionError`).

### 4. Divide a list
*   **File**: `4-list_division.py`
*   **Prototype**: `def list_division(my_list_1, my_list_2, list_length):`
*   **Description**: Write a function that divides element by element 2 lists. `my_list_1` and `my_list_2` can contain any type. `list_length` can be bigger than the length of both lists. Returns a new list (length = `list_length`) with all divisions. If 2 elements can’t be divided, the division result should be equal to `0`. If an element is not an integer or float, print: `wrong type`. If the division can’t be done (`/0`), print: `division by 0`. If `my_list_1` or `my_list_2` is too short, print: `out of range`. You have to use `try: / except: / finally:`. You are not allowed to import any module.
*   **Concept**: This comprehensive task requires handling multiple exception types (`TypeError`, `ZeroDivisionError`, `IndexError`) within a single function, demonstrating robust error management for complex operations involving multiple inputs.

### 5. Raise exception
*   **File**: `5-raise_exception.py`
*   **Prototype**: `def raise_exception():`
*   **Description**: Write a function that raises a type exception. You are not allowed to import any module.
*   **Concept**: This task focuses on explicitly raising exceptions using the `raise` keyword, specifically a `TypeError`, which is crucial for signaling invalid operations or states within a program.

### 6. Raise a message
*   **File**: `6-raise_exception_msg.py`
*   **Prototype**: `def raise_exception_msg(message=""):`
*   **Description**: Write a function that raises a name exception with a message. You are not allowed to import any module.
*   **Concept**: This task extends the concept of raising exceptions by demonstrating how to provide a custom error message when raising an exception, making debugging and error reporting more informative.

## Compilation
Python files are interpreted using `python3`. C files are compiled using `gcc`.

Example for Python scripts:
```bash
python3 0-main.py
```

## Resources
*   [Errors and Exceptions](https://savanna.alxafrica.com/rltoken/Yj7sDOzmKwICSHr7WEAW3A)
*   [Learn to Program 11 Static & Exception Handling](https://savanna.alxafrica.com/rltoken/xASzXarhF1sBhzYkJ14LvQ) (starting at minute 7)
*   [Python bytecode](https://savanna.alxafrica.com/rltoken/-eivu0w172OUPm-iCeKgtw)

## Key Concepts Summary
This project focuses on Python's robust error and exception handling mechanisms. Key concepts include:
*   **Errors vs. Exceptions**: Understanding the distinction between syntax errors, which prevent code execution, and exceptions, which occur during runtime and can be handled.
*   **`try`, `except`, `else`, `finally`**: Mastering the use of these blocks for controlled execution, error catching, code execution when no exceptions occur, and guaranteed cleanup operations.
*   **Raising Exceptions**: Learning how to explicitly raise built-in or custom exceptions using the `raise` keyword to signal problematic situations.
*   **Specific Exception Types**: Recognizing and handling common Python exceptions like `TypeError`, `ValueError`, `ZeroDivisionError`, and `IndexError`.
*   **Error Logging**: Directing error messages to `stderr` for better debugging and system monitoring.
*   **Python C API**: For advanced tasks, understanding how to interact with Python objects from C, demonstrating the extensibility of Python and its underlying architecture.

## Author
@zolldic
