#!/usr/bin/python3
"""Module for serializing and deserializing Python dictionaries using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename where XML data will be saved.
    """
    try:
        # Create root element <data>
        root = ET.Element("data")

        # Add each key-value pair as a child element
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Create the XML tree and write it to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)
    except Exception:
        return None


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The filename of the XML file to read.

    Returns:
        dict: A dictionary reconstructed from the XML data,
              or an empty dict if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}

        for child in root:
            data[child.tag] = child.text

        return data
    except Exception:
        return {}
