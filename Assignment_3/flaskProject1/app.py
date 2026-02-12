from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
