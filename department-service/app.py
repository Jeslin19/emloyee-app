from flask import Flask, jsonify

app = Flask(__name__)

departments = [
    {"id": 1, "name": "IT"},
    {"id": 2, "name": "HR"},
    {"id": 3, "name": "Finance"}
]

@app.route("/")
def home():
    return """
    <html><head><title>Department Service</title>
    <style>body{font-family:Arial;text-align:center;margin-top:80px;background:#f0f2f5}
    h1{color:#2c3e50} a{display:inline-block;margin:10px;padding:12px 25px;background:#007bff;color:white;text-decoration:none;border-radius:8px}</style>
    </head><body>
    <h1>👋 Welcome to Department Service</h1>
    <p>Employee Management System - Running on Azure AKS</p>
    <a href="/departments">View Departments</a>
    <a href="/employees">View Employees</a>
    <a href="/attendance">View Attendance</a>
    </body></html>
    """

@app.route("/departments")
def get_departments():
    rows = "".join([f"<tr><td>{d['id']}</td><td>{d['name']}</td></tr>" for d in departments])
    return f"""
    <html><head><title>Departments</title>
    <style>body{{font-family:Arial;text-align:center;margin-top:50px}} table{{margin:auto;border-collapse:collapse}} td,th{{border:1px solid #ccc;padding:10px 30px}} th{{background:#007bff;color:white}}</style>
    </head><body>
    <h1>🏢 Departments</h1>
    <table><tr><th>ID</th><th>Name</th></tr>{rows}</table>
    <br><a href="/">⬅ Back to Home</a>
    </body></html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
