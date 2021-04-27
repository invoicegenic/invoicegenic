'''
'''
from sqlalchemy.ext.declarative import declared_attr

from . import utcnow
from extensions import db


class CreatedTimeMixin(object):
    @declared_attr
    def created_at(self):
        return db.Column(db.DateTime, nullable=False,
                         default=utcnow)
