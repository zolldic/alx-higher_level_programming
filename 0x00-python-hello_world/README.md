# 0x00. Python - Hello, World

This project introduces the fundamentals of Python programming, covering basic syntax, string manipulation, the Python interpreter, and coding style conventions.

## Learning Objectives

At the end of this project, you should be able to explain:

- Why Python programming is awesome
- Who created Python and who is Guido van Rossum
- Where does the name 'Python' come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with pycodestyle

## Project Structure

- **Python Scripts**: Using Python 3.8.5 on Ubuntu 20.04 LTS
- **Shell Scripts**: Bash scripts for running Python code
- **C Files**: Function to detect cycles in linked lists
- **Header File**: `lists.h` for C function prototypes

## Completed Tasks

### Task 0: Run Python file
- **File**: `0-run`
- **Description**: Write a Shell script that runs a Python script
- **Concept**: The script uses the environment variable `$PYFILE` to execute Python files

### Task 1: Run inline
- **File**: `1-run_inline`
- **Description**: Write a Shell script that runs Python code
- **Concept**: Using the `-c` flag to run Python code directly from the command line via the `$PYCODE` environment variable

### Task 2: Hello, print
- **File**: `2-print.py`
- **Description**: Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line
- **Concept**: Using the `print()` function to output text with proper escaping

### Task 3: Print integer
- **File**: `3-print_number.py`
- **Description**: Complete source code to print an integer stored in a variable
- **Concept**: String formatting with f-strings to display integers

### Task 4: Print float
- **File**: `4-print_float.py`
- **Description**: Complete source code to print a float with a precision of 2 digits
- **Concept**: Float formatting using f-string precision specifiers

### Task 5: Print string
- **File**: `5-print_string.py`
- **Description**: Print a string 3 times, then print its first 9 characters
- **Concept**: String repetition and slicing operations in Python

### Task 6: Play with strings
- **File**: `6-concat.py`
- **Description**: Concatenate two strings to form "Welcome to Holberton School!"
- **Concept**: String concatenation without using loops or conditionals

### Task 7: Copy - Cut - Paste
- **File**: `7-edges.py`
- **Description**: Extract specific portions of a string using slicing
- **Concept**: String slicing with positive and negative indices

### Task 8: Create a new sentence
- **File**: `8-concat_edges.py`
- **Description**: Print "object-oriented programming with Python" by slicing a given string
- **Concept**: Advanced string slicing and concatenation

### Task 9: Easter Egg
- **File**: `9-easter_egg.py`
- **Description**: Write a Python script that prints "The Zen of Python" by Tim Peters
- **Concept**: Python's hidden easter egg using `import this`

### Task 10: Linked list cycle
- **Files**: `10-check_cycle.c`, `lists.h`
- **Description**: Write a function in C that checks if a singly linked list has a cycle in it
- **Prototype**: `int check_cycle(listint_t *list);`
- **Concept**: Floyd's cycle-finding algorithm (tortoise and hare) to detect cycles in linked lists

## Compilation

### Python Scripts
```bash
# Make scripts executable
chmod +x <filename>.py

# Run Python scripts
./<filename>.py
```

### Shell Scripts
```bash
# Make scripts executable
chmod +x <filename>

# Run with environment variable
export PYFILE=main.py
./0-run

export PYCODE='print(f"Best School: {88+10}")'
./1-run_inline
```

### C Files
```bash
# Compile with gcc
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle

# Run
./cycle
```

## Resources

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) (first three chapters)
- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
- [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
- [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [Pycodestyle – Style Guide for Python Code](https://pycodestyle.pycqa.org/en/latest/)

## Key Concepts Summary

**The Zen of Python**: A collection of 19 guiding principles for writing computer programs in Python. Access it with `import this`.

**String Operations**: Python provides powerful string manipulation through slicing `[start:end]`, concatenation with `+`, and repetition with `*`.

**Print Function**: The built-in `print()` function outputs text to stdout. Use f-strings for formatted output: `f"{variable}"`.

**Pycodestyle**: The official Python style guide checker (PEP 8) ensuring code readability and consistency.

## Author

@zolldic

## Note

This project emphasizes learning by doing. Understanding these fundamentals builds a strong foundation for Python programming. Focus on comprehension rather than completion.
