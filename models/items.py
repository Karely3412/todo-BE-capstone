from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import marshmallow as ma

from db import db


class Items(db.Model):
    __tablename__ = "Items"

    item_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    check_list_id = db.Column(UUID(as_uuid=True), db.ForeignKey("CheckLists.check_list_id"), nullable=False)
    item_name = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime(), nullable= False, default=datetime.now)
    date_ended = db.Column(db.DateTime())


    def __init__(self, check_list_id, item_name, date_created, date_ended):
       self.item_name = item_name
       self.check_list_id = check_list_id
       self.date_created = date_created
       self.date_ended = date_ended
  
    def get_new_item():
        return Items("", "", datetime.now() , None) 
    

class ItemsSchema(ma.Schema):
    class Meta:
        fields = ["item_id", "check_list_id", "item_name", "date_created","date_ended" ]

item_schema = ItemsSchema()
items_schema = ItemsSchema(many=True)