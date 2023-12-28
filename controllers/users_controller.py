from flask import jsonify, request
from db import db

from util.reflecton import populate_object
from models.users import Users, user_schema, users_schema


def user_add(req):
    post_data = req.form if req.form else req.json 

    new_user = Users.get_new_user()

    populate_object(new_user, post_data)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "user added successfully", "user": user_schema.dump(new_user) })


def users_get_all(req):
    users_query = db.session.query(Users).all()

    return jsonify({"message ": "users found", "users": users_schema.dump(users_query)})


def user_get_by_id(req, user_id):
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()

    return jsonify({"message ": "user found", "user": user_schema.dump(user_query)})


def user_update(req, user_id):
    post_data = req.form if req.form else req.json
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()

    populate_object(user_query, post_data)

    db.session.commit()
    return jsonify({"message ": "user updated", "user": user_schema.dump(user_query)})

    



def user_delete(req, user_id):
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()
    
    db.session.delete(user_query)
    db.session.commit()
    return jsonify({"message ": "user successfully deleted"})
    