from flask import jsonify, request
from db import db

from util.reflecton import populate_object
from models.items import Items, item_schema, items_schema


def item_add(req):
    post_data = req.form if req.form else req.json

    new_item = Items.get_new_item()
    populate_object(new_item, post_data)

    db.session.add(new_item)
    db.session.commit()

    return jsonify({"message": "item successfully added", "item": item_schema.dump(new_item)}), 201


def items_get_all(req):
    items_query = db.session.query(Items).all()

    return jsonify({"message": "items successfully fetched", "items": items_schema.dump(items_query)}), 200


def item_get_by_id(req, item_id):
    item_query = db.session.query(Items).filter(Items.item_id == item_id).first()

    return jsonify({"message": "item successfully fetched", "item": item_schema.dump(item_query)}), 200


def item_get_by_check_list_id(req, check_list_id):
    item_query = db.session.query(Items).filter(Items.check_list_id == check_list_id).all()

    return jsonify({"message": "item successfully fetched", "item": items_schema.dump(item_query)}), 200


def item_delete(req, item_id):
    item_query = db.session.query(Items).filter(Items.item_id == item_id).first()

    db.session.delete(item_query)
    db.session.commit()

    return jsonify({"message": "item successfully deleted"}), 200



    
