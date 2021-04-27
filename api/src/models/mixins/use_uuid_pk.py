'''
'''
from uuid import uuid4

from extensions import db


class UseUuidAsPK(object):
    id = db.Column(db.String(40), primary_key=True)

    def make_uuid(self) -> uuid4:
        self.id = str(uuid4())
