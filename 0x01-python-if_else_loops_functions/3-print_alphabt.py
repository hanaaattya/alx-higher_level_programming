#!/usr/bin/python3
for num in range(ord('a'), ord('z') + 1):
    if num != ord('e') and num != ord('q'):
        print("{:c}".format(num), end="")
