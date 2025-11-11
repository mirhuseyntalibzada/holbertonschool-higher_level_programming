#!/usr/bin/python3
"""
Module: task_04_flask
Description: Minimal Flask API demonstrating routes, JSON responses,
and handling POST requests to add data (in-memory).
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store (do NOT pre-populate with test data)
# username -> full user object
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Health/status endpoint."""
    return "OK"


@app.route("/data", methods=["GET"])
def list_usernames():
    """
    Return a JSON list of all usernames in the API.
    Example: ["jane", "john"]
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Return the full object for the given username, or 404 if not found.
    """
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Accept JSON, require 'username', add user to in-memory store,
    and return confirmation with 201 status.
    Expected JSON example:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    """
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid or missing JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Ensure stored object contains 'username' as well
    user_obj = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    users[username] = user_obj
    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    # Enable running via: python3 task_04_flask.py
    app.run()
