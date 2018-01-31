from src import app
from flask import jsonify
from flask import json
from flask import Flask,request,render_template,make_response

hasuradbUrl = "https://data.joviality89.hasura-app.io/v1/query";

#task-two
@app.route("/")
def home():
    return 'App Started'

#task-two
@app.route("/GetMetric",methods=['POST'])
def getMetric():
	metric = request.form['metric']
	print(metric)
	requestOptions = {
    "method": "POST",
    "headers": {
        "Content-Type": "application/json"
		}
	}

	metricDB =  = {
		"type": "select",
		"args": {
			"table": "world_happ_rpt",
			"columns": [
				"*"
			],
			"order_by": [
				{
					"column": "H_Rank",
					"order": "asc"
				}
			]
		}
	}

    resp = requests.request("POST", hasuradbUrl, data=json.dumps(metricDB))
    respObj = resp.json()
	actualMetric[] = 0
	
	for i in len(respObj):
	
		actualMetric[i] = respObj[i][metric] #store the json data in an array
	
	return actualMetric #returns array

app.run(debug = True,port=8080)