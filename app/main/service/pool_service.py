import uuid
import datetime

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

def add_pool(id,request):
    try:
        pool = Pool.query.get(id)
        if pool:
            result = {'error': 'Resource with same id already exists'}
            return make_response(jsonify(result), 409)
        else:
            if not request.json:
                result = {'error': 'check your request inputs'}
                return make_response(jsonify(result),500)
            name = request.json['name']
            resources = request.json['resources']
            pool = Pool(
                id=id,
                name=name
            )
            save_changes(pool)
            
            for resource in resources:
                res = Resource(
                    pool_id=id,
                    id=uuid.uuid4(),
                    ip_address=resource,
                    status='RELEASED'
                )
                save_changes(res)
				
            return make_response(request.json, 201)
    except Exception as e:
        result = {'error': 'something went wrong'}
        return make_response(jsonify(result),500)

def get_pools():
    try:
        all_pools = []
        pools = Pool.query.all()
        for pool in pools:
            resources = pool.resources
            p_resources = []
            for resource in resources:
                p_resource = {}
                p_resource['id'] = resource.id
                p_resource['ip_address'] = resource.ip_address
                p_resource['status'] = resource.status
                p_resources.append(p_resource)
            p = {'name': pool.name, 'resources': p_resources}
            all_pools.append(p)
        return make_response(jsonify({'items': all_pools}), 200)
    except Exception as e:
        result = {'error': 'something went wrong'}
        return make_response(jsonify(result),500)
		
def get_pool_by_id(id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        if not Pool:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        resources = pool.resources
        p = {}
        p['name'] = pool.name
        p_resources = []
        for resource in resources:
            p_resource = {}
            p_resource['id'] = resource.id
            p_resource['ip_address'] = resource.ip_address
            p_resource['status'] = resource.status
            p_resources.append(p_resource)
        p['resources'] = p_resources
        return make_response(jsonify(p), 200)
    except Exception as e:
        result = {'error': 'something went wrong'}
        return make_response(jsonify(result),500)

def delete_pool_by_id(id):
    try:
        pool = Pool.query.get(id)
        if not pool:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            resources = pool.resources
            if resources:
                result = {
                    'error': 'Conflict When it is not allowed to remove pool'}
                return make_response(jsonify(result), 409)
            delete_changes(pool)
			
            return make_response({}, 204)
    except Exception as e:
        print (e)
        result = {'error': 'something went wrong'}
        return make_response(jsonify(result),500)