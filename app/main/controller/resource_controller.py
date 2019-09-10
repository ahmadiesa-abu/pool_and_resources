from flask import request
from flask_restplus import Resource


from ..util.dto import PoolResourceDto
from ..service.resource_service import allocate_resource, release_resource, add_resource, delete_resource_by_id, get_resource_by_id, get_first_released_resource_and_allocate_it

api = PoolResourceDto.api
_ResouceId = PoolResourceDto._ResouceId
_ResouceIp = PoolResourceDto._ResouceIp

@api.route('/api/pools/<string:id>/allocate')
class ResourceAllocate(Resource):
    @api.expect(_ResouceId)
    def put(self, id):
        data = request
        return allocate_resource(id, data)
		
@api.route('/api/pools/<string:id>/release')

class ReleaseAllocate(Resource):
    @api.expect(_ResouceId)
    def put(self, id):
        data = request
        return release_resource(id, data)

@api.route('/api/pools/<string:id>/resource/add')
class ResourceAdd(Resource):
    @api.expect(_ResouceIp)
    def post(self, id):
        data = request
        return add_resource(id, data)

@api.route('/api/pools/<string:id>/resource/remove/<string:resource_id>')
class ResourceRemove(Resource):

    def delete(self, id, resource_id):
        return delete_resource_by_id(id, resource_id)

@api.route('/api/pools/<string:id>/resource/<string:resource_id>')
class ResourceList(Resource):

    def get(self, id, resource_id):
        return get_resource_by_id(id, resource_id)

@api.route('/api/pools/<string:id>/allocate_first_released')
class FirstReleasedResourceAllocate(Resource):
   def put(self, id):
       return get_first_released_resource_and_allocate_it(id)
