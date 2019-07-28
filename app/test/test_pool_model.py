import unittest

import datetime

import uuid

from app.main import db
from app.main.model.Pool import Pool
from app.test.base import BaseTestCase


class TestPoolModel(BaseTestCase):

    def test_add_pool(self):
        pool = Pool(
            id=uuid.uuid4(),
            name='test_pool_model'
        )
        db.session.add(pool)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()

