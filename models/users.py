from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma
import uuid


from db import db

from models.users_check_lists_xref import users_check_list_xref

class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)

    auth = db.relationship("AuthTokens", back_populates='user')
    check_lists = db.relationship("CheckLists", back_populates='users', secondary=users_check_list_xref)

    def __init__(self, first_name, last_name, email, password, phone, address, active ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address
        self.active = active

    def get_new_user():
        return Users("", "", "", "", "", "", True)
    

class UsersSchema(ma.Schema):
    class Meta:
        fields = ["user_id", "first_name", "last_name", "email", "phone", "address", "active"]

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)