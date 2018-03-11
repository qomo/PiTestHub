from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world!'}

class AndroidDevice(Resource):
    def get(self):
        pass

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='192.168.3.19', debug=True)
