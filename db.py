from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects.postgres import 


__all__ = ('db', 'init_db')

db = SQLAlchemy()

def init_db(app=None, db=None):
    if isinstance(app, Flask) and isinstance(db, SQLAlchemy):
        db.init_app(app)

