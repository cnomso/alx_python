#Write a Python function called is_prime that takes a number as input and returns True if the number is prime, and False otherwise.

def is_prime(number):
    
    if number <= 1:
        return False
         
    for prime in range(2, int(number ** 0.5) + 1):
        if number % prime == 0:
            return False

    return True