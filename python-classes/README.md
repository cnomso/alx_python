Python - Classes and Objects
Python
OOP
=====================================================================
=====================================================================

Requirements
----------------------------------
General
----------------
- Recommended text editor: Visual studio code
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)



=====================================================================
Tasks
=====================================================================

0. Square with size
mandatory
--------
Write a class Square that defines a square by:

- Private instance attribute: size
- Instantiation with size (no type/value verification)
- You are not allowed to import any module

1. Size validation
mandatory
---------
Write a class Square that defines a square by: (based on 0-square.py)

- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
- You are not allowed to import any module

2. Area of a square
mandatory
---------
Write a class Square that defines a square by: (based on 1-square.py)

- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module

3. Access and update private attribute
mandatory
---------
Write a class Square that defines a square by: (based on 2-square.py)

- Private instance attribute: size:
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
        - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module

4. Printing a square
mandatory
---------
Write a class Square that defines a square by: (based on 3-square.py)

- Private instance attribute: size:
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
        - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:
    - if size is equal to 0, print an empty line
- You are not allowed to import any module