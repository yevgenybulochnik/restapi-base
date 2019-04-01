from flask_restful import Resource


class HelloWorldResource(Resource):
    def get(self):
        return {'Hello': 'World'}
