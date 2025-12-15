# 0x04. Python - More Data Structures: Set, Dictionary

This project focuses on advanced Python data structures: sets and dictionaries. It covers their creation, manipulation, and appropriate use cases, along with an introduction to lambda functions and the `map`, `reduce`, and `filter` functions.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
*   Why Python programming is awesome
*   What are sets and how to use them
*   What are the most common methods of set and how to use them
*   When to use sets versus lists
*   How to iterate into a set
*   What are dictionaries and how to use them
*   When to use dictionaries versus lists or sets
*   What is a key in a dictionary
*   How to iterate over a dictionary
*   What is a lambda function
*   What are the map, reduce and filter functions

## Project Structure

This repository contains Python files, each addressing a specific task related to sets, dictionaries, and functional programming concepts.

## Project Tasks

### 0. Squared simple
*   **File:** `0-square_matrix_simple.py`
*   **Prototype:** `def square_matrix_simple(matrix=[]):`
*   **Description:** Write a function that computes the square value of all integers of a matrix.
*   **Concept:** This task introduces basic matrix manipulation and iteration in Python, emphasizing the creation of a new matrix without modifying the original.

### 1. Search and replace
*   **File:** `1-search_replace.py`
*   **Prototype:** `def search_replace(my_list, search, replace):`
*   **Description:** Write a function that replaces all occurrences of an element by another in a new list.
*   **Concept:** This task focuses on list manipulation, specifically replacing elements, while ensuring the original list remains unchanged.

### 2. Unique addition
*   **File:** `2-uniq_add.py`
*   **Prototype:** `def uniq_add(my_list=[]):`
*   **Description:** Write a function that adds all unique integers in a list (only once for each integer).
*   **Concept:** This task introduces the concept of uniqueness in a list and how to sum only distinct elements, implicitly touching upon the use of sets or similar logic.

### 3. Present in both
*   **File:** `3-common_elements.py`
*   **Prototype:** `def common_elements(set_1, set_2):`
*   **Description:** Write a function that returns a set of common elements in two sets.
*   **Concept:** This task explores set operations, specifically finding the intersection of two sets.

### 4. Only differents
*   **File:** `4-only_diff_elements.py`
*   **Prototype:** `def only_diff_elements(set_1, set_2):`
*   **Description:** Write a function that returns a set of all elements present in only one set.
*   **Concept:** This task focuses on symmetric difference operation between two sets.

### 5. Number of keys
*   **File:** `5-number_keys.py`
*   **Prototype:** `def number_keys(a_dictionary):`
*   **Description:** Write a function that returns the number of keys in a dictionary.
*   **Concept:** This task introduces basic dictionary property access to determine its size.

### 6. Print sorted dictionary
*   **File:** `6-print_sorted_dictionary.py`
*   **Prototype:** `def print_sorted_dictionary(a_dictionary):`
*   **Description:** Write a function that prints a dictionary by ordered keys.
*   **Concept:** This task involves iterating through a dictionary and printing its contents, with an emphasis on sorting keys alphabetically.

### 7. Update dictionary
*   **File:** `7-update_dictionary.py`
*   **Prototype:** `def update_dictionary(a_dictionary, key, value):`
*   **Description:** Write a function that replaces or adds key/value in a dictionary.
*   **Concept:** This task covers the dynamic nature of dictionaries, specifically how to add new key-value pairs or update existing ones.

### 8. Simple delete by key
*   **File:** `8-simple_delete.py`
*   **Prototype:** `def simple_delete(a_dictionary, key=""):`
*   **Description:** Write a function that deletes a key in a dictionary.
*   **Concept:** This task focuses on removing elements from a dictionary based on their key.

### 9. Multiply by 2
*   **File:** `9-multiply_by_2.py`
*   **Prototype:** `def multiply_by_2(a_dictionary):`
*   **Description:** Write a function that returns a new dictionary with all values multiplied by 2.
*   **Concept:** This task involves iterating through a dictionary's values and transforming them to create a new dictionary.

### 10. Best score
*   **File:** `10-best_score.py`
*   **Prototype:** `def best_score(a_dictionary):`
*   **Description:** Write a function that returns a key with the biggest integer value.
*   **Concept:** This task focuses on finding the maximum value in a dictionary and returning its corresponding key.

### 11. Multiply by using map
*   **File:** `11-multiply_list_map.py`
*   **Prototype:** `def multiply_list_map(my_list=[], number=0):`
*   **Description:** Write a function that returns a list with all values multiplied by a number without using any loops, utilizing `map`.
*   **Concept:** Introduces functional programming with `map` for list transformation.

### 12. Roman to Integer
*   **File:** `12-roman_to_int.py`
*   **Prototype:** `def roman_to_int(roman_string):`
*   **Description:** Converts a Roman numeral to an integer.
*   **Concept:** This technical interview preparation task requires understanding Roman numeral rules and string manipulation.

### 13. Weighted average!
*   **File:** `100-weight_average.py`
*   **Prototype:** `def weight_average(my_list=[]):`
*   **Description:** Write a function that returns the weighted average of all integers tuple `(<score>, <weight>)`.
*   **Concept:** This advanced task involves calculations on lists of tuples to determine a weighted average.

### 14. Squared by using map
*   **File:** `101-square_matrix_map.py`
*   **Prototype:** `def square_matrix_map(matrix=[]):`
*   **Description:** Write a function that computes the square value of all integers of a matrix using `map`.
*   **Concept:** This advanced task revisits matrix squaring but mandates the use of the `map` function, disallowing explicit loops.

### 15. Delete by value
*   **File:** `102-complex_delete.py`
*   **Prototype:** `def complex_delete(a_dictionary, value):`
*   **Description:** Write a function that deletes keys with a specific value in a dictionary.
*   **Concept:** This advanced task involves iterating through dictionary items to find and delete keys based on their associated values.

### 16. CPython #1: PyBytesObject
*   **File:** `103-python.c`
*   **Prototype:** `void print_python_list(PyObject *p);` and `void print_python_bytes(PyObject *p);`
*   **Description:** Create two C functions that print some basic info about Python lists and Python bytes objects, directly interacting with the CPython API.
*   **Concept:** This advanced task delves into the CPython internals, demonstrating how Python objects are represented in C and how to interact with them at a low level.

## Compilation

*   All Python files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
*   The C file for task 16 will be compiled with:
    ```bash
    gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
    ```

## Resources
*   [Data structures](https://savanna.alxafrica.com/rltoken/GmgoSUtBbHBW8suWkws51g)
*   [Lambda, filter, reduce and map](https://savanna.alxafrica.com/rltoken/53f4kKVT0-jyzrJstOSJWg)
*   [Learn to Program 12 Lambda Map Filter Reduce](https://savanna.alxafrica.com/rltoken/v9eyFryhkYmxDI13iTx2VA)
*   `python3` man page

## Key Concepts Summary

This project reinforces understanding of fundamental Python data structures like lists, sets, and dictionaries. It also introduces higher-order functions (`map`, `filter`, `reduce`) and lambda expressions for more concise and functional programming. Finally, it provides a glimpse into CPython internals by requiring direct C code interaction with Python objects, deepening the understanding of how Python works under the hood.

## Author
@zolldic

## Note
The goal of this project is to learn and understand Python's data structures and functional programming paradigms. Focus on grasping the underlying concepts rather than simply copying solutions.
