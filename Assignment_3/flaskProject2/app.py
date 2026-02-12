from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["studentDB"]
collection = db["students"]

@app.route('/api')
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return {"data": data}

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for('success'))

    except Exception as e:
        return render_template("form.html", error=str(e))

@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)
