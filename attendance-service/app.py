from flask import Flask
app = Flask(__name__)

employees = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Priya"},
    {"id": 3, "name": "Rahul"}
]

@app.route('/')
@app.route('/employees')
def home():
    html = "<h1><b>Hello, Welcome to Employee Service</b></h1>"
    html += "<h2>Employee List:</h2><ul>"
    for e in employees:
        html += f"<li><b>{e['name']}</b> - ID: {e['id']}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
