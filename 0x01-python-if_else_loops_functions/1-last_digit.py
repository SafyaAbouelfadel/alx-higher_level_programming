#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10
if number < 0:
    last_number = -last_number
print("Last digit of {} is {}".format(number, last_number), end=" ")
if last_number > 5:
    print("and is greater than 5")
elif last_number == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
