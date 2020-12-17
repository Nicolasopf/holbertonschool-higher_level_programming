#!/usr/bin/python3
def search_replace(my_list, search, replace):
    tmp = my_list.copy()
    for i in range(len(tmp)):
        if tmp[i] == search:
            tmp[i] = replace
    return tmp
