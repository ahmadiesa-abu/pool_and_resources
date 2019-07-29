from flask_restplus import Namespace,fields


class PoolResourceDto:
    api = Namespace('', description='pool/resource related operations')
    _Pool = api.model('Pool', {
        'name': fields.String(required=True, description='pool name'),
        'resources': fields.List(fields.String)
    })

    _ResouceId = api.model('ResourceId', {
        'id': fields.String(required=True, description='resource identifier')
    })

    _ResouceIp = api.model('ResourceIP', {
		'ip_address': fields.String(required=True, description='resource ip address')
    })