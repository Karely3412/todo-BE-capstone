import uuid
import marshmallow as ma
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from db import db

class CheckLists(db.Model):
    __tablename__ = "CheckLists"

    check_list_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    date_ended = db.Column(db.DateTime(), default=None)

    def __init__(self, name, last_name, email):
        self.name = name
        self.date_created = last_name
        self.date_ended = email
        
    def get_new_check_list():
        return CheckLists("", "", "")
    

class CheckListsSchema(ma.Schema):
    class Meta:
        fields = ["name", "date_created", "date_ended"]

check_list_schema = CheckListsSchema()
check_lists_schema = CheckListsSchema(many=True)