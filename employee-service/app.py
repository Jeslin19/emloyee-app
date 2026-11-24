
from flask import Flask, jsonify
import os

app = Flask(__name__)

SERVICE_NAME = os.getenv("SERVICE_NAME", "Employee Service")
ENVIRONMENT = os.getenv("ENVIRONMENT", "Development")

employees = [
    {
        "id": 1,
        "name": "John",
        "department": "IT"
    },
    {
        "id": 2,
        "name": "David",
        "department": "HR"
    }
]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Employee Service",
        "service": SERVICE_NAME,
        "environment": ENVIRONMENT
    })

@app.route("/employees")
def get_employees():
    return jsonify(employees)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

