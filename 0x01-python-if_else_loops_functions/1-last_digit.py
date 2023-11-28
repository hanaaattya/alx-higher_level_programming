#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = number % 10 if number >= 10 else number % -10
print(f"Last digit of {number} is {LastDigit}", end=" ")
if LastDigit == 0:
    print("and is 0")
elif LastDigit > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
