#!/usr/bin/python3
"""
This module defines a function that reads a text file (UTF8)
and prints its contents to standard output.
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
