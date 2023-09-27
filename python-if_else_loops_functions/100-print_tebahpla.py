#!/usr/bin/python3
i = 122
j = 89
while i >= 97 and j >= 65:
    print("{}{}".format(chr(i), chr(j)), end="")
    i = i - 2
    j = j - 2
