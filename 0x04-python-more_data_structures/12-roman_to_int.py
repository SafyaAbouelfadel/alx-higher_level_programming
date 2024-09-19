#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    result = 0
    number = 0
    roman = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for k in reversed(roman_string):
        num = digits[k]
        result += number if (total < number * 5) else -number
    return result
