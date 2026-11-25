from flask import Flask
app = Flask(__name__)

departments = [
    {"id": 1, "name": "IT"},
    {"id": 2, "name": "HR"},
    {"id": 3, "name": "Finance"}
]

@app.route('/')
@app.route('/departments')
def home():
    html = "<h1><b>Hello, Welcome to Department Service</b></h1>"
    html += "<h2>Department List:</h2><ul>"
    for d in departments:
        html += f"<li><b>{d['name']}</b> - ID: {d['id']}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
