# Program that gives numbers from 0 to 99

for number in range(100):
    if number != 99:
        print("{:02d}, " .format(number), end="")
    else: 
        print(number)
