from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for users
users = {}

@app.route("/")
def home():
    return {"message": "API working!"}

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data["username"]
    password = data["password"]

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = password
    return jsonify({"message": "Signup successful!"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    if users.get(username) == password:
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid credentials"}), 404

@app.route("/users", methods=["GET"])
def get_users():
    """Endpoint to get all registered users"""
    # Convert the users dictionary to a list of usernames
    user_list = list(users.keys())
    return jsonify({"users": user_list, "count": len(user_list)})
