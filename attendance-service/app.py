from flask import Flask

app = Flask(__name__)

ATTENDANCE = [
    {"employee_id": 1, "date": "2026-11-25", "status": "Present"},
    {"employee_id": 2, "date": "2026-11-25", "status": "Absent"}
]

@app.route("/")
def home():
    return "<h1>Welcome to Attendance Service</h1>"

@app.route("/attendance")
def get_attendance():
    return ATTENDANCE

@app.route("/health")
def health():
    return {"service": "Attendance Service", "status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
