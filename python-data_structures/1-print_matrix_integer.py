#Write a function that prints a matrix of integers.


def print_matrix_integer(matrix=[[]]):
     for row in matrix:
        for i, num in enumerate(row):
            if i < len(row) - 1:
                print("{:d} ".format(num), end="")
            else:
                print("{:d}".format(num))
     if not matrix:
        print()