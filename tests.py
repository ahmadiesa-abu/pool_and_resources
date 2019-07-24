import unittest
import json

from app import app


class PoolTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_create_pool_status_code(self):
        result = self.app.put('/api/pools/fg34sc-re34-12tg-dv34hn12za56',
                              data=json.dumps(dict(name='testing_pool', resources=[
                                              '1.1.1.1', '2.2.2.2', '3.3.3.3'])),
                              content_type='application/json')

        self.assertEqual(result.status_code, 201)

    def test_get_pools_status_code(self):
        result = self.app.get('/api/pools')

        self.assertEqual(result.status_code, 200)

    def test_get_pool_by_id(self):
        result = self.app.get('/api/pools/fg34sc-re34-12tg-dv34hn12za56')

        self.assertEqual(result.status_code, 200)

    def test_delete_pool_by_id(self):
        result = self.app.delete('/api/pools/fg34sc-re34-12tg-dv34hn12za56')

        self.assertEqual(result.status_code, 204)

    def test_allocate_resource(self):
        result = self.app.put('/api/pools/fg34sc-re34-12tg-dv34hn12za56/allocate',
                              data=json.dumps(
                                  dict(id='saukR69C-Yr0b-qai5-UL8rTgJMWofR')),
                              content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_release_resource(self):
        result = self.app.put('/api/pools/fg34sc-re34-12tg-dv34hn12za56/release',
                              data=json.dumps(
                                  dict(id='ds8X8PZY-qf4B-UfTg-CcuTx0YkVa2U')),
                              content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_add_resource(self):
        result = self.app.post('/api/pools/fg34sc-re34-12tg-dv34hn12za56/resource/add',
                               data=json.dumps(dict(ip_address='7.7.7.7')),
                               content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_delete_resource_by_id(self):
        result = self.app.delete('/api/pools/fg34sc-re34-12tg-dv34hn12za56/resource/' +
                                 'remove/i81YoErB-qNUn-OWUi-qIzGavZ9zORt')

        self.assertEqual(result.status_code, 204)

    def test_get_resource_by_id(self):
        result = self.app.get('/api/pools/fg34sc-re34-12tg-dv34hn12za56/resource/' +
                              'saukR69C-Yr0b-qai5-UL8rTgJMWofR')

        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
