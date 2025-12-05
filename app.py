from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}  # Demo ke liye (production me database use karein)

@app.route("/")
def home():
    return {"message": "API is working!"}

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = password
    return jsonify({"message": "Signup successful"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify({"message": "Login successful"})
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run()
