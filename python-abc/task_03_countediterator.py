#!/usr/bin/python3

class CountedIterator():
    def __init__(self, obj):
        self.__iter = iter(obj)
        self.__count = 0

    def get_count(self):
        return (self.__count)

    def __next__(self):
        item = next(self.__iter)
        self.__count += 1
        return (item)
