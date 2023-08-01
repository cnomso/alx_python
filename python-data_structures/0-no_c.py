#Write a function that removes all characters c and C from a string.

def no_c(my_string):
    noC = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            noC += char

    return noC