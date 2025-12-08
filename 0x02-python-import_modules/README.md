# 0x02. Python - import & modules

This project explores Python's module system and how to import functions from other files. It covers command-line arguments, preventing code execution during import, and discovering module contents programmatically.

## Learning Objectives

By the end of this project, you should understand:

* Why Python programming is powerful and flexible
* How to import functions from another file
* How to use imported functions in your code
* How to create and structure modules
* How to use the built-in function `dir()`
* How to prevent code from being executed when imported
* How to use command line arguments with your Python programs
* The difference between `import` statements and `from...import` syntax
* How `sys.argv` works for accessing command-line arguments

## Project Structure

The project contains Python scripts that demonstrate various import techniques:

* Module files: `add_0.py`, `calculator_1.py`, `variable_load_5.py`, `hidden_4.pyc`
* Task implementation files: numbered scripts from `0-add.py` to `5-variable_load.py`

## Project Tasks

### Task 0: Import a simple function from a simple file
**File:** `0-add.py`

Import the function `add(a, b)` from `add_0.py` and print the result of adding 1 and 2.

**Concept:** Basic function import using `from module import function`. The program must only execute when run directly, not when imported. This is controlled using `if __name__ == '__main__'`.

---

### Task 1: My first toolbox
**File:** `1-calculation.py`

Import functions `add`, `sub`, `mul`, and `div` from `calculator_1.py` and perform basic arithmetic operations on two variables.

**Concept:** Importing multiple functions from a single module in one line. Each function is called to demonstrate the four basic arithmetic operations with formatted output.

---

### Task 2: How to make a script dynamic
**File:** `2-args.py`

Print the number of command-line arguments and their values.

**Concept:** Using `sys.argv` to access command-line arguments. The list includes the script name at index 0. The script demonstrates dynamic behavior based on user input, handling singular/plural forms and different argument counts.

---

### Task 3: Infinite addition
**File:** `3-infinite_add.py`

Print the sum of all command-line arguments (integers).

**Concept:** Iterating through `sys.argv` to process variable numbers of arguments. This shows how to convert string arguments to integers and accumulate results. The import is placed inside the guard clause to demonstrate another import pattern.

---

### Task 4: Who are you?
**File:** `4-hidden_discovery.py`

Print all names defined by the compiled module `hidden_4.pyc`, excluding those starting with `__`.

**Concept:** Using the `dir()` function to introspect module contents. This demonstrates how to discover what a module contains programmatically, filtering out private/magic attributes.

---

### Task 5: Everything can be imported
**File:** `5-variable_load.py`

Import a variable `a` from `variable_load_5.py` and print its value.

**Concept:** Variables can be imported just like functions. The import statement is placed inside the execution guard, showing that imports can happen conditionally. This demonstrates Python's flexibility in what can be shared between modules.

---

## Compilation

Python scripts do not need compilation. Run them directly with the Python interpreter:

```bash
# Task 0
./0-add.py

# Task 1
./1-calculation.py

# Task 2 - with various arguments
./2-args.py
./2-args.py Hello
./2-args.py Hello World

# Task 3 - adding numbers
./3-infinite_add.py 5 10 15
./3-infinite_add.py 100 200

# Task 4
./4-hidden_discovery.py

# Task 5
./5-variable_load.py
```

Make sure scripts have execute permissions:
```bash
chmod +x *.py
```

## Resources

* [Modules - Python Official Documentation](https://docs.python.org/3/tutorial/modules.html)
* [Command line arguments in Python](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
* [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [Python's dir() function](https://docs.python.org/3/library/functions.html#dir)
* [Python sys module](https://docs.python.org/3/library/sys.html)

## Key Concepts Summary

**Module Import Patterns:**
* `import module` - imports entire module
* `from module import function` - imports specific function
* `from module import *` - imports everything (not recommended)

**Execution Guard:**
The `if __name__ == '__main__':` pattern ensures code only runs when the script is executed directly, not when imported as a module.

**Command-Line Arguments:**
`sys.argv` is a list where `sys.argv[0]` is the script name and `sys.argv[1:]` contains the arguments passed by the user.

**Module Introspection:**
The `dir()` function returns a list of all attributes and methods in a module, useful for exploring unfamiliar code.

## Author

@zolldic

---

**Note:** This project focuses on understanding Python's import system and module structure. Take time to experiment with different import patterns and understand why `__name__ == '__main__'` is important for creating reusable code.
