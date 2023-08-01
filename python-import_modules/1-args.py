#!/usr/bin/python3

import sys

# filename = None
# starting_point = 0 

# if len(sys.argv) < 2:
#     print("Needs at least one argument: <filename>")
#     exit()

# filename = sys.argv[1]

# for idx, arg in enumerate(sys.argv):
#     if arg in ("--start", "-s"):
#         starting_point = int(sys.argv[idx + 1])

# print("Filename:", filename)
# print("start:", starting_point)

# with open(filename, "rb") as f: 
#     f.seek(starting_point)
    # file = f.read()


def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    if num_arguments > 1:
        print("{} arguments:" .format(num_arguments), end="")
    elif num_arguments == 0:
         print("{} arguments:" .format(num_arguments), end="")    
    else:
        print("{} argument:" .format(num_arguments), end="")
    if num_arguments == 0:
        print(".")
    else:
        print(end="\n")
        for i, arg in enumerate(arguments, 1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()