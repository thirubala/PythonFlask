from src import app
from flask import jsonify
from flask import json
from flask import Flask,request,render_template,make_response

#task-two
@app.route("/")
def home():
    return 'Hello'

app.run(debug = True,port=8080)