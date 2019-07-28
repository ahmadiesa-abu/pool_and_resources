
from .. import db, flask_bcrypt
import datetime
from ..config import key


class Pool(db.Model):
    __tablename__ = 'pool'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String())
    resources = db.relationship('Resource', backref='Pool', lazy=True)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'name': self.name,
            'resources' : self.resources
        }