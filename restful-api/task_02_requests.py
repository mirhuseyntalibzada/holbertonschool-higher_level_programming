#!/usr/bin/python3
"""
Module: task_02_requests
Description: Demonstrates how to use the requests library to fetch,
process, and save data from a public API (JSONPlaceholder).
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the HTTP status code
    print(f"Status Code: {response.status_code}")

    # Proceed only if the request was successful (status code 200)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """Fetch all posts and save them into a CSV file (posts.csv)."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Prepare data for CSV
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Define CSV filename
        filename = "posts.csv"

        # Write data to CSV
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)

        print(f"Data successfully saved to {filename}")
    else:
        print("Failed to fetch posts.")
