import unittest

from app.main import db
import json
from app.test.base import BaseTestCase

def allocate_resource(self):
    return self.client.put(
        '/api/pools/fg34sc-re34-12tg-dv34hn12za56/allocate',
        data=json.dumps(dict(
            id='saukR69C-Yr0b-qai5-UL8rTgJMWofR'
        )),
        content_type='application/json'
    )

def release_resource(self):
    return self.client.put(
        '/api/pools/fg34sc-re34-12tg-dv34hn12za56/release',
        data=json.dumps(dict(
            id='ds8X8PZY-qf4B-UfTg-CcuTx0YkVa2U'
        )),
        content_type='application/json'
    )

def add_resource(self):
    return self.client.post(
        '/api/pools/fg34sc-re34-12tg-dv34hn12za56/resource/add',
        data=json.dumps(dict(
            ip_address='7.7.7.7'
        )),
        content_type='application/json'
    )

def delete_resource_by_id(self):
    return self.client.delete(
        '/api/pools/fg34sc-re34-12tg-dv34hn12za56/resource/' +
        'remove/i81YoErB-qNUn-OWUi-qIzGavZ9zORt')

def get_resource_by_id(self):
    return self.client.get(
        '/api/pools/fg34sc-re34-12tg-dv34hn12za56/resource/' +
        'saukR69C-Yr0b-qai5-UL8rTgJMWofR')

class TestResourceService(BaseTestCase):
    def test_allocate_resource(self):
        with self.client:
            response = allocate_resource(self)
            self.assertEqual(response.status_code, 200)

    def test_release_resource(self):
        with self.client:
            response = release_resource(self)
            self.assertEqual(response.status_code, 200)
			
    def test_add_resource(self):
        with self.client:
            response = add_resource(self)
            self.assertEqual(response.status_code, 200)
			
    def test_delete_resource_by_id(self):
        with self.client:
            response = allocate_resource(self)
            self.assertEqual(response.status_code, 204)
			
    def test_get_resource_by_id(self):
        with self.client:
            response = get_resource_by_id(self)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
