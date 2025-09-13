#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from. Can contain any type.
        x (int): The number of elements to access from my_list.

    Returns:
        The real number of integers printed.
    """
    integers_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            integers_printed += 1
        except (ValueError, TypeError):
            continue
    print()
    return integers_printed
