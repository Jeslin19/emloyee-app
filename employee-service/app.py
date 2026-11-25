import os
from flask import Flask

app = Flask(__name__)

EMPLOYEES = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "David", "department": "HR"},
]

@app.route("/")
def home():
    """Welcome page for Employee Service."""
    return "<h1 style='text-align:center;margin-top:100px;font-family:Arial'>👋 Welcome to Employee Page</h1>"

@app.route("/employees")
def get_employees():
    """Return employees list."""
    items = "".join(f"<li>{e['name']} - {e['department']}</li>" for e in EMPLOYEES)
    return f"<h1 style='text-align:center;font-family:Arial'>Welcome to Employee Page</h1><ul style='text-align:center;list-style:none'>{items}</ul>"

@app.route("/health")
def health():
    """Health check."""
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5002")))
