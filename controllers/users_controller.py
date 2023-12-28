from flask import jsonify, request
from db import db

from models.users import Users, user_schema, users_schema


def user_add(req):
    post_data = req.form if req.form else req.json 


    post_data.get("first_name")
    post_data.get("last_name")
    post_data.get("email")
    post_data.get("password")
    post_data.get("phone")
    post_data.get("address")

    user_query = db.session.query(Users).filter(Users.user_id == Users.user_id).first()



    db.session.add()
    db.session.commit()
    


    # return jsonify({"message": "user added successfully", "user information": user_schema.dump() })

    return user_query