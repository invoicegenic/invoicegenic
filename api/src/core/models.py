'''App models'''
from datetime import datetime
from core import db


class User(db.Model):
    '''User model class'''
    id = db.Column(db.String(40), primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'


# class Invoice(db.Model):
#     '''Invoice model class'''
#     pass


# class Customer(db.Model):
#     '''Customer model class'''
#     pass


class Item(db.Model):
    '''Item model class'''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(40), db.ForeignKey('user.id'))
    code = db.Column(db.String(8), index=True, unique=True)
    short_description = db.Column(db.String(255), nullable=True)
    long_description = db.Column(db.Text, nullable=True)
    rate = db.Column(db.Float(precision=2), default=0)
    taxable = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Item {self.code}>'
