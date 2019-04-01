from flask import Blueprint
from flask_restful import Api


bp = Blueprint('apiv1', __name__)

api = Api(bp)

from app.apiv1 import routes
