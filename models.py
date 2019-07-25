from app import db

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
		
class Resource(db.Model):
    __tablename__ = 'resource'
	
    pool_id = db.Column(db.String(),db.ForeignKey('Pool.id'),
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
