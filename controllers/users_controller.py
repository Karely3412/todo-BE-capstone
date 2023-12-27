from flask import jsonify, request
from db import db

from models.users import Users, user_schema, users_schema


def user_add():
    return jsonify({"message": "test return"})