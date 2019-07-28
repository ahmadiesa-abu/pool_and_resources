import os
import unittest

import traceback

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model.Pool import Pool
from app.main.model.Resource import Resource

app = create_app('dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    try:
        Pool.query.get('1')
    except Exception as e:
        ''' build the database if the table is not there '''
        if getattr(e, 'message', repr(e)).find('\"pool\" does not exist')!=-1:
            db.create_all()
            db.session.commit()
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
