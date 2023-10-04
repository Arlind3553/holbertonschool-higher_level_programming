#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    numbers = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    value = 0
    for i in range(len(roman_string) - 1):
        if numbers[roman_string[i]] < numbers[roman_string[i+1]]:
            value -= numbers[roman_string[i]]
        else:
            value += numbers[roman_string[i]]
    value += numbers[roman_string[-1]]
    return value
