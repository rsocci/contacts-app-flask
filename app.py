
from flask import Flask, request, json, jsonify
from flask.ext.pymongo import PyMongo
from flask import render_template
from bson.json_util import dumps, loads
from bson.objectid import ObjectId

app = Flask('contact')
mongo = PyMongo(app) # PyMongo connects to MongoDB server on port 27017
					 # Assumes default db name of app.name (whatever passed to Flask)

@app.route('/')
def default():
	return render_template('index.html')

@app.route('/contacts', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		results = mongo.db.contact.find()
		return dumps(results)
	contact = loads(request.data)
	mongo.db.contact.insert(contact)
	return 'contact added'

@app.route('/contacts/<id>', methods=['GET', 'PUT', 'DELETE'])
def show(id):
	if request.method == 'GET':
		result = mongo.db.contact.find_one_or_404({'_id': ObjectId(id)})
		return dumps(result)
	elif request.method == 'PUT':
		to_update = loads(request.data)
		mongo.db.contact.update({'_id': ObjectId(id)}, {'$set': to_update})
		return 'updated contact'
	else:
		mongo.db.contact.remove({'_id': ObjectId(id)})	
		return 'deleted contact'

if __name__ == '__main__':
	app.run(debug=True)