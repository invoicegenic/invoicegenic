'''App models'''
from models import db
from uuid import uuid4
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash


class User(db.Model):
    '''User model class'''
    id = db.Column(db.String(40), primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.now(tz=timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(tz=timezone.utc))
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def __make_id(self):
        self.id = str(uuid4())

    def __make_pw_hash(self, password):
        method = 'pbkdf2:sha256:120282'
        salt_length = 32
        self.password_hash = \
            generate_password_hash(password, method, salt_length)

    def __check_pw_hash(self, password):
        pass

    def to_dict(self):
        payload = {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at.isoformat() + 'Z',
            'updated_at': self.updated_at.isoformat() + 'Z',
        }
        return payload

    def from_dict(self, data, new_user=False):
        fields = ['email']
        for field, value in fields:
            if field in data:
                setattr(self, field, value)

        if new_user and 'password' in data:
            self.__make_id()
            self.__make_pw_hash(password=data['password'])
