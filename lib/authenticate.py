import functools
from flask import jsonify
from datetime import datetime

from db import db
from models.auth_tokens import AuthTokens
from util.validate_uuid4 import validate_uuid4

def validate_token(args):
    auth_token = args.headers['auth']

    if not auth_token or not validate_uuid4(auth_token):
        return False

    existing_token = db.session.query(AuthTokens).filter(AuthTokens.auth_token == auth_token).first()

    if existing_token:
        if existing_token.expiration > datetime.now():
            return existing_token
    else:
        return False

def fail_response():
    return jsonify({"message": "authentication required"}), 401

def authenticate(func):
    @functools.wraps(func)
    def wrapper_auth_return(*args, **kwargs):
        auth_info = validate_token(args[0])

        if auth_info:
            return func(*args, **kwargs)
        else:
            return fail_response()
    return wrapper_auth_return

def authenticate_return_auth(func):
    @functools.wraps(func)
    def wrapper_auth_return(*args, **kwargs):
        auth_info = validate_token(args[0])
        kwargs['auth_info'] = auth_info

        if auth_info:
            return func(*args, **kwargs)
        else:
            return fail_response()
    return wrapper_auth_return