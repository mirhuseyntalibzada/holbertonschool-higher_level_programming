#!/usr/bin/python3
"""Defines a CustomObject class with pickle-based serialization
and deserialization methods.
"""
import pickle


class CustomObject:
    """A class representing a custom object with basic attributes."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the CustomObject."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object and save it to a file.

        Args:
            filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a pickle file.

        Args:
            filename (str): The name of the file containing the serialized data.

        Returns:
            CustomObject | None: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
