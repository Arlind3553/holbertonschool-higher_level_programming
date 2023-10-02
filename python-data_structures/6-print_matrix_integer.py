#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for columns in row:
            print("{}".format(columns), end="")
            if row.index(columns) != len(row) - 1:
                print(" ", end="")
        print()
