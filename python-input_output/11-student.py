#!/usr/bin/python3
"""Defines a Student class with JSON-style serialization helpers."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.

        If `attrs` is a list of strings, only keys listed in `attrs` that
        exist as attributes on the instance are returned. Otherwise, return
        all public attributes.

        Args:
            attrs (list|None): Optional list of attribute names (strings).

        Returns:
            dict: Serialized dictionary of the student's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return dict(self.__dict__)

    def reload_from_json(self, json):
        """Replace all attributes of the Student from a dictionary.

        Args:
            json (dict): Keys are attribute names; values are the new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
