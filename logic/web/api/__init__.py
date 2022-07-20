from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Striver(Resource):
    def get( self, email):
        args_parser = reqparse.RequestParser()
        args_parser.add_argument('email', type=str)

        args = args_parser.parse_args()
        email = args['email']
        return {'email': email}
    
    
    def post(self, name, email):
        args_parser = reqparse.RequestParser()
        args_parser.add_argument('email', type=str)
        args_parser.add_argument('name', type=str)

        args = args_parser.parse_args()
        email = args['email']
        name = args['name']

        return {'email': email, 'name': name}


api.add_resource(Striver)
    