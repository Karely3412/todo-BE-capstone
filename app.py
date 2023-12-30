from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow 
from flask_bcrypt import generate_password_hash
import os

from db import * 

from models.users import Users, user_schema

from routes.users_routes import user
from routes.auth_tokens_routes import auth_token 
from routes.check_lists_routes import check_lists
from routes.items_routes import items

app = Flask(__name__)

flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_POST")

database_scheme = os.environ.get("DATABASE_SCHEME")
database_user = os.environ.get("DATABASE_USER")
database_address = os.environ.get("DATABASE_ADDRESS")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")


app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_scheme}{database_user}@{database_address}:{database_port}/{database_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)
ma = Marshmallow(app)

app.register_blueprint(user)
app.register_blueprint(auth_token)
app.register_blueprint(check_lists)
app.register_blueprint(items)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")

        first_name = 'super'
        last_name = 'admin'
        email = 'test@test.com'
        phone = "000-000-0000"
        address = "1234 Dream Blvd."
        active = True

        user_query = db.session.query(Users).filter(Users.email == email).first()

        if not user_query:
            password = input("Enter Super-admin Password: ")
            new_user = Users(first_name, last_name, email, password, phone, address, active)

            password = new_user.password
            new_user.password = generate_password_hash(password).decode("utf8")

            db.session.add(new_user)
            db.session.commit()



       

create_tables()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8086', debug=True)