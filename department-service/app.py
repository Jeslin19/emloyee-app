from flask import Flask

app = Flask(__name__)

DEPARTMENTS = [
    {"id": 1, "name": "IT"},
    {"id": 2, "name": "HR"},
    {"id": 3, "name": "Finance"}
]

@app.route("/")
def home():
    return "<h1>Welcome to Department Service</h1>"

@app.route("/departments")
def get_departments():
    return DEPARTMENTS

@app.route("/health")
def health():
    return {"service": "Department Service", "status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
