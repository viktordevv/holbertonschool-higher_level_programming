#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    if idx in range(len(my_list)):
        my_list[idx] = element
        return my_list
    elif idx in range(-len(my_list), -1):
        return my_list
