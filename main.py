import flask
import json
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import http.client
from flask import Flask
from flask_restplus import Api, Resource


from flask import request, jsonify

app = Flask(__name__)
api = Api(app)

StoragePath = "localhost:8080"


@api.route('/hel11lo/',methods=['GET'])
class HelloWorld(Resource):
    def get(self):
        return "Hello World"


@api.route('/', methods=['GET'])
class HelloWorld1(Resource):
    def get(self):
        return "You have 2 functions: getX and getAge"

# A route to return all of the available entries in our catalog.
@api.route('/api/v1/getX/', methods=['GET'])
class HelloWorld2(Resource):
    def get(self):
       #connection = http.client.HTTPSConnection(StoragePath)
        connection = http.client.HTTPConnection(StoragePath)
        connection.request("GET", "/api/v1/getX")
        response = connection.getresponse().readlines().__str__()
        return jsonify(response)


@api.route('/api/v1/getAge', methods=['GET'])
class HelloWorld3(Resource):
    def get(self):
        # connection = http.client.HTTPSConnection(StoragePath)
        connection = http.client.HTTPConnection(StoragePath)
        connection.request("GET", "/api/v1/getAge")
        response = connection.getresponse().readlines().__str__()
        return jsonify(response)

app.run(host="localhost", port=8081, debug=True)