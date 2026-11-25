from flask import Flask

app = Flask(__name__)

DEPARTMENTS = [
    {"id": 1, "name": "IT"},
    {"id": 2, "name": "HR"},
    {"id": 3, "name": "Finance"}
]

@app.route("/")
def home():
    return """
    <h1 style="text-align:center">Welcome to Department Service</h1>
    <h2 style="text-align:center">Department Details</h2>
    """

@app.route("/departments")
def get_departments():
    items = "".join(
        f"<li>{d['name']}</li>" for d in DEPARTMENTS
    )
    return f"""
    <h1 style="text-align:center">Welcome to Department Service</h1>
    <h2>Department List</h2>
    <ul>{items}</ul>
    """

@app.route("/health")
def health():
    return {"service": "Department Service", "status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
