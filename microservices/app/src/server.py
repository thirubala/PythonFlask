from src import app
from flask import jsonify
from flask import json
from flask import Flask,request,render_template,make_response

#task-two
@app.route("/")
def home():
    return 'Hello'

#task-two
@app.route("/GetMetric",methods=['POST'])
def getMetric():
	metric = request.form['metric']
	var requestOptions = {
    "method": "POST",
    "headers": {
        "Content-Type": "application/json"
    }
};

var body = {
    "type": "select",
    "args": {
        "table": "world_happ_rpt",
        "columns": [
            "*"
        ]
    }
};

requestOptions.body = JSON.stringify(body);

fetchAction(url, requestOptions)
.then(function(response) {
	return response.json();
})
.then(function(result) {
	console.log(result);
})
.catch(function(error) {
	console.log('Request Failed:' + error);
});

@app.route('/Thiru-taskone')
def hello_world():
	users = requests.get('https://jsonplaceholder.typicode.com/users').json()
	posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
	return render_template('Task2.html',users=users,posts=posts)
			
	return "Done"

app.run(debug = True,port=8080)