from flask import jsonify, request
from db import db

from models.check_lists import CheckLists, check_lists_schema, check_list_schema
from util.reflecton import populate_object


def check_list_add(req):
    post_data = req.form if req.form else req.json

    new_check_list = CheckLists.get_new_check_list()
    populate_object(new_check_list, post_data)

    db.session.add(new_check_list)
    db.session.commit()

    return jsonify({"message": "check list successfully created", "check_list": check_list_schema.dump(new_check_list)})


def check_lists_get_all(req):
    check_lists_query =db.session.query(CheckLists).all()

    return jsonify({"message": "check lists found", "check_lists": check_lists_schema.dump(check_lists_query) })


