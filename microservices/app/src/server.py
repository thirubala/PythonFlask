from src import app
# from flask import jsonify


@app.route("/")
def home():
    return "Hasura Hello World"

# Uncomment to add a new URL at /new

@app.route('/Thiru-taskone')
def hello_world():
    return 'Hello World - Thiru'
