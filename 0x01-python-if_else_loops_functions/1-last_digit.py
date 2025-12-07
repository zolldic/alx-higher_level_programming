#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = (number * -1) % 10
    last *= -1
    str = f"Last digit of {number} is {last} "
else:
    last = number % 10
    str = f"Last digit of {number} is {last} "

if last > 5:
    str += "and is greater than 5"
elif last == 0:
    str += "and is 0"
else:
    str += "and is less than 6 and not 0"
print(str)
