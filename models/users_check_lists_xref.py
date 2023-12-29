from db import db 

users_check_list_xref = db.Table(
    "UsersCheckListsXref",
    db.Model.metadata,
    db.Column("user_id", db.ForeignKey('Users.user_id'), primary_key=True),
    db.Column("check_list_id", db.ForeignKey('CheckLists.check_list_id'), primary_key=True)
)

