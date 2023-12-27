from flask import Flask, jsonify, request
import psycopg2 
import os
from flask_marshmallow import Marshmallow

from db import * 

from routes.auth_tokens_routes import auth_token 
from routes.check_lists_routes import check_list
from routes.users_routes import user
from routes.items_routes import item

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

app.register_blueprint(auth_token)
app.register_blueprint(check_list)
app.register_blueprint(user)
app.register_blueprint(item)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")

create_tables()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8086', debug=True)