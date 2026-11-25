from flask import Flask

app = Flask(__name__)

EMPLOYEES = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "David", "department": "HR"}
]

@app.route("/")
def home():
    return "<h1>Welcome to Employee Service</h1>"

@app.route("/employees")
def get_employees():
    items = "".join(
        f"<li>{e['name']} - {e['department']}</li>"
        for e in EMPLOYEES
    )

    return f"""
    <h1 style="text-align:center">Welcome to Employee Service</h1>
    <h2>Employee Details</h2>
    <ul>{items}</ul>
    """

@app.route("/health")
def health():
    return {"service": "Employee Service", "status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
