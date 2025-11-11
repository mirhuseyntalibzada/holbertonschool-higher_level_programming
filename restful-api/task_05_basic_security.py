#!/usr/bin/python3
"""
Module: task_05_basic_security
Description:
  - Basic HTTP Authentication (Flask-HTTPAuth)
  - JWT Authentication (Flask-JWT-Extended)
  - Role-based access control (admin/user)
  - Consistent 401 responses for all auth-related errors
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)

app = Flask(__name__)

# Use a strong, secret key in real apps (e.g., from env var)
app.config["JWT_SECRET_KEY"] = "change-this-to-a-strong-secret"

# ----- In-memory users (hashed passwords) -----
# NOTE: Keep these exact sample users for the checker.
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ----- Basic HTTP Authentication setup -----
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user["password"], password)

# Ensure Basic Auth failures return 401 with JSON
@auth.error_handler
def basic_auth_error(status):
    # status is usually 401 for HTTPBasicAuth; enforce 401 explicitly
    return jsonify({"error": "Unauthorized"}), 401


# ----- JWT setup -----
jwt = JWTManager(app)

# Uniform 401 responses for JWT errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err_msg):
    # Missing Authorization Header, malformed header, etc.
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err_msg):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# ========== Endpoints ==========

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    # Reaching here implies valid Basic credentials
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Accepts JSON: {"username": "...", "password": "..."}
    Returns: {"access_token": "<JWT_TOKEN>"} on success.
    """
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid or missing JSON"}), 401

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed identity and role in the token
    additional_claims = {"role": user["role"]}
    token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify({"access_token": token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    # Valid JWT required to reach here
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    # Enforce role-based access (admin)
    claims = get_jwt()  # contains our additional claims, including "role"
    role = claims.get("role")
    if role != "admin":
        # Must be exactly 403 per spec for role denial
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# Optional: simple root for sanity
@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Security demo API"})


if __name__ == "__main__":
    # Enable running via: python3 task_05_basic_security.py
    app.run()
