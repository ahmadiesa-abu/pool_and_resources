from flask import request
from flask_restplus import Resource

from ..util.dto import PoolResourceDto
from ..service.pool_service import add_pool, get_pools, get_pool_by_id, delete_pool_by_id

api = PoolResourceDto.api
_Pool = PoolResourceDto._Pool

@api.route('/api/pools')
class PoolList(Resource):

    def get(self):
        return get_pools()

@api.route('/api/pools/<string:id>')
class Pool(Resource):
    
    @api.expect(_Pool)
    def put(self, id):
        data = request	
        return add_pool(id, data)

    def get(self, id):
        return get_pool_by_id(id)

    def delete(self, id):
        return delete_pool_by_id(id)