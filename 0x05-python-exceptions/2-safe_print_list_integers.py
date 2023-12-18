#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c, index = 0, 0
    while c < x:
         try:
            print("{:d}".format(my_list[i]), end="")
            c += 1
            except (IndexError, TypeError):
                pass
            index += 1
        print()
        return c
