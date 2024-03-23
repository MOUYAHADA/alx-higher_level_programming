#!/usr/bin/python3


def weight_average(my_list=[]):
    """Returns weighted average of all integers tuple (<score>, <weight>)"""
    if not my_list:
        return 0
    return sum(list(map(lambda x: x[0] * x[1], my_list))) / sum(
        list(map(lambda x: x[1], my_list))
    )
