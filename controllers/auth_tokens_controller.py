from flask import jsonify, request
from flask_bcrypt import check_password_hash
from datetime import datetime, timedelta
from db import db

from models.users import  Users
from models.auth_tokens import AuthTokens, auth_token_schema



def auth_token_add(req):
    post_data = req.form if req.form else req.json 

    fields = ['email', 'password']

    for field in fields:
        if field in fields and not post_data[field]:
            return jsonify({"message": f'{field} is required'}), 401

    user_data = db.session.query(Users).filter(Users.email == post_data['email']).first()

    if not post_data['email'] or not post_data['password'] or not user_data:
        return jsonify({"message": "invalid login"}), 401

    valid_password = check_password_hash(user_data.password, post_data['password'])

    if not valid_password:
        return jsonify({"message": "invalid Login"}), 401

    existing_tokens = db.session.query(AuthTokens).filter(AuthTokens.user_id == user_data.user_id).all()

    expiry = datetime.now() + timedelta(hours=12)

    if existing_tokens:
        for token in existing_tokens:
            if token.expiration < datetime.now():
                db.session.delete(token)

    new_token = AuthTokens(user_data.user_id, expiry)
    db.session.add(new_token)
    db.session.commit()

    return jsonify({"message": {"auth_token": auth_token_schema.dump(new_token)}})
    