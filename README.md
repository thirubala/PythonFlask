This is a simple app that will take a metric value and then return the corresponding value for all countries back to the user

Features:
Receive Metric
Get data from the database 
Return data for that particular metric back to user

All of the code is in one file that you can read at: microservices/bot/app/src/server.py

POST /GetMetric

Metric = metricvalue

This will return the value for that particular metric back to user

$hasura quickstart team29/hello-python-flask && cd hello-python-flask

http://app.joviality89.hasura-app.io/GetMetric

