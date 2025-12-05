from flask import Flask, request, jsonify

app = Flask(__name__)

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
