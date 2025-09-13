#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of '.', '?', and ':'.

    Ensures no leading or trailing spaces on any printed line.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_spaces = True
    for char in text:
        if skip_spaces and char == ' ':
            continue

        skip_spaces = False

        print(char, end="")

        if char in ".?:":
            print("\n")
            skip_spaces = True
