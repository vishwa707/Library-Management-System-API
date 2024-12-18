import os
import json
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Data is stored in-memory
data = {
    "books": [],
    "members": []
}

# Authentication Token
TOKEN = "alpha beta gamma"

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token != f"{TOKEN}":
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated_function

# Generate unique IDs
def generate_id(entity):
    return max([item["id"] for item in data[entity]] + [0]) + 1

# Default route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Library Management System API"}), 200

# Handles unnecessary browser requests
@app.route("/favicon.ico")
def favicon():
    return "", 204

# CRUD Operations for Books

# Add a Book
@app.route("/books", methods=["POST"])
@authenticate
def add_book():
    book = request.json
    book["id"] = generate_id("books")
    data["books"].append(book)
    return jsonify(book), 201

# Get All Books
@app.route("/books", methods=["GET"])
@authenticate
def get_books():
    search = request.args.get("search")
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))

    books = data["books"]

    # Search functionality
    if search:
        books = [
            {"id": b["id"], **{k: v for k, v in b.items() if k != "id"}} for b in books
            if search.lower() in b["title"].lower() or search.lower() in b["author"].lower()
        ]

    # Pagination
    start = (page - 1) * per_page
    end = start + per_page
    paginated_books = books[start:end]

    return jsonify({"books": paginated_books, "total": len(books)}), 200

# Get a Single Book
@app.route("/books/<int:book_id>", methods=["GET"])
@authenticate
def get_book(book_id):
    book = next((b for b in data["books"] if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

# Update a Book
@app.route("/books/<int:book_id>", methods=["PUT"])
@authenticate
def update_book(book_id):
    book = next((b for b in data["books"] if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    updated_data = request.json
    book.update(updated_data)
    return jsonify(book), 200

# Delete a Book
@app.route("/books/<int:book_id>", methods=["DELETE"])
@authenticate
def delete_book(book_id):
    book = next((b for b in data["books"] if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data["books"].remove(book)
    return jsonify({"message": "Book deleted"}), 200

# CRUD Operations for Members

# Add a member
@app.route("/members", methods=["POST"])
@authenticate
def add_member():
    member = request.json
    member["id"] = generate_id("members")
    data["members"].append(member)
    return jsonify(member), 201

# Get all members
@app.route("/members", methods=["GET"])
@authenticate
def get_members():
    return jsonify({"members": data["members"]}), 200

# Get a single member
@app.route("/members/<int:member_id>", methods=["GET"])
@authenticate
def get_member(member_id):
    member = next((m for m in data["members"] if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200

# Update a member
@app.route("/members/<int:member_id>", methods=["PUT"])
@authenticate
def update_member(member_id):
    member = next((m for m in data["members"] if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404

    updated_data = request.json
    member.update(updated_data)
    return jsonify(member), 200

# Delete a member
@app.route("/members/<int:member_id>", methods=["DELETE"])
@authenticate
def delete_member(member_id):
    member = next((m for m in data["members"] if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404

    data["members"].remove(member)
    return jsonify({"message": "Member deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
