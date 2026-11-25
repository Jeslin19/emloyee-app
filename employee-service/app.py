from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John Doe", "department": "IT"},
    {"id": 2, "name": "Jane Smith", "department": "HR"},
    {"id": 3, "name": "Mike Johnson", "department": "Finance"}
]

@app.route("/")
def home():
    return """
    <html><head><title>Employee Service</title>
    <style>body{font-family:Arial;text-align:center;margin-top:80px;background:#f0f2f5}
    h1{color:#2c3e50} a{display:inline-block;margin:10px;padding:12px 25px;background:#007bff;color:white;text-decoration:none;border-radius:8px}</style>
    </head><body>
    <h1>👋 Welcome to Employee Page</h1>
    <p>Employee Management System - Running on Azure AKS</p>
    <a href="/employees">View Employees</a>
    <a href="/departments">View Departments</a>
    <a href="/attendance">View Attendance</a>
    </body></html>
    """

@app.route("/employees")
def get_employees():
    rows = "".join([f"<tr><td>{e['id']}</td><td>{e['name']}</td><td>{e['department']}</td></tr>" for e in employees])
    return f"""
    <html><head><title>Employees</title>
    <style>body{{font-family:Arial;text-align:center;margin-top:50px}} table{{margin:auto;border-collapse:collapse}} td,th{{border:1px solid #ccc;padding:10px 30px}} th{{background:#28a745;color:white}}</style>
    </head><body>
    <h1>👨‍💼 Employees</h1>
    <table><tr><th>ID</th><th>Name</th><th>Department</th></tr>{rows}</table>
    <br><a href="/">⬅ Back to Home</a>
    </body></html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
