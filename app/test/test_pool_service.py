import unittest

from app.main import db
import json
from app.test.base import BaseTestCase


def create_pool(self):
    return self.client.put(
        '/api/pools/fg34sc-re34-12tg-dv34hn12za56',
        data=json.dumps(dict(
            name='testing_pool',
            resources=['1.1.1.1',
            '2.2.2.2','3.3.3.3']
        )),
        content_type='application/json'
    )

def get_pools(self):
    return self.client.get(
        '/api/pools')

def get_pool_by_id(self):
    return self.client.get(
        '/api/pools/fg34sc-re34-12tg-dv34hn12za56')

def delete_pool_by_id(self):
    return self.client.delete(
        '/api/pools/fg34sc-re34-12tg-dv34hn12za56')

class TestPoolService(BaseTestCase):
    def test_create_pool(self):
        with self.client:
            response = create_pool(self)
            self.assertEqual(response.status_code, 201)

    def test_get_pools(self):
        get_pools(self)
        with self.client:
            response = get_pools(self)
            self.assertEqual(response.status_code, 200)

    def test_get_pool_by_id(self):
        with self.client:
            response = get_pool_by_id(self)
            self.assertEqual(response.status_code, 200)

    def test_delete_pool_by_id(self):
        with self.client:
            response = delete_pool_by_id(self)
            self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
