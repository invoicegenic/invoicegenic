'''
'''
from sqlalchemy.ext.declarative import declared_attr

from . import utcnow
from extensions import db


class SoftDeleteMixin(object):
    @declared_attr
    def deleted_at(self):
        return db.Column(db.DateTime, nullable=True)

    def soft_delete(self):
        deleted_datetime = utcnow().strftime('%Y-%m-%d %H:%M:%S')
        return setattr(self, 'deleted_at', deleted_datetime)
