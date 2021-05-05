'''App models'''
from uuid import uuid4
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash

from models import db
from .mixins.use_uuid_pk import UseUuidAsPK
from .mixins.created_time import CreatedTimeMixin
from .mixins.updated_time import UpdatedTimeMixin
from .mixins.soft_delete import SoftDeleteMixin


class Mixins(CreatedTimeMixin, UpdatedTimeMixin, SoftDeleteMixin):
    pass


class User(UseUuidAsPK, Mixins, db.Model):
    '''User model class'''
    email = db.Column(db.String(120), nullable=False, index=True, unique=True)

    password = db.Column(db.String(128), nullable=False)

    editable = ['email', 'password']

    def __repr__(self):
        return f'<User {self.email}>'

    def __make_pw_hash(self, password):
        method = 'pbkdf2:sha256:120282'
        salt_length = 32
        return generate_password_hash(password, method, salt_length)

    def __check_pw_hash(self, password):
        pass

    def to_utc_iso(self, utc_datetime: datetime) -> str:
        return utc_datetime.isoformat() + 'Z'

    def to_dict(self):
        payload = {
            'id': self.id,
            'email': self.email,
            'created_at': self.to_utc_iso(self.created_at),
            'updated_at': self.to_utc_iso(self.updated_at)
        }
        return payload

    def from_dict(self, data, new_user=False):
        if new_user:
            super().make_uuid()

        for _, field in enumerate(self.editable):
            if field not in data:
                continue

            if field == 'password':
                pw_hash = self.__make_pw_hash(data['password'])
                setattr(self, 'password', pw_hash)
            else:
                setattr(self, field, data[field])
