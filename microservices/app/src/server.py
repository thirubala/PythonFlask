from src import app
# from flask import jsonify


@app.route("/")
def home():
    return "Hasura Hello World"

# Uncomment to add a new URL at /new
#task-one-one
@app.route('/Thiru-taskone')
def hello_world():
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
	posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
	return render_template('Task2.html',users=users,posts=posts)
			
	return "Done"return 'Hello World - Thiru'

	
	