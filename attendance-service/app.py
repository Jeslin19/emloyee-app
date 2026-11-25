from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/attendance')
def home():
    html = "<h1><b>Hello, Welcome to Attendance Service</b></h1>"
    html += "<h2>Attendance List:</h2><ul><li><b>John</b> - Present</li><li><b>Priya</b> - Present</li></ul>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
