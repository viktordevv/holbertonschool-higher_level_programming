#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    nux = min(my_list)
    for i in my_list:
        if i > nux:
            nux = i

    return nux
