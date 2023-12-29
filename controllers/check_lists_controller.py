from flask import jsonify, request
from db import db

from models.check_lists import CheckLists, check_lists_schema, check_list_schema
from models.users import  Users, user_schema, users_schema
from util.reflecton import populate_object
from lib.authenticate import authenticate


def check_list_add(req):
    post_data = req.form if req.form else req.json

    new_check_list = CheckLists.get_new_check_list()
    populate_object(new_check_list, post_data)

    db.session.add(new_check_list)
    db.session.commit()

    return jsonify({"message": "checklist successfully created", "check_list": check_list_schema.dump(new_check_list)})


def check_lists_get_all(req):
    check_lists_query = db.session.query(CheckLists).all()

    return jsonify({"message": "checklists found", "check_lists": check_lists_schema.dump(check_lists_query) })


def check_list_get_by_id(req, check_list_id):
    check_list_query = db.session.query(CheckLists).filter(CheckLists.check_list_id == check_list_id).first()

    return jsonify({"message": "checklist found", "check_list": check_list_schema.dump(check_list_query) })

@authenticate
def check_lists_get_by_user_id(req, user_id):
    check_list_query = db.session.query(CheckLists).join(Users).first()

    return jsonify({"message": "checklist(s) found", "check_lists": check_lists_schema.dump(check_list_query) })


def check_list_delete(req, check_list_id):
    check_list_query = db.session.query(CheckLists).filter(CheckLists.check_list_id == check_list_id).first()

    db.session.delete(check_list_query)
    db.session.commit()
    

    return jsonify({"message": "checklist deleted"})
    
    

