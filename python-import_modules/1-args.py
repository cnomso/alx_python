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

    print("Number of argument(s): {}" .format(num_arguments), end="")
    if num_arguments == 0:
        print(".")
    else:
        print(", followed by:\n")

        for i, arg in enumerate(arguments, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()