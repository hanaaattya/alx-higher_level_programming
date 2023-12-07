#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        tot_score = sum(score * weight for score, weight in my_list)
        tot_weight = sum(weight for _, weight in my_list)
        return tot_score / tot_weight
