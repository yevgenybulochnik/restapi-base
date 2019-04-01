from app.apiv1 import api
from app.apiv1.resources.helloworld import HelloWorldResource


api.add_resource(HelloWorldResource, '/hello')
