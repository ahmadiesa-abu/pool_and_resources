import os
import random
import string
from flask import Flask, request, jsonify, make_response
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Resource
from models import Pool

def randomStringDigits(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits)
                   for i in range(stringLength))


def generate_random_resource_id():
    return randomStringDigits(8)+'-'+randomStringDigits(4)+'-'\
        + randomStringDigits(4)+'-'+randomStringDigits(12)


@app.route('/api/pools/<string:id>', methods=['PUT'])
def add_pool(id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        if pool is not None:
            result = {'error': 'Resource with same id already exists'}
            return make_response(jsonify(result), 409)
        else:
            name = request.json['name']
            resources = request.json['resources']
            pool = Pool(
                id=id,
                name=name
            )
            db.session.add(pool)
            db.session.commit()

            for resource in resources:
                res = Resource(
                    pool_id=id,
                    id=generate_random_resource_id(),
                    ip_address=resource,
                    status='RELEASED'
                )
                db.session.add(res)
                db.session.commit()

            return make_response(request.json, 201)
    except Exception as e:
        return make_response({},500)


@app.route("/api/pools", methods=['GET'])
def get_pools():
    try:
        all_pools = []
        pools = Pool.query.all()
        for pool in pools:
            resources = Resource.query.filter_by(pool_id=pool.id)
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
        return make_response({},500)


@app.route("/api/pools/<string:id>", methods=['GET'])
def get_pool_by_id(id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        resources = Resource.query.filter_by(pool_id=id)
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
        return make_response({},500)


@app.route("/api/pools/<string:id>", methods=['DELETE'])
def delete_pool_by_id(id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        if pool is None:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            resources = Resource.query.filter_by(pool_id=id)
            if resources is not None:
                result = {
                    'error': 'Conflict When it is not allowed to remove pool'}
                return make_response(jsonify(result), 409)
            db.session.delete(pool)
            db.session.commit()
            return make_response({}, 204)
    except Exception as e:
        return make_response({},500)


@app.route('/api/pools/<string:id>/allocate', methods=['PUT'])
def allocate_resource(id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        if pool is None:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        resource_id = request.json['id']
        resource = Resource.query.filter_by(id=resource_id, pool_id=id).first()
        if resource is None:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            resource.status = 'ALLOCATED'
            db.session.commit()
            p_resource = {}
            p_resource['id'] = resource.id
            p_resource['ip_address'] = resource.ip_address
            p_resource['status'] = resource.status
            return make_response(jsonify(p_resource), 200)
    except Exception as e:
        return make_response({},500)


@app.route('/api/pools/<string:id>/release', methods=['PUT'])
def release_resource(id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        if pool is None:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        resource_id = request.json['id']
        resource = Resource.query.filter_by(id=resource_id, pool_id=id).first()
        if resource is None:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            resource.status = 'RELEASED'
            db.session.commit()
            p_resource = {}
            p_resource['id'] = resource.id
            p_resource['ip_address'] = resource.ip_address
            p_resource['status'] = resource.status
            return make_response(jsonify(p_resource), 200)
    except Exception as e:
        return make_response({},500)


@app.route('/api/pools/<string:id>/resource/add', methods=['POST'])
def add_resource(id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        if pool is None:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            p_resource = {}
            p_resource['id'] = generate_random_resource_id()
            p_resource['ip_address'] = request.json['ip_address']
            p_resource['status'] = 'RELEASED'
            res = Resource(
                pool_id=id,
                id=p_resource['id'],
                ip_address=p_resource['ip_address'],
                status=p_resource['status']
            )
            db.session.add(res)
            db.session.commit()
            return make_response(jsonify(p_resource), 200)
    except Exception as e:
        return make_response({},500)


@app.route("/api/pools/<string:id>/resource/remove/<string:resource_id>", methods=['DELETE'])
def delete_resource_by_id(id, resource_id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        if pool is None:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            resource = Resource.query.filter_by(
                pool_id=id, id=resource_id).first()
            if resource is None:
                result = {'error': 'Resource is not found'}
                return make_response(jsonify(result), 404)
            db.session.delete(resource)
            db.session.commit()
            return make_response({}, 204)
    except Exception as e:
        return make_response({},500)


@app.route("/api/pools/<string:id>/resource/<string:resource_id>", methods=['GET'])
def get_resource_by_id(id, resource_id):
    try:
        pool = Pool.query.filter_by(id=id).first()
        if pool is None:
            result = {'error': 'Resource is not found'}
            return make_response(jsonify(result), 404)
        else:
            resource = Resource.query.filter_by(
                pool_id=id, id=resource_id).first()
            if resource is None:
                result = {'error': 'Resource is not found'}
                return make_response(jsonify(result), 404)
            else:
                p_resource = {}
                p_resource['pool_name'] = pool.name
                p_resource['id'] = resource.id
                p_resource['ip_address'] = resource.ip_address
                p_resource['status'] = resource.status
                return make_response(jsonify(p_resource), 200)
    except Exception as e:
        return make_response({},500)


if __name__ == '__main__':
    app.run()
