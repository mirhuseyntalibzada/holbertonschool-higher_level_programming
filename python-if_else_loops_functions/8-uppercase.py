#!/usr/bin/python3

def uppercase(str):
    result = ""

    for i in str:
        if 97 <= ord(i) <= 122:
            result += chr(ord(i) - 32)
        else:
            result += i

    print(result, end="\n")
