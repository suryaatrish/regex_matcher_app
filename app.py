from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.json['test_string']
    regex = request.json['regex']
    matches = re.findall(regex, test_string)
    return jsonify({'matches': matches})

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.json['email']
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return 'Valid Email'
    else:
        return 'Invalid Email'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
