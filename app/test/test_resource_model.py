import unittest

import datetime

import uuid

from app.main import db
from app.main.model.Pool import Pool
from app.main.model.Resource import Resource
from app.test.base import BaseTestCase


class TestResourceModel(BaseTestCase):

    def test_add_pool(self):
        pool_id = uuid.uuid4()
        pool = Pool(
            id=pool_id,
            name='test_pool_model'
        )
        db.session.add(pool)
        db.session.commit()
        resource = Resource(
            pool_id=pool_id,
			id=uuid.uuid4(),
			ip_address='5.6.7.8',
            status='RELEASED'
        )
        db.session.add(resource)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()

