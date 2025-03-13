from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# MongoDB config
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://mongo:27017/loginapp")
mongo = PyMongo(app)
users_collection = mongo.db.users

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    existing_user = users_collection.find_one({"username": data['username']})
    if existing_user:
        return jsonify({"message": "User already exists"}), 409
    users_collection.insert_one({
        "username": data['username'],
        "password": data['password']
    })
    return jsonify({"message": "User created!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users_collection.find_one({
        "username": data['username'],
        "password": data['password']
    })
    if user:
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
