#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

print(__import__("0-square").__doc__)
print(__import__("0-square").Square.__doc__)
# print(__import__("my_module").__init__.__doc__)