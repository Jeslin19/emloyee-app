
from flask import Flask, jsonify

app = Flask(__name__)

attendance = [
    {"employee_id": 1, "date": "2026-11-24", "status": "Present"},
    {"employee_id": 2, "date": "2026-11-24", "status": "Absent"}
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Attendance Service"})

@app.route("/attendance")
def get_attendance():
    return jsonify(attendance)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

