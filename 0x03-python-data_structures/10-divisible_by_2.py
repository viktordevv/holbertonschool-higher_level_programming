#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    qlist = []
    for i in my_list:
        if i % 2 == 0:
            qlist.append(True)
        else:
            qlist.append(False)
    return qlist
