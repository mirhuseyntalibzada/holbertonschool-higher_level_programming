#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = []
    for num in my_list:
        if num not in unique_elements:
            unique_elements.append(num)
    return sum(unique_elements)
