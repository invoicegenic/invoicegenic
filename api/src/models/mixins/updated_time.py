'''
'''
from sqlalchemy.ext.declarative import declared_attr

from . import utcnow
from extensions import db


class UpdatedTimeMixin(object):
    @declared_attr
    def updated_at(self):
        return db.Column(db.DateTime, nullable=False,
                         default=utcnow, onupdate=utcnow)
