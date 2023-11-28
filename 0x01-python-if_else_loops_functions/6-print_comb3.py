#!/usr/bin/python3
for num_1 in range(10):
    for num_2 in range(num_1 + 1, 10):
        print("{:d}{:d}".format(num_1, num_2), end=", " if num_1 < 8 or num_2 < 9 else "\n")

