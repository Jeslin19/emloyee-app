
from flask import Flask, jsonify

app = Flask(__name__)

departments = [
    {"id": 1, "name": "IT"},
    {"id": 2, "name": "HR"},
    {"id": 3, "name": "Finance"}
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Department Service"})

@app.route("/departments")
def get_departments():
    return jsonify(departments)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

