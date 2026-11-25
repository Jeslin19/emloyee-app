from flask import Flask, jsonify

app = Flask(__name__)

attendance = [
    {"id": 1, "employee": "John Doe", "status": "Present"},
    {"id": 2, "employee": "Jane Smith", "status": "Present"},
    {"id": 3, "employee": "Mike Johnson", "status": "Absent"}
]

@app.route("/")
def home():
    return """
    <html><head><title>Attendance Service</title>
    <style>body{font-family:Arial;text-align:center;margin-top:80px;background:#f0f2f5}
    h1{color:#2c3e50} a{display:inline-block;margin:10px;padding:12px 25px;background:#007bff;color:white;text-decoration:none;border-radius:8px}</style>
    </head><body>
    <h1>👋 Welcome to Attendance Page</h1>
    <p>Employee Management System - Running on Azure AKS</p>
    <a href="/attendance">View Attendance</a>
    <a href="/employees">View Employees</a>
    <a href="/departments">View Departments</a>
    </body></html>
    """

@app.route("/attendance")
def get_attendance():
    rows = "".join([f"<tr><td>{a['id']}</td><td>{a['employee']}</td><td>{a['status']}</td></tr>" for a in attendance])
    return f"""
    <html><head><title>Attendance</title>
    <style>body{{font-family:Arial;text-align:center;margin-top:50px}} table{{margin:auto;border-collapse:collapse}} td,th{{border:1px solid #ccc;padding:10px 30px}} th{{background:#ffc107;color:black}}</style>
    </head><body>
    <h1>📅 Attendance</h1>
    <table><tr><th>ID</th><th>Employee</th><th>Status</th></tr>{rows}</table>
    <br><a href="/">⬅ Back to Home</a>
    </body></html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
