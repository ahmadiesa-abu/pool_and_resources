import uuid
import datetime
import traceback

from app.main import db
from app.main.model.Pool import Pool
from app.main.model.Resource import Resource

from flask import Flask, request, jsonify, make_response



def save_changes(data):
    db.session.add(data)
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()

def allocate_resource(id,request):
    try:
        pool = Pool.query.get(id)
        if not pool:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            if request.data:
                if not request.is_json:
                    result = {'error': 'API input must be of json content type'}
                    return make_response(jsonify(result),500)
                if not request.json:
					result = {'error': 'check your request inputs'}
					return make_response(jsonify(result),500)
            resource_id = request.json['id']
            resources = pool.resources
            if not resources:
                result = {'error': 'Resource is not found'}
                return make_response(jsonify(result), 404)
            for resource in resources:
                if resource.id == resource_id:
                    if resource.status == 'ALLOCATED':
                        result = {'error': 'Resource is already allocated'}
                        return make_response(jsonify(result), 409)
                    resource.status = 'ALLOCATED'
                    db.session.commit()
                    p_resource = {}
                    p_resource['id'] = resource.id
                    p_resource['ip_address'] = resource.ip_address
                    p_resource['status'] = resource.status
                    return make_response(jsonify(p_resource), 200)
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
    except Exception as e:
        result = {'error': 'Exception occured : '+getattr(e, 'message', repr(e))}
        return make_response(jsonify(result),500)

def release_resource(id,request):
    try:
        pool = Pool.query.get(id)
        if not pool:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            if request.data:
                if not request.is_json:
                    result = {'error': 'API input must be of json content type'}
                    return make_response(jsonify(result),500)
                if not request.json:
					result = {'error': 'check your request inputs'}
					return make_response(jsonify(result),500)
            resource_id = request.json['id']
            resources = pool.resources
            if not resources:
                result = {'error': 'Resource is not found'}
                return make_response(jsonify(result), 404)
            for resource in resources:
                if resource.id == resource_id:
                    resource.status = 'RELEASED'
                    db.session.commit()
                    p_resource = {}
                    p_resource['id'] = resource.id
                    p_resource['ip_address'] = resource.ip_address
                    p_resource['status'] = resource.status
                    return make_response(jsonify(p_resource), 200)
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
    except Exception as e:
        result = {'error': 'Exception occured : '+getattr(e, 'message', repr(e))}
        return make_response(jsonify(result),500)


def get_first_released_resource_and_allocate_it(id):
    try:
        pool = Pool.query.get(id)
        if not pool:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            resource_id = ''
            resources = pool.resources
            if not resources:
                result = {'error': 'Release resource was not found'}
                return make_response(jsonify(result), 404)
            for resource in resources:
                if resource.status == 'RELEASED':
                    resource_id = resource.id
                    resource.status = 'ALLOCATED'
                    db.session.commit()
                    p_resource = {}
                    p_resource['id'] = resource.id
                    p_resource['ip_address'] = resource.ip_address
                    p_resource['status'] = resource.status
                    return make_response(jsonify(p_resource), 200)
            if resource_id == '':
                result = {'error': 'Released resource was not found'}
                return make_response(jsonify(result), 404)
    except Exception as e:
        result = {'error': 'Exception occured : '+getattr(e, 'message', repr(e))}
        return make_response(jsonify(result),500)

def add_resource(id,request):
    try:
        pool = Pool.query.get(id)
        if not pool:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            if request.data:
                if not request.is_json:
                    result = {'error': 'API input must be of json content type'}
                    return make_response(jsonify(result),500)
                if not request.json:
					result = {'error': 'check your request inputs'}
					return make_response(jsonify(result),500)
            ip_address = request.json['ip_address']
            p_resource = {}
            p_resource['id'] = uuid.uuid4()
            p_resource['ip_address'] = request.json['ip_address']
            p_resource['status'] = 'RELEASED'
            res = Resource(
                pool_id=id,
                id=p_resource['id'],
                ip_address=p_resource['ip_address'],
                status=p_resource['status']
            )
            save_changes(res)
            
            return make_response(jsonify(p_resource), 200)
    except Exception as e:
        result = {'error': 'Exception occured : '+getattr(e, 'message', repr(e))}
        return make_response(jsonify(result),500)

def delete_resource_by_id(id, resource_id):
    try:
        pool = Pool.query.get(id)
        if not pool:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            resources = pool.resources
            if not resources:
                result = {'error': 'Resource is not found'}
                return make_response(jsonify(result), 404)
            for resource in resources:
                if resource.id == resource_id:
                    delete_changes(resource)
                    return make_response({}, 204)
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
    except Exception as e:
        result = {'error': 'Exception occured : '+getattr(e, 'message', repr(e))}
        return make_response(jsonify(result),500)
		
def get_resource_by_id(id, resource_id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        if not Pool:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        resources = pool.resources
        if not resources:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        p = {}
        p['name'] = pool.name
        p_resources = []
        for resource in resources:
            if resource.id == resource_id:
                p_resource = {}
                p_resource['id'] = resource.id
                p_resource['ip_address'] = resource.ip_address
                p_resource['status'] = resource.status
                p_resource['pool_name'] = pool.name
                return make_response(jsonify(p_resource), 200)
        result = {'error': 'Resource is not found'}
        return make_response(jsonify(result), 404)
    except Exception as e:
        result = {'error': 'Exception occured : '+getattr(e, 'message', repr(e))}
        return make_response(jsonify(result),500)

