# Program that prints numbers from 0 to 99

# number = 0
# while number <= 99: 
#     print("{:02d}, " .format(number))
#     number +=1

for number in range(100):
    if number != 99:
        print(number, end=", ")
    else: 
        print(number)
