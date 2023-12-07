#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        tot_score = sum(a * b for a, b in my_list)
        tot_weight = sum(b for a, b in my_list)
        return tot_score / tot_weight
