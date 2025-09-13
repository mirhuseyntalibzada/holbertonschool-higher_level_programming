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

    # Use a flag to know when to skip leading spaces on a new line
    skip_spaces = True
    for char in text:
        # If we are in "skip mode" and the character is a space, ignore it
        if skip_spaces and char == ' ':
            continue
        
        # If we encounter any other character, turn off "skip mode"
        skip_spaces = False
        
        # Print the character without a newline
        print(char, end="")
        
        # If the character is a delimiter, print two newlines
        # and turn "skip mode" back on for the next line.
        if char in ".?:":
            print("\n") # print() adds one \n, the "\n" character is the second.
            skip_spaces = True
