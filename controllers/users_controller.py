from flask import jsonify, request
from db import db

from util.reflecton import populate_object
from util.validate_uuid4 import validate_uuid4
from models.users import Users, user_schema, users_schema


def user_add(req):
    post_data = req.form if req.form else req.json 
    fields = ['first_name', 'last_name', 'email', 'password', 'phone']
    
    for field in fields:
        if field not in post_data:
            return jsonify({"message": "field(s) required"}), 400
    
    for field in fields:
        if post_data[field] == '':
            return jsonify({"message": "field(s) required"}), 400
        
    new_user = Users.get_new_user()

    populate_object(new_user, post_data)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "user added successfully", "user": user_schema.dump(new_user) }), 201


def users_get_all(req):
    users_query = db.session.query(Users).all()

    return jsonify({"message": "users found", "users": users_schema.dump(users_query)}), 200


def user_get_by_id(req, user_id):
    if validate_uuid4(user_id) == False:
        return jsonify({"message": "invalid user id"}), 400

    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()

    if not user_query:
        return jsonify({"message": "user not found"}), 404    

    return jsonify({"message": "user found", "user": user_schema.dump(user_query)}), 200


def user_update(req, user_id):
    post_data = req.form if req.form else req.json
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()

    populate_object(user_query, post_data)

    db.session.commit()
    return jsonify({"message": "user updated", "user": user_schema.dump(user_query)}), 200


def user_activity(req, user_id):
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()

    user_query.active = not user_query.active
    db.session.commit()

    if user_query.active:
        return jsonify({"message": "user activated", "user": user_schema.dump(user_query)}), 200
    else:    
        return jsonify({"message": "user deactivated", "user": user_schema.dump(user_query)}), 200
    

def user_delete(req, user_id):
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()

    if not user_query:
        return jsonify({"message": "user not found"}), 404
    
    
    db.session.delete(user_query)
    db.session.commit()
    return jsonify({"message ": "user successfully deleted"}), 200
    