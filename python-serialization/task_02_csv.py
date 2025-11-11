#!/usr/bin/python3
"""Converts CSV data into JSON format and saves it to data.json."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file into a JSON file named data.json.

    Args:
        csv_filename (str): The name of the CSV file to read.

    Returns:
        bool: True if conversion succeeds, False otherwise.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
