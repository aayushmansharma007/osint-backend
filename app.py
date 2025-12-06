from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for users with credits
users = {}  # Format: {username: {"password": "hashed_pw", "credits": 0}}

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

    users[username] = {"password": password, "credits": 10}  # Initialize with 10 credits
    return jsonify({"message": "Signup successful!"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    user = users.get(username)
    if user and user["password"] == password:
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid credentials"}), 404

@app.route("/<username>/credit", methods=["GET"])
def get_user_credit(username):
    """Endpoint to get a specific user's credit"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        "username": username,
        "credits": users[username]["credits"]
    })

@app.route("/users", methods=["GET"])
def get_users():
    """Endpoint to get all registered users with their data"""
    return jsonify({
        "users": [{"username": user, "password": data["password"], "credits": data["credits"]} for user, data in users.items()],
        "count": len(users)
    })
