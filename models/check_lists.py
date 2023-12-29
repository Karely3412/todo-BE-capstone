import uuid
import marshmallow as ma
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from db import db

from models.users_check_lists_xref import users_check_list_xref

class CheckLists(db.Model):
    __tablename__ = "CheckLists"

    check_list_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    check_list_name = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    date_ended = db.Column(db.DateTime(), default=None)

    users = db.relationship("Users", back_populates='check_lists', secondary=users_check_list_xref)

    def __init__(self, check_list_name, date_created, date_ended):
        self.check_list_name = check_list_name
        self.date_created = date_created
        self.date_ended = date_ended
        
    def get_new_check_list():
        return CheckLists("", datetime.now(),  None)
    

class CheckListsSchema(ma.Schema):
    class Meta:
        fields = ["check_list_id", "check_list_name", "date_created", "date_ended", "users"]
    users = ma.fields.Nested("UsersSchema", many=True)

    
check_list_schema = CheckListsSchema()
check_lists_schema = CheckListsSchema(many=True)