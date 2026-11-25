import os
from flask import Flask

app = Flask(__name__)

DEPARTMENTS = [
    {"id": 1, "name": "IT"},
    {"id": 2, "name": "HR"},
]

@app.route("/")
def home():
    """Welcome page for Department Service."""
    return "<h1 style='text-align:center;margin-top:100px;font-family:Arial'>👋 Welcome to Department Page</h1>"

@app.route("/departments")
def get_departments():
    """Return departments list."""
    items = "".join(f"<li>{d['name']}</li>" for d in DEPARTMENTS)
    return f"<h1 style='text-align:center;font-family:Arial'>Welcome to Department Page</h1><ul style='text-align:center;list-style:none'>{items}</ul>"

@app.route("/health")
def health():
    """Health check."""
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5001")))
