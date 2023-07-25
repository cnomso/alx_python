#Write a program that prints all possible different combinations of two digits. 

for numberone in range(10):
    for numbertwo in range(10):
        print ("{}{}, " .format(numberone, numbertwo), end="")
    # if
    # else:
    #     print(numberone,numbertwo)