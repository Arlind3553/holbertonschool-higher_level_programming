#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNum = abs(number) % 10
if number < 0:
    lastNum = lastNum* -1
if lastNum > 5:
    print(f"Last digit of {number} is {lastNum} and is greater than 5")
elif lastNum == 0:
    print(f"Last digit of {number} is {lastNum} and is 0")
else:
    print(f"Last digi of {number} is {lastNum} and is less than 6 and not 0")
