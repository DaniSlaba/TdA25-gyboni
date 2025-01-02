import os

from flask import Flask, jsonify
from flask_restful import Resource, Api 

from . import db


app = Flask(__name__)
api = Api(app, prefix='/api/v1')


app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite'),
)


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return "Hello TdA!"

@app.route('/api')
def route_api():
    data = {'organization': 'Student Cyber Games'}
    return jsonify(data)


class Games(Resource):

    def get(self):
        return jsonify({'hry': 'všecky'})


api.add_resource(Games, '/games')


if __name__ == '__main__':
    app.run()
