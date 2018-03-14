from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world!'}

class AndroidDeviceManager(Resource):
    def get(self):
        return 'test'

class AndroidDevice(Resource):
    def get(self):
        return {'hhhh': 'hhhh'}

api.add_resource(HelloWorld, '/')
api.add_resource(AndroidDeviceManager, '/android_device')

if __name__ == '__main__':
    app.run(host='192.168.3.19', debug=True)
