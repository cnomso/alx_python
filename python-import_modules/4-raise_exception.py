#a function that raises a type exception.

def raise_exception():
    value = "Hello, ALX"
    if not isinstance(value, int):
        raise TypeError("Expected an integer, but got '{}' instead.".format(value))
        