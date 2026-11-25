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
    return EMPLOYEES

@app.route("/health")
def health():
    return {"service": "Employee Service", "status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
