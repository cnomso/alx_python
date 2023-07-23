#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digi = number % 10

if last_digi > 5: 
    print('The Last digit of {0} is {1} and is greater than 5' .format(number, last_digi))

if last_digi < 6 and last_digi !=0: 
    print('The Last digit of {0} is {1} and is less than 6 and not 0' .format(number, last_digi))

if last_digi == 0: 
    print('The Last digit of {0} is {1} and is greater than 5' .format(number, last_digi))
