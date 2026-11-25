from flask import Flask

app = Flask(__name__)

ATTENDANCE = [
    {"employee_id": 1, "date": "2026-11-24", "status": "Present"},
    {"employee_id": 2, "date": "2026-11-24", "status": "Absent"}
]

@app.route("/")
def home():
    return "<h1 style='text-align:center'>Welcome to Attendance Service</h1>"

@app.route("/attendance")
def get_attendance():
    items = "".join(
        f"<li>Employee ID: {a['employee_id']} | Date: {a['date']} | Status: {a['status']}</li>"
        for a in ATTENDANCE
    )

    return f"""
    <h1 style='text-align:center'>Welcome to Attendance Service</h1>
    <h2>Attendance Details</h2>
    <ul>{items}</ul>
    """

@app.route("/health")
def health():
    return {"service": "Attendance Service", "status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
