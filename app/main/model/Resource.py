from .. import db
import datetime


class Resource(db.Model):
    __tablename__ = 'resource'
	
    pool_id = db.Column(db.String(),db.ForeignKey('pool.id'),
        nullable=False)
    id = db.Column(db.String, primary_key=True)
    ip_address = db.Column(db.String())
    status = db.Column(db.String())
	
    def __init__(self, pool_id, id, ip_address, status):
        self.pool_id = pool_id
        self.id = id
        self.ip_address = ip_address
        self.status = status
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
			'ip_address': self.ip_address,
			'status': self.status
        }
