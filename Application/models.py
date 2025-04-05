from .database import db #.database will search the file within this folder

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(),nullable=False,unique=True)
    email=db.Column(db.String(),nullable=False,unique=True)
    password=db.Column(db.String(),nullable=False)
    type=db.Column(db.String(),default='general')
    details=db.relationship('Info',backref='creator')

class Info(db.Model):
    id=db.Column(db.Integer(),primary_key=True)  
    attribute_name=db.Column(db.String(),nullable=False)
    attribute_value=db.Column(db.String(),nullable=False)
    card_name=db.Column(db.String(),nullable=False)
    user_id=db.Column(db.Integer(),db.ForeignKey('user.id'),nullable=False)