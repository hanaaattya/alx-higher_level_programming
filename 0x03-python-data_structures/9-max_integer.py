#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    list_cpy = my_list.copy()
    list_cpy.sort()
    return list_cpy[-1]
