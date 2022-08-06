from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URIL

app = Flask(__name__)

app.secret_key = "secret key"
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URIL
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/contactsdb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(contacts)
