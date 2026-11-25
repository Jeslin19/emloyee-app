import os
from flask import Flask

app = Flask(__name__)

ATTENDANCE = [
    {"id": 1, "employee": "John", "status": "Present"},
    {"id": 2, "employee": "David", "status": "Present"},
]

@app.route("/")
def home():
    """Welcome page for Attendance Service."""
    return "<h1 style='text-align:center;margin-top:100px;font-family:Arial'>👋 Welcome to Attendance Page</h1>"

@app.route("/attendance")
def get_attendance():
    """Return attendance list."""
    items = "".join(f"<li>{a['employee']} - {a['status']}</li>" for a in ATTENDANCE)
    return f"<h1 style='text-align:center;font-family:Arial'>Welcome to Attendance Page</h1><ul style='text-align:center;list-style:none'>{items}</ul>"

@app.route("/health")
def health():
    """Health check."""
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5003")))
