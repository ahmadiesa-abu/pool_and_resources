from flask_restplus import Api
from flask import Blueprint

from .main.controller.pool_controller import api as pool_ns
from .main.controller.resource_controller import api as resource_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Pool and Resources Test with Flask',
          version='1.0',
          description='a simple flask rest web service'
          )

api.add_namespace(pool_ns)
api.add_namespace(resource_ns)